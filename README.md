# 🔐 Python Security Scanner

Projeto desenvolvido com o objetivo de analisar aspectos básicos de segurança em aplicações web e APIs, aplicando conceitos fundamentais de **Cybersecurity, HTTP, Autenticação, Port Scanning e Secure Coding**.

O scanner recebe uma URL como alvo e executa uma série de verificações automáticas, gerando ao final um **relatório técnico em texto** com os resultados da análise.

---

## 🎯 Objetivo do Projeto

Este projeto tem como finalidade:

- Aplicar conceitos práticos de segurança defensiva
- Automatizar verificações básicas de segurança em APIs
- Demonstrar entendimento sobre:
  - HTTP Security Headers
  - Port Scanning
  - Authentication & Authorization
- Gerar relatórios claros e interpretáveis
- Servir como projeto prático para portfólio na área de **Cybersecurity / Backend**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Biblioteca padrão:
  - `socket`
  - `requests`
  - `urllib`
- Conceitos de:
  - HTTP
  - APIs REST
  - Segurança de aplicações
  - Análise estática e dinâmica simples

---

## 📂 Estrutura do Projeto
```bash
python-security-scanner/
├── scanner/
│ ├── headers_check.py   # Verificação de headers de segurança
│ ├── open_port_check.py   # Scanner de portas TCP
│ ├── auth_check.py   # Teste de autenticação e autorização
│
├── reports/
│ └── sample_report.txt   # Exemplo de relatório gerado
│
├── main.py   # Arquivo principal do scanner
├── requirements.txt   # Dependências do projeto
└── README.md
```

---

## 🔍 Funcionalidades

### ✅ 1. Security Headers Check

Verifica a presença de headers HTTP importantes para segurança, como:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Referrer-Policy`

Esses headers ajudam a prevenir ataques como:

- XSS
- Clickjacking
- MIME sniffing
- Vazamento de informações

---

### ✅ 2. Open Port Scan

Realiza um scan de portas TCP comuns, identificando serviços potencialmente expostos, como:

- Bancos de dados
- Serviços administrativos
- APIs abertas indevidamente

O objetivo é alertar sobre **exposição desnecessária de serviços**.

---

### ✅ 3. Authentication & Authorization Check

Testa endpoints sensíveis da API para verificar se:

- Estão protegidos por autenticação
- Retornam corretamente `401 Unauthorized` ou `403 Forbidden` quando acessados sem token

Isso valida boas práticas de **controle de acesso**.

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

- Python 3 instalado
- API ou aplicação web para testes (preferencialmente local)

### Instalação das dependências
```bash
pip install -r requirements.txt
```
### Execução do scanner
```bash
python main.py http://localhost:8080
```
O scanner irá executar as verificações e gerar um relatório automaticamente.

## 📄 Relatório de Segurança

Após a execução, um relatório será gerado em:
```bash
reports/sample_report.txt
```
Exemplo de saída
```bash
========================================
 Python Security Scanner - Scan Report
========================================

Target URL: http://localhost:8080
Host: localhost
Scan Date: 2026-01-11 12:51:03.451308

Checks executed:
- HTTP Security Headers
- Open Ports Scan
- Authentication & Authorization

========================================

[Security Headers]
Status: WARNING
Details: Missing headers: Content-Security-Policy, Strict-Transport-Security, Referrer-Policy
----------------------------------------
[Open Ports]
Status: WARNING
Details: Open ports detected: 5432 (PostgreSQL)
----------------------------------------
[Authentication & Authorization]
Status: OK
Details: All sensitive endpoints are protected (401/403 without token).
----------------------------------------
```
## 🧪 Ambiente de Testes

Este projeto foi testado contra uma API própria desenvolvida em **Spring Boot**, garantindo que:

- Nenhum sistema de terceiros fosse afetado
- Nenhuma violação ética fosse cometida
- Todos os testes fossem realizados em ambiente controlado

⚠️ **Este scanner deve ser utilizado apenas em aplicações próprias ou com autorização explícita.**

---

## 📌 Possíveis Evoluções

- Geração de relatório em JSON ou HTML
- Suporte a HTTPS com validação de certificados
- Scan de vulnerabilidades OWASP adicionais
- Configuração de portas e headers via arquivo `.config`
- Integração com CI/CD para análise automática

---

## 👨‍💻 Autor

Projeto desenvolvido por **Gustavo**<br>
Focado em **Backend, APIs e Cybersecurity**










