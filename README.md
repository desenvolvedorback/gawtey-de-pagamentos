# Payment Gateway - Sandbox (FastAPI + Fraud Java)

**Última atualização:** 09/10/2025

## Visão geral
Gateway de pagamento modular para uso em ambiente de testes/sandbox. 
Inclui: FastAPI backend, microserviço de fraude (Spring Boot), Redis (Celery), PostgreSQL, frontend checkout e admin (HTML/JS), tokenização em sandbox (Fernet), client-side encryption.

> ***AVISO***: Este projeto é para testes locais/sandbox. **Não processe cartões reais** sem certificação PCI e HSM/KMS em produção.

---

## Requisitos locais
- Docker & Docker Compose (recomendado)
- (Opcional) Python 3.11 e pip se quiser rodar sem Docker

---

## Como rodar localmente (Docker)
1. Copie `.env.example` para `.env` e ajuste se quiser. (ou exporte variáveis)
2. Build e startup:
```bash
docker-compose up --build
