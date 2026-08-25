# 2. Arquitetura Conceitual

## 2.1 Visão geral

A arquitetura deste projeto representa, de forma conceitual, os principais componentes necessários para estruturar um agente conversacional denominado **Assistente de Atendimento e Suporte**.

O modelo foi elaborado para fins de documentação e estudo. Ele não representa uma arquitetura extraída de uma implementação real no Microsoft Copilot Studio.

## 2.2 Arquitetura proposta

```text
                         ┌─────────────────────┐
                         │       Usuário       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Interface de        │
                         │ interação           │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Agente conversacional│
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌────────────────────────────┐
                    │ Identificação da necessidade│
                    └─────────────┬──────────────┘
                                  │
              ┌───────────────────┼──────────────────────────┐
              │                   │             │            │
              ▼                   ▼             ▼            ▼
        ┌────────────┐      ┌────────────┐ ┌──────────────┐ ┌────────────────┐
        │  Dúvidas   │      │  Suporte   │ │ Informações  │ │ Entrada        │
        └─────┬──────┘      └─────┬──────┘ └──────┬───────┘ │ ambígua        │
              │                   │               │         └───────┬────────┘
              │                   │               │                 ▼
              │                   │               │        ┌────────────────┐
              │                   │               │        │ Esclarecimento │
              │                   │               │        └───────┬────────┘
              │                   │               │                │
              └───────────────────┼───────────────┼────────────────┘
                                  ▼
                         ┌─────────────────────┐
                         │      Resposta       │
                         └──────────┬──────────┘
                                    │
                       ┌────────────┴────────────┐
                       │                         │
                       ▼                         ▼
                Nova solicitação           Encerramento

Fora do escopo: quando identificado, o agente informa a limitação e orienta
sobre os caminhos disponíveis, sem representar uma configuração real.
```

## 2.3 Usuário

O usuário representa a pessoa que interage com o agente. A interação pode começar por uma saudação, uma pergunta, uma solicitação de suporte ou um pedido de informação.

## 2.4 Interface de interação

A interface representa, de forma conceitual, o ponto de entrada e saída da conversa entre o usuário e o agente. Ela não corresponde a uma interface específica comprovadamente configurada no Microsoft Copilot Studio.

## 2.5 Agente conversacional

O agente representa o componente responsável por conduzir a experiência conversacional. Neste projeto conceitual, foi definido o agente **Assistente de Atendimento e Suporte**.

Seu objetivo é orientar o usuário em relação às categorias definidas para o cenário:

- Dúvidas;
- Suporte;
- Informações;
- entrada ambígua;
- fora do escopo.

## 2.6 Identificação da necessidade

Esta etapa representa a decisão conceitual sobre qual caminho deve ser seguido a partir da solicitação do usuário.

Uma entrada ambígua não é tratada como fora do escopo: primeiro deve ser solicitado esclarecimento e, depois, a necessidade deve ser identificada novamente.

## 2.7 Tópico de Dúvidas

Representa solicitações nas quais o usuário busca explicações ou esclarecimentos.

**Exemplos:**

- "Tenho uma dúvida."
- "Como funciona?"
- "Pode me explicar?"

**Resultado esperado:** fornecer uma resposta baseada nas informações disponíveis ou informar que não há dados suficientes para responder.

## 2.8 Tópico de Suporte

Representa situações nas quais o usuário relata um problema ou solicita orientação.

**Exemplos:**

- "Estou com um problema."
- "Preciso de ajuda."
- "Não consigo acessar minha conta."

**Resultado esperado:** solicitar informações relevantes e apresentar orientações compatíveis com o escopo definido.

## 2.9 Tópico de Informações

Representa solicitações gerais sobre o serviço ou contexto do agente.

**Exemplos:**

- "Quero informações."
- "Quais serviços estão disponíveis?"
- "Onde encontro informações?"

## 2.10 Tratamento de entradas ambíguas

Quando a intenção do usuário não puder ser identificada com segurança, o fluxo conceitual prevê uma solicitação de esclarecimento antes do direcionamento.

Exemplo:

> Posso ajudar. Você precisa de esclarecimento, suporte ou informações?

Esse comportamento é uma decisão de projeto e não representa uma configuração comprovada no Microsoft Copilot Studio.

## 2.11 Tratamento de entradas fora do escopo

O projeto prevê um caminho específico para solicitações que não estejam relacionadas ao escopo definido.

Exemplo:

> Não consigo ajudar com essa solicitação dentro do escopo atual. Posso ajudar com dúvidas, suporte ou informações relacionadas ao serviço.

Esse comportamento é uma decisão de projeto e não representa uma configuração comprovada no Microsoft Copilot Studio.

## 2.12 Orquestração e seleção de recursos

Esta camada representa, conceitualmente, o processo utilizado pelo agente para determinar quais recursos devem participar da resposta.

Dependendo da configuração utilizada no Microsoft Copilot Studio, a orquestração pode envolver tópicos, ferramentas, fontes de conhecimento e outros recursos disponíveis para o agente.

A implementação exata dessa camada não foi realizada neste projeto e, portanto, não é apresentada como configuração comprovada.

## 2.13 IA generativa

A IA generativa é considerada neste projeto como uma possibilidade de implementação para ampliar a capacidade de resposta do agente.

Entre os possíveis usos conceituais estão:

- geração de respostas em linguagem natural;
- tratamento de perguntas abertas;
- apoio à formulação de respostas;
- utilização de conhecimento disponível para elaboração de respostas.

A utilização efetiva desses recursos não foi implementada ou testada neste projeto.

## 2.14 Encerramento

Após o atendimento, o usuário pode iniciar uma nova solicitação ou encerrar a conversa. Quando deseja continuar, o fluxo retorna à etapa de identificação da necessidade.

## 2.15 Princípios arquiteturais

### Clareza

Os caminhos conversacionais devem ser compreensíveis e organizados.

### Modularidade

Os diferentes tipos de atendimento devem ser tratados como componentes separados.

### Escalabilidade

Novos caminhos podem ser adicionados posteriormente.

### Rastreabilidade

As decisões de projeto devem ser diferenciadas das funcionalidades efetivamente comprovadas.

### Confiabilidade

O agente não deve apresentar como fato uma informação que não possa ser sustentada pelas informações disponíveis.

## 2.16 Limitações

Esta arquitetura:

- não foi implementada no Microsoft Copilot Studio;
- não foi validada por execução de um agente real;
- não representa uma exportação ou captura da plataforma;
- não demonstra configurações específicas;
- não contém resultados experimentais.

Portanto, deve ser interpretada como uma **arquitetura conceitual para fins de documentação e estudo**.

## 2.17 Classificação das informações

| Elemento | Classificação |
|---|---|
| Usuário | Conceito do projeto |
| Interface de interação | Abstração conceitual |
| Assistente de Atendimento e Suporte | Decisão de projeto |
| Dúvidas | Decisão de projeto |
| Suporte | Decisão de projeto |
| Informações | Decisão de projeto |
| Entrada ambígua | Decisão de projeto |
| Tratamento fora do escopo | Decisão de projeto |
| Orquestração | Conceito técnico que depende da implementação |
| IA generativa | Recurso técnico documentado; uso neste projeto não confirmado |
| Arquitetura apresentada | Arquitetura conceitual |
| Implementação no Copilot Studio | Não realizada |
| Resultados funcionais | Não disponíveis |

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado  
**Autora:** Nágyla Silva  

Projeto integrante do portfólio prático em Inteligência Artificial, desenvolvido para demonstrar competências em treinamento e avaliação de sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em experiência em QA e Auditoria.