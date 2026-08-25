# 4. Requisitos do Projeto

## 4.1 Objetivo

Esta seção apresenta os requisitos funcionais e não funcionais definidos para o projeto **Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado**.

Os requisitos representam a especificação conceitual do agente **Assistente de Atendimento e Suporte**. Eles não representam requisitos extraídos de uma implementação existente no Microsoft Copilot Studio.

## 4.2 Classificação

- **RF — Requisito Funcional:** descreve uma função ou comportamento esperado do agente.
- **RNF — Requisito Não Funcional:** descreve uma característica de qualidade, restrição ou condição de funcionamento.

# 4.3 Requisitos Funcionais

## RF-01 — Iniciar atendimento

O agente deve permitir o início de uma interação com o usuário.

**Exemplo:** "Olá."

**Resultado esperado:** iniciar o fluxo de atendimento.

## RF-02 — Apresentar saudação

O agente deve apresentar uma mensagem inicial adequada ao contexto. A mensagem deve apresentar o agente, indicar sua finalidade e orientar o usuário sobre as possibilidades de atendimento.

## RF-03 — Identificar a necessidade

O agente deve identificar a necessidade apresentada pelo usuário. As categorias previstas são Dúvidas, Suporte, Informações e Fora do escopo.

## RF-04 — Atender dúvidas

O agente deve permitir o tratamento de perguntas e solicitações de esclarecimento relacionadas ao escopo definido.

## RF-05 — Prestar suporte

O agente deve permitir o tratamento de solicitações relacionadas a problemas ou dificuldades. O fluxo deve solicitar as informações necessárias e apresentar orientação compatível com o cenário.

## RF-06 — Fornecer informações

O agente deve permitir o atendimento de solicitações de informações gerais relacionadas ao escopo do projeto.

## RF-07 — Solicitar esclarecimentos

Quando a entrada do usuário não for suficientemente clara, o agente deve solicitar informações adicionais.

**Exemplo:** "Preciso resolver isso." → "Pode me explicar qual problema ou informação você precisa?"

## RF-08 — Tratar solicitações fora do escopo

O agente deve possuir comportamento definido para solicitações não relacionadas ao escopo. Deve informar sua limitação e evitar apresentar uma resposta como se possuísse conhecimento ou capacidade não disponíveis.

## RF-09 — Permitir continuidade

Após uma interação, o agente deve permitir que o usuário apresente uma nova solicitação. Caso o usuário responda positivamente à pergunta de continuidade, o fluxo deve retornar à identificação da necessidade.

## RF-10 — Encerrar atendimento

O agente deve permitir o encerramento da conversa quando o usuário não desejar continuar.

## RF-11 — Considerar contexto da interação

Quando aplicável à implementação futura, o fluxo deve considerar o contexto da conversa para evitar solicitações desnecessariamente repetitivas. A forma exata de implementação depende da plataforma e da configuração utilizada.

## RF-12 — Responder de acordo com o escopo

O agente deve priorizar respostas relacionadas à finalidade definida para o projeto. Quando não houver informação suficiente, deve comunicar a limitação em vez de inventar informações.

# 4.4 Requisitos Não Funcionais

## RNF-01 — Clareza

As respostas devem utilizar linguagem clara e compreensível.

## RNF-02 — Objetividade

As respostas devem evitar informações desnecessárias e manter foco na solicitação apresentada.

## RNF-03 — Consistência

O agente deve manter comportamento e tom de comunicação coerentes ao longo da interação.

## RNF-04 — Escalabilidade

A estrutura deve permitir a inclusão de novos caminhos conversacionais no futuro.

## RNF-05 — Manutenibilidade

Os fluxos devem ser organizados de forma que alterações futuras possam ser realizadas de maneira estruturada.

## RNF-06 — Rastreabilidade

Cada requisito deve poder ser relacionado a pelo menos um fluxo ou caso de teste.

## RNF-07 — Confiabilidade das informações

O agente não deve apresentar como fato uma informação que não possua fundamentação adequada.

## RNF-08 — Tratamento de incerteza

Quando não houver informação suficiente para responder, o comportamento esperado é comunicar a limitação.

## RNF-09 — Segurança conceitual

O agente não deve ser projetado para produzir respostas deliberadamente enganosas ou apresentar capacidades inexistentes como se fossem reais.

## RNF-10 — Transparência

As limitações do agente devem ser identificáveis na documentação.

# 4.5 Matriz de rastreabilidade

| Requisito | Fluxo relacionado | Caso de teste |
|---|---|---|
| RF-01 | Início | CT-01 |
| RF-02 | Saudação | CT-01 |
| RF-03 | Identificação | CT-02, CT-03, CT-04 |
| RF-04 | Dúvidas | CT-02 |
| RF-05 | Suporte | CT-03 |
| RF-06 | Informações | CT-04 |
| RF-07 | Entrada ambígua | CT-06 |
| RF-08 | Fora do escopo | CT-05 |
| RF-09 | Continuidade | CT-07 |
| RF-10 | Encerramento | CT-08 |
| RF-11 | Conversação | Planejado |
| RF-12 | Todos os fluxos | CT-02 a CT-06 |
| RNF-01 | Todos os fluxos | Planejado |
| RNF-02 | Todos os fluxos | Planejado |
| RNF-03 | Todos os fluxos | Planejado |
| RNF-04 | Arquitetura | Planejado |
| RNF-05 | Arquitetura | Planejado |
| RNF-06 | Documentação | Verificação documental |
| RNF-07 | Respostas | CT-05, CT-06 |
| RNF-08 | Fora do escopo | CT-05, CT-06 |
| RNF-09 | Todos os fluxos | Verificação conceitual |
| RNF-10 | Documentação | Verificação documental |

# 4.6 Prioridade

| Prioridade | Significado |
|---|---|
| Alta | Essencial para o fluxo principal |
| Média | Importante para qualidade e experiência |
| Baixa | Pode ser incorporado posteriormente |

### Alta

RF-01, RF-02, RF-03, RF-04, RF-05, RF-06, RF-07, RF-08, RF-09 e RF-10.

### Média

RF-11, RF-12, RNF-01, RNF-02, RNF-03, RNF-06, RNF-07 e RNF-08.

### Baixa

RNF-04, RNF-05, RNF-09 e RNF-10.

# 4.7 Critérios de aceitação

Uma futura implementação deverá:

1. permitir iniciar uma conversa;
2. apresentar uma saudação adequada;
3. direcionar a solicitação para o caminho correspondente;
4. permitir o fluxo de Dúvidas;
5. permitir o fluxo de Suporte;
6. permitir o fluxo de Informações;
7. tratar entradas ambíguas com solicitação de esclarecimento;
8. tratar entradas fora do escopo adequadamente;
9. permitir continuidade;
10. permitir encerramento;
11. manter clareza e consistência;
12. evitar apresentar informações sem fundamentação como fatos.

# 4.8 Status dos requisitos

| Status | Significado |
|---|---|
| Conceitual | Definido na documentação |
| Planejado | Previsto para futura implementação |
| Implementado | Implementado em ambiente real |
| Testado | Validado por execução |
| Não confirmado | Não há evidência suficiente |

### Status atual

Os requisitos deste documento encontram-se nos estados **Conceitual** ou **Planejado**.

Nenhum requisito deve ser classificado como **Implementado** ou **Testado**, pois não foi realizada uma implementação funcional no Microsoft Copilot Studio.

# 4.9 Limitações

A especificação não foi derivada de uma aplicação funcional. Portanto:

- os requisitos são uma proposta de projeto;
- os casos de teste são planejados;
- os critérios de aceitação são previstos;
- não existem métricas reais de desempenho;
- não existem resultados de execução.

## 4.10 Observação

Os requisitos foram elaborados com auxílio de Inteligência Artificial e submetidos a análise crítica. As decisões específicas do projeto foram diferenciadas das características dependentes da plataforma.

Este documento deve ser interpretado como uma **especificação conceitual** para fins de documentação técnica e estudo.

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado  
**Autora:** Nágyla Silva  

Projeto integrante do portfólio prático em Inteligência Artificial, desenvolvido para demonstrar competências em treinamento e avaliação de sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em experiência em QA e Auditoria.