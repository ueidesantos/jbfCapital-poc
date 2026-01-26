# Diagrama de Integração - APIs JBF Capital

## Visão Executiva do Fluxo de Integração

Este diagrama apresenta de forma simples como nossa plataforma JBF Capital se conecta com a API da Creditas para oferecer simulações de empréstimo Home Equity aos nossos clientes.

---

## Fluxo Principal de Integração

```mermaid
flowchart TB
    %% Estilo visual limpo e profissional
    classDef plataforma fill:#1e40af,stroke:#1e3a8a,stroke-width:3px,color:#fff
    classDef api fill:#059669,stroke:#047857,stroke-width:3px,color:#fff
    classDef processo fill:#f59e0b,stroke:#d97706,stroke-width:2px,color:#000
    classDef dados fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff
    
    %% Componentes Principais
    Cliente[👤 Cliente JBF Capital<br/>Acessa Plataforma Web]
    Plataforma[🏢 Plataforma JBF Capital<br/>Sistema Web de Simulação]
    API[🔗 API Creditas<br/>Serviço de Empréstimos]
    
    %% Processo de Integração
    Cliente -->|1. Preenche dados da simulação| Plataforma
    
    Plataforma -->|2. Solicita autenticação| API
    API -->|3. Retorna token de acesso| Plataforma
    
    Plataforma -->|4. Consulta elegibilidade| API
    API -->|5. Confirma aprovação| Plataforma
    
    Plataforma -->|6. Solicita ofertas disponíveis| API
    API -->|7. Retorna propostas de empréstimo| Plataforma
    
    Plataforma -->|8. Apresenta melhores opções| Cliente
    
    %% Aplicar estilos
    class Cliente,Plataforma plataforma
    class API api
```

---

## O Que Acontece em Cada Etapa

### 1️⃣ **Cliente Inicia Simulação**
O cliente acessa nossa plataforma web e informa:
- Valor do imóvel
- Valor desejado do empréstimo
- Prazo de pagamento

### 2️⃣ **Autenticação Segura**
Nossa plataforma se conecta de forma segura com a API da Creditas usando credenciais autorizadas.

### 3️⃣ **Verificação de Elegibilidade**
Consultamos se o cliente pode solicitar o empréstimo baseado nos dados informados.

### 4️⃣ **Busca de Ofertas**
Solicitamos as melhores opções de empréstimo disponíveis para o perfil do cliente.

### 5️⃣ **Apresentação de Resultados**
O cliente visualiza múltiplas ofertas com:
- Valor da parcela mensal
- Taxa de juros
- Prazo total
- Custo total da operação

---

## Componentes do Sistema

| Componente | Descrição | Responsabilidade |
|------------|-----------|------------------|
| **🏢 Plataforma JBF Capital** | Sistema web responsivo | Interface com cliente e gerenciamento de solicitações |
| **🔗 API Creditas** | Serviço externo de empréstimos | Processamento de elegibilidade e geração de ofertas |
| **👤 Cliente** | Usuário final | Inicia processo de simulação |

---

## APIs Integradas

### 🔐 **API de Autenticação**
- **Finalidade**: Garantir acesso seguro ao sistema
- **Requisição**: Credenciais da JBF Capital
- **Resposta**: Token de acesso temporário

### ✅ **API de Elegibilidade**
- **Finalidade**: Verificar se cliente pode solicitar empréstimo
- **Requisição**: Dados do imóvel e valor desejado
- **Resposta**: Aprovado ou não aprovado

### 💰 **API de Ofertas**
- **Finalidade**: Buscar melhores condições de empréstimo
- **Requisição**: Perfil do cliente e valor solicitado
- **Resposta**: Lista de ofertas personalizadas

### 📝 **API de Proposta**
- **Finalidade**: Formalizar interesse do cliente
- **Requisição**: Oferta escolhida e dados completos
- **Resposta**: Número da proposta e próximos passos

---

## Fluxo Detalhado de Dados

```mermaid
sequenceDiagram
    participant C as 👤 Cliente
    participant P as 🏢 Plataforma JBF
    participant A as 🔗 API Creditas

    Note over C,A: INÍCIO DO PROCESSO

    C->>P: Acessa plataforma e preenche formulário
    Note over P: Valida dados localmente
    
    P->>A: Solicita autenticação
    A->>P: Retorna token de acesso
    
    P->>A: Envia dados para verificação de elegibilidade
    A->>P: Confirma: Cliente está elegível
    
    P->>A: Solicita ofertas personalizadas
    A->>P: Retorna lista de ofertas (taxas, prazos, parcelas)
    
    P->>C: Exibe ofertas ao cliente
    
    C->>P: Seleciona oferta desejada
    P->>A: Cria proposta formal
    A->>P: Confirma proposta criada
    
    P->>C: Apresenta número da proposta e próximos passos
    
    Note over C,A: FIM DO PROCESSO
```

---

## Benefícios da Integração

✅ **Agilidade**: Resposta em tempo real para o cliente  
✅ **Precisão**: Ofertas baseadas em dados reais e atualizados  
✅ **Segurança**: Comunicação criptografada entre sistemas  
✅ **Escalabilidade**: Capacidade de atender múltiplos clientes simultaneamente  
✅ **Transparência**: Cliente vê todas as opções disponíveis  

---

## Tecnologias Utilizadas

- **Plataforma Web**: HTML5, CSS3, JavaScript
- **Protocolo**: HTTPS (comunicação segura)
- **Formato de Dados**: JSON (leve e eficiente)
- **Autenticação**: OAuth 2.0 (padrão de mercado)

---

## Resumo Executivo

Nossa integração com a API da Creditas permite que clientes JBF Capital tenham acesso instantâneo a simulações de empréstimo Home Equity de forma totalmente digital e segura. O processo é rápido, transparente e oferece múltiplas opções para o cliente escolher a que melhor se adequa ao seu perfil.

**Tempo médio de resposta**: Menos de 2 segundos  
**Disponibilidade**: 24/7  
**Segurança**: Criptografia de ponta a ponta  

---

*Última atualização: Janeiro 2026*  
*JBF Capital © 2026 - Todos os direitos reservados*
