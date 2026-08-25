# 5. Testes

## 5.1 Objetivo

Esta seção apresenta o plano de testes do projeto **Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado**.

Os testes foram definidos para validar, em uma futura implementação, o comportamento esperado do **Assistente de Atendimento e Suporte**.

**Status atual:** os testes são **planejados e não executados**, pois o projeto não possui uma implementação funcional disponível no Microsoft Copilot Studio.

---

## 5.2 Estratégia de testes

A estratégia considera cenários representativos do fluxo conversacional:

- início da conversa;
- saudação;
- dúvidas;
- suporte;
- informações;
- solicitações fora do escopo;
- entradas ambíguas;
- continuidade;
- encerramento.

A validação futura deverá comparar o comportamento observado com o resultado esperado definido neste documento.

---

## 5.3 Casos de teste

### CT-01 — Saudação

**Objetivo:** verificar o início adequado da interação.

**Entrada:** `Olá`

**Resultado esperado:** o agente apresenta uma saudação e orienta o usuário sobre as possibilidades de atendimento.

**Status:** Planejado — não executado.

---

### CT-02 — Dúvidas

**Objetivo:** verificar o direcionamento de uma solicitação para o caminho de Dúvidas.

**Entrada:** `Tenho uma dúvida.`

**Resultado esperado:** o agente identifica a necessidade e conduz a conversa pelo caminho de Dúvidas.

**Status:** Planejado — não executado.

---

### CT-03 — Suporte

**Objetivo:** verificar o direcionamento de uma solicitação de suporte.

**Entrada:** `Estou com um problema.`

**Resultado esperado:** o agente conduz o usuário para o caminho de Suporte e solicita informações necessárias para compreender o problema.

**Status:** Planejado — não executado.

---

### CT-04 — Informações

**Objetivo:** verificar o atendimento de uma solicitação de informação.

**Entrada:** `Quero informações.`

**Resultado esperado:** o agente direciona a interação para o caminho de Informações.

**Status:** Planejado — não executado.

---

### CT-05 — Fora do escopo

**Objetivo:** verificar o tratamento de uma solicitação não relacionada ao escopo definido.

**Entrada:** `Qual será o preço do Bitcoin amanhã?`

**Resultado esperado:** o agente informa a limitação e não apresenta uma previsão como se fosse uma informação confirmada dentro do escopo do projeto.

**Status:** Planejado — não executado.

---

### CT-06 — Entrada ambígua

**Objetivo:** verificar o comportamento diante de uma solicitação insuficientemente especificada.

**Entrada:** `Preciso resolver isso.`

**Resultado esperado:** o agente solicita esclarecimentos antes de direcionar a conversa.

**Status:** Planejado — não executado.

---

### CT-07 — Continuidade

**Objetivo:** verificar a possibilidade de iniciar uma nova solicitação após um atendimento.

**Entrada:** `Sim, preciso de outra informação.`

**Resultado esperado:** o agente permite a continuidade e retorna à identificação da necessidade.

**Status:** Planejado — não executado.

---

### CT-08 — Encerramento

**Objetivo:** verificar o encerramento da interação.

**Entrada:** `Não, obrigado.`

**Resultado esperado:** o agente encerra a conversa de maneira adequada.

**Status:** Planejado — não executado.

---

## 5.4 Matriz de testes

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

---

## 5.5 Critérios de aprovação

Em uma futura execução, cada caso poderá ser classificado como:

- **Aprovado:** comportamento observado corresponde ao esperado.
- **Reprovado:** comportamento observado não corresponde ao esperado.
- **Inconclusivo:** não foi possível determinar o resultado adequadamente.
- **Não executado:** teste ainda não realizado.

Um resultado positivo deverá ser baseado em evidência da execução, e não apenas na expectativa descrita neste documento.

---

## 5.6 Evidências

Quando os testes forem efetivamente executados, recomenda-se registrar, para cada caso:

- data da execução;
- ambiente utilizado;
- entrada enviada;
- resposta recebida;
- resultado observado;
- classificação do teste;
- captura de tela ou outra evidência verificável, quando apropriado.

Enquanto não houver execução real, não serão apresentadas capturas de tela ou resultados como se fossem evidências funcionais.

---

## 5.7 Limitações

Os testes documentados nesta seção são **casos de teste planejados**.

Não foram executados porque a autora não possui acesso ao ambiente original do Microsoft Copilot Studio utilizado para a implementação do cenário.

Consequentemente, este documento não apresenta métricas de desempenho, taxa de acerto ou resultados funcionais reais.

---

## 5.8 Rastreabilidade

Os casos de teste estão relacionados aos requisitos definidos em `docs/04-requisitos/README.md`:

| Teste | Requisitos relacionados |
|---|---|
| CT-01 | RF-01, RF-02 |
| CT-02 | RF-03, RF-04 |
| CT-03 | RF-03, RF-05 |
| CT-04 | RF-03, RF-06 |
| CT-05 | RF-08, RF-12, RNF-07, RNF-08 |
| CT-06 | RF-07, RNF-08 |
| CT-07 | RF-09 |
| CT-08 | RF-10 |

---

## 5.9 Classificação das informações

| Informação | Classificação |
|---|---|
| Casos CT-01 a CT-08 | Testes planejados |
| Entradas | Cenários ilustrativos |
| Resultados esperados | Especificação do projeto |
| Resultados observados | Não disponíveis |
| Evidências funcionais | Não disponíveis |
| Execução no Copilot Studio | Não realizada |

---

## 5.10 Observação

Os casos de teste foram elaborados com auxílio de Inteligência Artificial e submetidos a análise crítica.

Os resultados esperados não devem ser confundidos com resultados de execução. Qualquer futura evidência deverá ser registrada separadamente e vinculada ao respectivo caso de teste.

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado

**Autora:** Nágyla Silva

Projeto integrante do portfólio prático em Inteligência Artificial,
desenvolvido para demonstrar competências em treinamento e avaliação de
sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às
funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em
experiência em QA e Auditoria.