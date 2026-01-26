/**
 * Home Equity Loan Simulation Application
 * JBF Capital POC
 * 
 * This application simulates home equity loan offers using the Creditas Mock API
 */

// ===================================
// API Configuration
// ===================================

/**
 * Base URL for the mock API server
 * Can be easily replaced with real Creditas API in production
 */
const API_CONFIG = {
    BASE_URL: 'https://85161e3c-30a2-420a-b976-c47884d97a74.mock.pstmn.io',
    ENDPOINTS: {
        AUTH: '/api/affiliate_clients/tokens',
        OFFERS: '/offers',
        ELIGIBILITY: '/eligibility'
    }
};

// ===================================
// Application State
// ===================================

const appState = {
    accessToken: null,
    currentOffers: [],
    formData: {
        propertyValue: 0,
        requestedAmount: 0,
        term: 0
    }
};

// ===================================
// DOM Elements
// ===================================

const elements = {
    form: document.getElementById('simulationForm'),
    propertyValueInput: document.getElementById('propertyValue'),
    requestedAmountInput: document.getElementById('requestedAmount'),
    termSelect: document.getElementById('term'),
    simulateBtn: document.getElementById('simulateBtn'),
    resultsSection: document.getElementById('resultsSection'),
    offersContainer: document.getElementById('offersContainer'),
    noResultsMessage: document.getElementById('noResultsMessage'),
    errorSection: document.getElementById('errorSection'),
    errorMessage: document.getElementById('errorMessage'),
    whatsappContainer: document.getElementById('whatsappContainer'),
    whatsappBtn: document.getElementById('whatsappBtn')
};

// ===================================
// WhatsApp Configuration
// ===================================

const WHATSAPP_CONFIG = {
    PHONE_NUMBER: '5511993652951', // Format: country code + area code + number
    BASE_URL: 'https://wa.me/'
};

// ===================================
// Utility Functions
// ===================================

/**
 * Format number to Brazilian currency format
 */
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL',
        minimumFractionDigits: 2
    }).format(value);
}

/**
 * Format number with thousand separators
 */
function formatNumber(value) {
    return new Intl.NumberFormat('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).format(value);
}

/**
 * Parse currency string to number
 */
function parseCurrency(value) {
    if (typeof value === 'number') return value;
    return parseFloat(value.replace(/[^\d,]/g, '').replace(',', '.')) || 0;
}

/**
 * Apply currency mask to input
 */
function applyCurrencyMask(input) {
    let value = input.value.replace(/\D/g, '');
    value = (parseInt(value) / 100).toFixed(2);
    value = value.replace('.', ',');
    value = value.replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.');
    input.value = value;
}

/**
 * Validate form field
 */
function validateField(field) {
    const errorElement = document.getElementById(`${field.name}Error`);
    let isValid = true;
    let errorMessage = '';

    // Check if required field is empty
    if (field.hasAttribute('required') && !field.value.trim()) {
        isValid = false;
        errorMessage = 'Este campo é obrigatório';
    }

    // Specific validations
    if (field.name === 'propertyValue' && field.value) {
        const value = parseCurrency(field.value);
        if (value < 100000) {
            isValid = false;
            errorMessage = 'Valor mínimo do imóvel: R$ 100.000,00';
        }
    }

    if (field.name === 'requestedAmount' && field.value) {
        const requestedValue = parseCurrency(field.value);
        const propertyValue = parseCurrency(elements.propertyValueInput.value);
        
        if (requestedValue < 50000) {
            isValid = false;
            errorMessage = 'Valor mínimo do empréstimo: R$ 50.000,00';
        } else if (propertyValue && requestedValue > propertyValue * 0.7) {
            isValid = false;
            errorMessage = 'Valor máximo: 70% do valor do imóvel';
        }
    }

    // Update UI
    if (isValid) {
        field.classList.remove('error');
        errorElement.textContent = '';
    } else {
        field.classList.add('error');
        errorElement.textContent = errorMessage;
    }

    return isValid;
}

/**
 * Validate entire form
 */
function validateForm() {
    const propertyValueValid = validateField(elements.propertyValueInput);
    const requestedAmountValid = validateField(elements.requestedAmountInput);
    const termValid = validateField(elements.termSelect);

    return propertyValueValid && requestedAmountValid && termValid;
}

/**
 * Show loading state
 */
function setLoadingState(isLoading) {
    const btnText = elements.simulateBtn.querySelector('.btn-text');
    const btnLoader = elements.simulateBtn.querySelector('.btn-loader');

    if (isLoading) {
        elements.simulateBtn.disabled = true;
        btnText.textContent = 'Simulando...';
        btnLoader.style.display = 'inline-block';
    } else {
        elements.simulateBtn.disabled = false;
        btnText.textContent = 'Simular Empréstimo';
        btnLoader.style.display = 'none';
    }
}

/**
 * Show error message
 */
function showError(message) {
    elements.errorMessage.textContent = message;
    elements.errorSection.style.display = 'block';
    elements.resultsSection.style.display = 'none';
    
    // Scroll to error
    elements.errorSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/**
 * Hide error message
 */
function hideError() {
    elements.errorSection.style.display = 'none';
}

// ===================================
// API Functions
// ===================================

/**
 * Get authentication token
 * NOTE: In production, credentials should be stored securely on the server-side
 * and never exposed in client-side code. This is a POC using mock credentials.
 */
async function getAuthToken() {
    try {
        const response = await fetch(`${API_CONFIG.BASE_URL}${API_CONFIG.ENDPOINTS.AUTH}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                // SECURITY NOTE: These are MOCK credentials for POC demonstration only
                // In production, authentication should happen server-side
                client_id: 'poc-client-id',
                client_secret: 'poc-client-secret',
                grant_type: 'client_credentials'
            })
        });

        if (!response.ok) {
            throw new Error('Falha na autenticação');
        }

        const data = await response.json();
        appState.accessToken = data.access_token;
        return data.access_token;
    } catch (error) {
        console.error('Authentication error:', error);
        // For mock purposes, use a dummy token if auth fails
        appState.accessToken = 'mock-token';
        return 'mock-token';
    }
}

/**
 * Calculate monthly payment using Price formula (Sistema de Amortização Francês - SAC)
 * PMT = PV × [i × (1 + i)^n] / [(1 + i)^n - 1]
 * where: PV = present value, i = monthly interest rate (decimal), n = number of periods
 */
function calculateMonthlyPayment(amount, monthlyRate, installments) {
    const rate = monthlyRate / 100; // Convert percentage to decimal
    const numerator = rate * Math.pow(1 + rate, installments);
    const denominator = Math.pow(1 + rate, installments) - 1;
    return amount * (numerator / denominator);
}

/**
 * Generate mock offers locally (fallback when API is unavailable)
 * NOTE: These are mock values for POC demonstration purposes only
 */
function generateMockOffers(propertyValue, requestedAmount) {
    console.log('Using local mock offers as fallback');
    
    // IOF calculation constant (0.5% for demonstration)
    const IOF_RATE = 0.005;
    
    // Generate realistic mock offers based on requested amount
    const offers = [
        {
            id: 'OFR-LOCAL-001',
            productType: 'HOME_EQUITY',
            amount: requestedAmount,
            rate: 1.20,
            monthlyRate: 0.12,
            installments: 120,
            monthlyPayment: calculateMonthlyPayment(requestedAmount, 0.12, 120),
            cet: 1.35,
            iof: requestedAmount * IOF_RATE,
            validUntil: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString()
        },
        {
            id: 'OFR-LOCAL-002',
            productType: 'HOME_EQUITY',
            amount: requestedAmount,
            rate: 1.15,
            monthlyRate: 0.115,
            installments: 96,
            monthlyPayment: calculateMonthlyPayment(requestedAmount, 0.115, 96),
            cet: 1.28,
            iof: requestedAmount * IOF_RATE,
            validUntil: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString()
        },
        {
            id: 'OFR-LOCAL-003',
            productType: 'HOME_EQUITY',
            amount: requestedAmount,
            rate: 1.10,
            monthlyRate: 0.11,
            installments: 84,
            monthlyPayment: calculateMonthlyPayment(requestedAmount, 0.11, 84),
            cet: 1.22,
            iof: requestedAmount * IOF_RATE,
            validUntil: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString()
        }
    ];
    
    return offers;
}

/**
 * Get loan offers from API
 */
async function getOffers(propertyValue, requestedAmount) {
    try {
        // Ensure we have a token
        if (!appState.accessToken) {
            await getAuthToken();
        }

        const response = await fetch(`${API_CONFIG.BASE_URL}${API_CONFIG.ENDPOINTS.OFFERS}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${appState.accessToken}`
            },
            body: JSON.stringify({
                productType: 'HOME_EQUITY',
                // PRIVACY NOTE: This is a MOCK CPF for POC demonstration only
                // In production, user CPF should be collected securely and validated
                cpf: '12345678900',
                requestedAmount: requestedAmount,
                propertyValue: propertyValue
            })
        });

        if (!response.ok) {
            throw new Error('Erro ao buscar ofertas');
        }

        const data = await response.json();
        return data.offers || [];
    } catch (error) {
        console.error('Get offers error:', error);
        // Fallback to local mock offers if API is unavailable
        console.log('Falling back to local mock offers');
        return generateMockOffers(propertyValue, requestedAmount);
    }
}

// ===================================
// Offer Rendering
// ===================================

/**
 * Create offer card HTML
 */
function createOfferCard(offer, index, isBestOffer = false) {
    const installmentYears = Math.floor(offer.installments / 12);
    const installmentMonths = offer.installments % 12;
    const installmentText = installmentYears > 0 
        ? `${installmentYears} ${installmentYears === 1 ? 'ano' : 'anos'}${installmentMonths > 0 ? ` e ${installmentMonths} ${installmentMonths === 1 ? 'mês' : 'meses'}` : ''}`
        : `${installmentMonths} ${installmentMonths === 1 ? 'mês' : 'meses'}`;

    return `
        <div class="offer-card ${isBestOffer ? 'best-offer' : ''}" role="article" aria-label="Oferta ${index + 1}">
            ${isBestOffer ? '<span class="offer-badge">Melhor Oferta</span>' : ''}
            
            <div class="offer-highlight">
                <div class="offer-amount">${formatCurrency(offer.amount)}</div>
                <div class="offer-payment">
                    Parcelas de <span class="offer-payment-value">${formatCurrency(offer.monthlyPayment)}</span>
                </div>
            </div>
            
            <div class="offer-details">
                <div class="detail-item">
                    <span class="detail-label">Taxa Mensal</span>
                    <span class="detail-value">${formatNumber(offer.monthlyRate)}%</span>
                </div>
                
                <div class="detail-item">
                    <span class="detail-label">Taxa Anual</span>
                    <span class="detail-value">${formatNumber(offer.rate)}%</span>
                </div>
                
                <div class="detail-item">
                    <span class="detail-label">Prazo</span>
                    <span class="detail-value">${offer.installments}x</span>
                </div>
                
                <div class="detail-item">
                    <span class="detail-label">Período</span>
                    <span class="detail-value">${installmentText}</span>
                </div>
                
                <div class="detail-item">
                    <span class="detail-label">CET (a.a.)</span>
                    <span class="detail-value">${formatNumber(offer.cet)}%</span>
                </div>
                
                <div class="detail-item">
                    <span class="detail-label">IOF</span>
                    <span class="detail-value">${formatCurrency(offer.iof)}</span>
                </div>
            </div>
        </div>
    `;
}

/**
 * Display offers to user
 */
function displayOffers(offers) {
    if (!offers || offers.length === 0) {
        elements.offersContainer.innerHTML = '';
        elements.noResultsMessage.style.display = 'block';
        elements.whatsappContainer.style.display = 'none';
        elements.resultsSection.style.display = 'block';
        return;
    }

    // Sort offers by best rate (lower is better)
    const sortedOffers = [...offers].sort((a, b) => a.monthlyRate - b.monthlyRate);

    // Generate HTML for all offers
    const offersHTML = sortedOffers.map((offer, index) => 
        createOfferCard(offer, index, index === 0)
    ).join('');

    elements.offersContainer.innerHTML = offersHTML;
    elements.noResultsMessage.style.display = 'none';
    elements.whatsappContainer.style.display = 'block';
    elements.resultsSection.style.display = 'block';

    // Scroll to results
    elements.resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ===================================
// WhatsApp Integration
// ===================================

/**
 * Generate WhatsApp message with simulation data
 */
function generateWhatsAppMessage() {
    const { propertyValue, requestedAmount, term } = appState.formData;
    const bestOffer = appState.currentOffers.length > 0 ? appState.currentOffers[0] : null;
    
    if (!bestOffer) {
        return null;
    }

    // Calculate installment period text
    const installmentYears = Math.floor(bestOffer.installments / 12);
    const installmentMonths = bestOffer.installments % 12;
    const installmentText = installmentYears > 0 
        ? `${installmentYears} ${installmentYears === 1 ? 'ano' : 'anos'}${installmentMonths > 0 ? ` e ${installmentMonths} ${installmentMonths === 1 ? 'mês' : 'meses'}` : ''}`
        : `${installmentMonths} ${installmentMonths === 1 ? 'mês' : 'meses'}`;

    // Build the message
    let message = `*Simulação de Empréstimo Home Equity - JBF Capital*\n\n`;
    message += `📋 *Dados da Simulação:*\n`;
    message += `• Valor do Imóvel: ${formatCurrency(propertyValue)}\n`;
    message += `• Valor Solicitado: ${formatCurrency(requestedAmount)}\n`;
    message += `• Prazo Desejado: ${term} meses (${Math.floor(term/12)} ${Math.floor(term/12) === 1 ? 'ano' : 'anos'})\n\n`;
    
    message += `💰 *Melhor Oferta Encontrada:*\n`;
    message += `• Valor do Empréstimo: ${formatCurrency(bestOffer.amount)}\n`;
    message += `• Parcela Mensal: ${formatCurrency(bestOffer.monthlyPayment)}\n`;
    message += `• Quantidade de Parcelas: ${bestOffer.installments}x\n`;
    message += `• Período: ${installmentText}\n`;
    message += `• Taxa Mensal: ${formatNumber(bestOffer.monthlyRate)}%\n`;
    message += `• Taxa Anual: ${formatNumber(bestOffer.rate)}%\n`;
    message += `• CET (a.a.): ${formatNumber(bestOffer.cet)}%\n`;
    message += `• IOF: ${formatCurrency(bestOffer.iof)}\n\n`;
    
    message += `Gostaria de mais informações sobre esta oferta!`;
    
    return message;
}

/**
 * Open WhatsApp with simulation data
 */
function openWhatsApp() {
    const message = generateWhatsAppMessage();
    
    if (!message) {
        alert('Não há dados de simulação para enviar.');
        return;
    }

    // Encode the message for URL
    const encodedMessage = encodeURIComponent(message);
    
    // Build WhatsApp URL
    const whatsappUrl = `${WHATSAPP_CONFIG.BASE_URL}${WHATSAPP_CONFIG.PHONE_NUMBER}?text=${encodedMessage}`;
    
    // Open WhatsApp in a new window/tab
    window.open(whatsappUrl, '_blank');
}

// ===================================
// Form Handling
// ===================================

/**
 * Handle form submission
 */
async function handleFormSubmit(event) {
    event.preventDefault();
    
    // Hide previous errors
    hideError();

    // Validate form
    if (!validateForm()) {
        return;
    }

    // Get form values
    const propertyValue = parseCurrency(elements.propertyValueInput.value);
    const requestedAmount = parseCurrency(elements.requestedAmountInput.value);
    const term = parseInt(elements.termSelect.value);

    // Store in state
    appState.formData = { propertyValue, requestedAmount, term };

    // Show loading
    setLoadingState(true);

    try {
        // Get offers from API
        const offers = await getOffers(propertyValue, requestedAmount);
        
        // Filter offers by selected term (with some flexibility: ±12 months)
        const filteredOffers = offers.filter(offer => 
            Math.abs(offer.installments - term) <= 12
        );

        // If no offers match the exact term, show all offers
        const offersToDisplay = filteredOffers.length > 0 ? filteredOffers : offers;

        // Store offers
        appState.currentOffers = offersToDisplay;

        // Display results
        displayOffers(offersToDisplay);

    } catch (error) {
        console.error('Simulation error:', error);
        showError('Não foi possível realizar a simulação. Por favor, tente novamente em alguns instantes.');
    } finally {
        setLoadingState(false);
    }
}

// ===================================
// Event Listeners Setup
// ===================================

/**
 * Initialize event listeners
 */
function initEventListeners() {
    // Form submission
    elements.form.addEventListener('submit', handleFormSubmit);

    // Currency mask for inputs
    elements.propertyValueInput.addEventListener('input', (e) => {
        applyCurrencyMask(e.target);
    });

    elements.requestedAmountInput.addEventListener('input', (e) => {
        applyCurrencyMask(e.target);
    });

    // Field validation on blur
    elements.propertyValueInput.addEventListener('blur', (e) => {
        validateField(e.target);
    });

    elements.requestedAmountInput.addEventListener('blur', (e) => {
        validateField(e.target);
    });

    elements.termSelect.addEventListener('change', (e) => {
        validateField(e.target);
    });

    // Clear error on input
    elements.propertyValueInput.addEventListener('focus', () => {
        elements.propertyValueInput.classList.remove('error');
        document.getElementById('propertyValueError').textContent = '';
    });

    elements.requestedAmountInput.addEventListener('focus', () => {
        elements.requestedAmountInput.classList.remove('error');
        document.getElementById('requestedAmountError').textContent = '';
    });

    elements.termSelect.addEventListener('focus', () => {
        elements.termSelect.classList.remove('error');
        document.getElementById('termError').textContent = '';
    });

    // WhatsApp button click
    elements.whatsappBtn.addEventListener('click', openWhatsApp);
}

// ===================================
// Application Initialization
// ===================================

/**
 * Initialize the application
 */
function initApp() {
    console.log('JBF Capital - Home Equity Simulation POC');
    console.log('API Base URL:', API_CONFIG.BASE_URL);

    // Setup event listeners
    initEventListeners();

    // Pre-authenticate (optional - for better UX)
    getAuthToken().catch(error => {
        console.warn('Pre-authentication failed, will retry on simulation:', error);
    });

    console.log('Application initialized successfully');
}

// Start the application when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}
