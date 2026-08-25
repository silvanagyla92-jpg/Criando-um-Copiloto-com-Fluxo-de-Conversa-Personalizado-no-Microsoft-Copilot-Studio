# 3. Fluxo Conversacional

## 3.1 Objetivo

Esta seção documenta o fluxo conversacional conceitual do projeto **Assistente de Atendimento e Suporte**.

O fluxo foi elaborado para demonstrar como um agente conversacional pode organizar uma interação desde a primeira mensagem do usuário até o atendimento, a continuidade da conversa ou o encerramento.

O fluxo apresentado é uma especificação conceitual e não representa uma implementação realizada no Microsoft Copilot Studio.

## 3.2 Visão geral do fluxo

O fluxo é composto por:

1. Início da interação;
2. Saudação;
3. Identificação da necessidade;
4. Direcionamento para um caminho de atendimento;
5. Tratamento da solicitação;
6. Verificação da necessidade de continuidade;
7. Nova solicitação ou encerramento.

Os três caminhos principais são **Dúvidas**, **Suporte** e **Informações**. Também existem caminhos alternativos para **entrada ambígua** e para solicitações **fora do escopo**.

## 3.3 Fluxo principal

```text
Usuário
   │
   ▼
Início da conversa
   │
   ▼
Saudação
   │
   ▼
Identificação da necessidade
   │
   ├──────────────┬──────────────┬─────────────────┬──────────────────┐
   │              │              │                 │                  │
   ▼              ▼              ▼                 ▼                  ▼
Dúvidas        Suporte      Informações     Entrada ambígua    Fora do escopo
   │              │              │                 │                  │
   ▼              ▼              ▼                 ▼                  ▼
Responder      Orientar      Informar      Solicitar esclarec.  Informar limitação
   │              │              │                 │                  │
   │              │              │                 ▼                  │
   │              │              │       Identificação da necessidade │
   │              │              │                 │                  │
   └──────────────┴──────────────┴─────────────────┴──────────────────┘
                          │
                          ▼
                 Precisa de mais ajuda?
                       │        │
                      Sim      Não
                       │        │
                       ▼        ▼
              Nova solicitação Fim
                       │
                       └──────► Identificação da necessidade
```

A **entrada ambígua** possui tratamento diferente de uma solicitação **fora do escopo**: no primeiro caso, o agente solicita esclarecimentos e retorna à identificação da necessidade; no segundo, informa a limitação de escopo.

## 3.4 Etapa 1 — Início

A conversa começa quando o usuário envia uma mensagem ao agente.

**Exemplos:**

- "Olá."
- "Oi."
- "Preciso de ajuda."
- "Tenho uma dúvida."
- "Quero uma informação."

A mensagem inicial pode ser uma saudação ou já apresentar diretamente a necessidade do usuário.

## 3.5 Etapa 2 — Saudação

Quando apropriado, o agente apresenta uma mensagem inicial.

**Exemplo:**

> Olá! Sou o Assistente de Atendimento e Suporte. Posso ajudar com dúvidas, suporte ou informações. Como posso ajudar?

A saudação deve apresentar o agente, indicar sua finalidade, orientar o usuário sobre as possibilidades de atendimento e iniciar a interação de forma clara.

## 3.6 Etapa 3 — Identificação da necessidade

O agente deve identificar qual tipo de atendimento é mais adequado à solicitação apresentada.

| Categoria | Finalidade |
|---|---|
| Dúvidas | Responder perguntas e esclarecer conceitos |
| Suporte | Orientar sobre problemas ou dificuldades |
| Informações | Apresentar informações gerais |
| Entrada ambígua | Solicitar esclarecimentos antes de direcionar |
| Fora do escopo | Tratar solicitações não relacionadas |

A classificação apresentada é uma decisão de projeto.

## 3.7 Caminho 1 — Dúvidas

### Objetivo

Atender usuários que desejam esclarecer uma questão ou obter uma explicação.

**Exemplos:**

> Tenho uma dúvida.

> Como funciona?

> Pode me explicar?

### Fluxo

```text
Usuário apresenta dúvida
          │
          ▼
Agente identifica a solicitação
          │
          ▼
Existe informação disponível?
       ┌──┴──┐
      Sim    Não
       │      │
       ▼      ▼
   Responder  Informar limitação
       │      │
       └──┬───┘
          ▼
Precisa de mais ajuda?
```

Quando houver informação adequada, o agente deve responder de maneira clara. Quando não houver informação suficiente, deve indicar a limitação em vez de inventar uma resposta.

## 3.8 Caminho 2 — Suporte

### Objetivo

Atender usuários que relatam um problema ou precisam de orientação.

**Exemplos:**

> Estou com um problema.

> Preciso de ajuda.

> Não consigo acessar minha conta.

### Fluxo

```text
Usuário relata problema
          │
          ▼
Solicitar detalhes
          │
          ▼
Identificar problema
          │
          ▼
Existe orientação disponível?
       ┌──┴──┐
      Sim    Não
       │      │
       ▼      ▼
   Orientar  Informar limitação
       │      │
       └──┬───┘
          ▼
Precisa de mais ajuda?
```

### Exemplo de diálogo

**Usuário:** Estou com um problema.

**Agente:** Claro. Pode descrever o problema que está enfrentando?

**Usuário:** Não consigo acessar minha conta.

**Agente:** Entendi. Posso orientar você sobre os procedimentos disponíveis para recuperação de acesso.

## 3.9 Caminho 3 — Informações

### Objetivo

Atender solicitações de informações gerais relacionadas ao escopo do agente.

**Exemplos:**

> Quero informações.

> Quais serviços estão disponíveis?

> Como funciona o atendimento?

### Fluxo

```text
Usuário solicita informação
          │
          ▼
Identificar informação desejada
          │
          ▼
Informação disponível?
       ┌──┴──┐
      Sim    Não
       │      │
       ▼      ▼
   Informar  Informar limitação
       │      │
       └──┬───┘
          ▼
Precisa de mais ajuda?
```

## 3.10 Caminho 4 — Fora do escopo

O agente deve possuir comportamento definido para solicitações que não estejam relacionadas ao objetivo do projeto.

**Exemplo:**

**Usuário:** Qual será o preço do Bitcoin amanhã?

**Resposta conceitual:**

> Não consigo ajudar com essa solicitação dentro do escopo atual. Posso ajudar com dúvidas, suporte ou informações relacionadas ao serviço.

O objetivo é evitar que o agente produza uma resposta sem relação com o escopo definido.

## 3.11 Entrada ambígua

Quando não for possível determinar a necessidade do usuário, o comportamento esperado é solicitar esclarecimentos.

**Exemplo:**

**Usuário:** Preciso resolver isso.

**Agente:** Pode me explicar qual problema ou informação você precisa?

Depois que o usuário fornecer mais detalhes, a conversa deve retornar à etapa de identificação da necessidade.

## 3.12 Continuidade

Após o atendimento, o agente pode perguntar:

> Posso ajudar com mais alguma coisa?

**Sim:** retorna à identificação da necessidade.  
**Não:** segue para o encerramento.

## 3.13 Encerramento

Quando o usuário não desejar continuar, o agente encerra a interação.

**Exemplo:**

**Usuário:** Não, obrigado.

**Agente:** Tudo bem. Obrigado pela interação. Até mais!

## 3.14 Fluxos alternativos

### Usuário muda de assunto

```text
Atendimento atual
       │
       ▼
Nova necessidade
       │
       ▼
Identificação da necessidade
       │
       ▼
Novo caminho
```

### Usuário fornece informações insuficientes

```text
Solicitação
    │
    ▼
Informação insuficiente
    │
    ▼
Solicitar esclarecimento
    │
    ▼
Nova informação
    │
    ▼
Continuar atendimento
```

### Usuário encerra inesperadamente

Se o usuário interromper a interação, a conversa pode ser considerada encerrada.

## 3.15 Casos de teste planejados

| ID | Cenário | Entrada | Resultado esperado | Status |
|---|---|---|---|---|
| CT-01 | Saudação | "Olá" | Apresentar saudação | Planejado |
| CT-02 | Dúvida | "Tenho uma dúvida" | Direcionar para Dúvidas | Planejado |
| CT-03 | Suporte | "Estou com um problema" | Direcionar para Suporte | Planejado |
| CT-04 | Informação | "Quero informações" | Direcionar para Informações | Planejado |
| CT-05 | Fora do escopo | Solicitação não relacionada | Informar limitação | Planejado |
| CT-06 | Entrada ambígua | "Preciso resolver isso" | Solicitar esclarecimento | Planejado |
| CT-07 | Continuidade | "Sim" | Permitir nova solicitação | Planejado |
| CT-08 | Encerramento | "Não, obrigado" | Encerrar conversa | Planejado |

**Observação:** nenhum dos testes acima foi executado em um agente real. Eles representam casos de teste planejados para uma futura implementação.

## 3.16 Critérios de aceitação

Uma futura implementação será considerada adequada quando:

- apresentar uma saudação coerente;
- permitir identificação da necessidade;
- direcionar corretamente os três caminhos principais;
- possuir tratamento para solicitações fora do escopo;
- solicitar esclarecimentos quando necessário;
- permitir continuidade;
- permitir encerramento;
- evitar respostas sem base nas informações disponíveis.

## 3.17 Limitações

O fluxo:

- não foi implementado em um ambiente real;
- não foi executado em testes funcionais;
- não possui métricas de desempenho;
- não possui integração com sistemas externos;
- não representa uma configuração específica do Microsoft Copilot Studio.

Consequentemente, os resultados apresentados nesta documentação são **resultados esperados**, e não resultados experimentais.

## 3.18 Classificação das informações

| Informação | Classificação |
|---|---|
| Fluxo de conversa | Decisão de projeto |
| Categorias Dúvidas/Suporte/Informações | Decisão de projeto |
| Entrada ambígua | Decisão de projeto |
| Mensagens de exemplo | Conteúdo ilustrativo |
| Tratamento fora do escopo | Decisão de projeto |
| Casos de teste | Testes planejados |
| Resultados dos testes | Não disponíveis |
| Implementação no Copilot Studio | Não realizada |
| Arquitetura apresentada | Conceitual |

## 3.19 Observação

Este fluxo foi elaborado com auxílio de Inteligência Artificial e submetido a análise crítica antes de sua inclusão na documentação.

O conteúdo representa uma proposta conceitual de fluxo conversacional e não deve ser interpretado como evidência de uma implementação funcional no Microsoft Copilot Studio.

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado  
**Autora:** Nágyla Silva  

Projeto integrante do portfólio prático em Inteligência Artificial, desenvolvido para demonstrar competências em treinamento e avaliação de sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em experiência em QA e Auditoria.