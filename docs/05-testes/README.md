# Arquivo legado — Testes

> **Aviso de organização:** o conteúdo desta pasta foi preservado para não perder histórico. A versão ativa e numerada do plano de testes está em [`../06-testes/README.md`](../06-testes/README.md).

---

# 5. Testes

Esta versão histórica contém o plano de testes elaborado anteriormente. Para a documentação ativa, utilize [`../06-testes/README.md`](../06-testes/README.md), que corrige a numeração e a rastreabilidade.

## 5.1 Objetivo

Esta seção apresenta o plano de testes do projeto **Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado**.

Os testes foram definidos para validar, em uma futura implementação, o comportamento esperado do **Assistente de Atendimento e Suporte**.

**Status atual:** os testes são **planejados e não executados**.

## 5.2 Casos de teste

| ID | Cenário | Entrada representativa | Resultado esperado | Status |
|---|---|---|---|---|
| CT-01 | Saudação | Olá | Apresentar saudação | Planejado |
| CT-02 | Dúvidas | Tenho uma dúvida | Direcionar para Dúvidas | Planejado |
| CT-03 | Suporte | Estou com um problema | Direcionar para Suporte | Planejado |
| CT-04 | Informações | Quero informações | Direcionar para Informações | Planejado |
| CT-05 | Fora do escopo | Solicitação não relacionada | Informar limitação | Planejado |
| CT-06 | Entrada ambígua | Preciso resolver isso | Solicitar esclarecimento | Planejado |
| CT-07 | Continuidade | Sim | Permitir nova solicitação | Planejado |
| CT-08 | Encerramento | Não, obrigado | Encerrar conversa | Planejado |

## 5.3 Rastreabilidade histórica

A matriz ativa está em [`../06-testes/README.md`](../06-testes/README.md) e relaciona os casos CT-01 a CT-08 aos requisitos ativos em [`../05-requisitos/README.md`](../05-requisitos/README.md).

## 5.4 Limitações

Os testes não foram executados e não existem resultados funcionais reais associados a esta versão histórica.

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado

**Autora:** Nágyla Silva

Projeto integrante do portfólio prático em Inteligência Artificial,
desenvolvido para demonstrar competências em treinamento e avaliação de
sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às
funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em
experiência em QA e Auditoria.