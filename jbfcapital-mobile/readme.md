# Home Equity Loan Simulation - JBF Capital POC

## 📋 Descrição

Aplicação web responsiva para simulação de empréstimo Home Equity da JBF Capital, desenvolvida como Proof of Concept (POC) integrada à API mockada da Creditas.

## 🎯 Objetivos

- Demonstrar viabilidade técnica de integração com API da Creditas
- Fornecer experiência de usuário intuitiva e orientada à conversão
- Implementar design responsivo com abordagem mobile-first
- Simular fluxo completo de empréstimo Home Equity

## 🚀 Funcionalidades

- ✅ Formulário de simulação com validação em tempo real
- ✅ Integração com Creditas Mock API
- ✅ Fallback para ofertas locais quando API indisponível
- ✅ Exibição de múltiplas ofertas com detalhes completos
- ✅ Design responsivo (mobile, tablet, desktop)
- ✅ Formatação automática de valores em moeda brasileira
- ✅ Cálculo automático de limites (70% LTV)

## 📁 Estrutura do Projeto

```
jbfcapital-mobile/
├── index.html          # Página principal com estrutura HTML5 semântica
├── css/
│   └── styles.css      # Estilos CSS com abordagem mobile-first
├── js/
│   └── app.js          # Lógica da aplicação em JavaScript puro
└── ImagensBase/        # Imagens de referência de UX
```

## 🔧 Tecnologias Utilizadas

- **HTML5** - Estrutura semântica
- **CSS3** - Design responsivo com Flexbox e Grid
- **JavaScript (Vanilla)** - Lógica da aplicação
- **Creditas Mock API** - Integração de dados

## 🌐 API Configuration

A URL base da API está centralizada na constante `API_CONFIG` no arquivo `js/app.js`:

```javascript
const API_CONFIG = {
    BASE_URL: 'https://85161e3c-30a2-420a-b976-c47884d97a74.mock.pstmn.io',
    ENDPOINTS: {
        AUTH: '/api/affiliate_clients/tokens',
        OFFERS: '/offers',
        ELIGIBILITY: '/eligibility'
    }
};
```

Para usar a API real da Creditas, basta atualizar a `BASE_URL`.

## 📱 Responsividade

O design segue a abordagem **mobile-first** com breakpoints:

- **Mobile**: < 768px (padrão)
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🎨 Identidade Visual

- Paleta de cores inspirada na JBF Capital
- Tipografia moderna e legível
- Hierarquia visual clara
- Componentes com micro-interações

## 🔒 Validações Implementadas

- Valor mínimo do imóvel: R$ 100.000,00
- Valor mínimo do empréstimo: R$ 50.000,00
- Valor máximo do empréstimo: 70% do valor do imóvel
- Campos obrigatórios
- Formatação automática de valores

## 📊 Campos da Simulação

1. **Valor do Imóvel** - Valor estimado do imóvel a ser dado como garantia
2. **Valor Desejado** - Montante solicitado para empréstimo (até 70% do valor do imóvel)
3. **Prazo** - Período de pagamento (12 a 240 meses)

## 📈 Informações das Ofertas

Cada oferta exibe:

- Valor do empréstimo
- Valor da parcela mensal
- Taxa de juros mensal
- Taxa de juros anual
- Prazo em parcelas
- Período em anos/meses
- CET (Custo Efetivo Total)
- IOF (Imposto sobre Operações Financeiras)

## 🚀 Como Usar

### Desenvolvimento Local

1. Navegue até o diretório do projeto:
```bash
cd jbfcapital-mobile
```

2. Inicie um servidor HTTP local:
```bash
python3 -m http.server 8080
```

3. Acesse no navegador:
```
http://localhost:8080
```

### Deploy no GitHub Pages

O projeto está pronto para deploy direto no GitHub Pages:

1. Os arquivos já estão estruturados corretamente
2. Todos os caminhos são relativos
3. O `index.html` está na raiz do diretório `jbfcapital-mobile`

## 🔄 Fluxo de Uso

1. Usuário acessa a página
2. Preenche o valor do imóvel
3. Informa o valor desejado do empréstimo
4. Seleciona o prazo desejado
5. Clica em "Simular Empréstimo"
6. Sistema valida os dados
7. Sistema busca ofertas na API (ou usa fallback local)
8. Exibe resultados com múltiplas ofertas
9. Destaca a melhor oferta disponível

## 🛡️ Tratamento de Erros

- Validação de campos em tempo real
- Mensagens de erro claras e específicas
- Fallback automático para ofertas locais
- Tratamento de falhas de rede
- Feedback visual durante carregamento

## 📝 Notas Técnicas

- **Código modular**: Funções bem definidas e reutilizáveis
- **Comentários**: Documentação inline em português
- **Acessibilidade**: ARIA labels e navegação por teclado
- **Performance**: Carregamento otimizado
- **Segurança**: Validação client-side e sanitização de inputs

## 🎯 Status do Projeto

✅ **POC Completa e Funcional**

- Interface responsiva implementada
- Integração com API mockada
- Validações funcionando
- Design coerente com identidade visual
- Pronto para GitHub Pages

## 📄 Licença

Este é um projeto de demonstração (POC) para fins educacionais e de avaliação técnica.

---

**JBF Capital** © 2026 - Todos os direitos reservados.
