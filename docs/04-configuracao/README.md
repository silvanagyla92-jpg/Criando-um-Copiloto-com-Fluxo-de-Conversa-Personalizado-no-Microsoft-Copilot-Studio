# 04 — Configuração

## 1. Escopo

Esta seção descreve conceitos e pontos de configuração relacionados ao desafio e ao cenário documentado.

O conteúdo organiza tecnicamente os elementos que compõem a solução proposta.

## 2. Criação do agente

O Microsoft Copilot Studio fornece recursos para criação e configuração de agentes conversacionais. A documentação oficial reúne orientações sobre criação, teste, publicação, tópicos, conhecimento e ferramentas.

[Microsoft Learn — Microsoft Copilot Studio](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/)

## 3. Criação de tópicos

Os tópicos organizam partes específicas da conversa. A documentação oficial descreve recursos para criar e editar tópicos, incluindo a criação de tópicos a partir de modelos ou de uma estrutura vazia.

[Microsoft Learn — Criar e editar tópicos](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-create-edit-topics)

## 4. Gatilhos

Os gatilhos determinam condições pelas quais um tópico pode ser acionado. Os mecanismos disponíveis dependem da configuração de orquestração e do tipo de evento utilizado.

[Microsoft Learn — Gatilhos de tópicos](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers)

## 5. Mensagens de erro e fallback

O tópico de fallback pode tratar situações nas quais a entrada do usuário não resulta em um encaminhamento adequado. A documentação da Microsoft também descreve a variável `UnrecognizedTriggerPhrase` para representar uma entrada não reconhecida.

[Microsoft Learn — Tópico de fallback do sistema](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-system-fallback-topic)

## 6. IA generativa

O Copilot Studio oferece recursos de orquestração generativa. Esses recursos podem permitir que o agente selecione tópicos, ferramentas e conhecimento de acordo com a solicitação e as descrições disponíveis.

[Microsoft Learn — Ações generativas](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions)

## 7. Aplicação ao cenário documentado

No cenário deste projeto, os conceitos são organizados da seguinte forma:

| Elemento | Aplicação conceitual |
|---|---|
| Agente | Assistente de Atendimento e Suporte |
| Tópicos | Dúvidas, Suporte, Informações e encerramento |
| Gatilhos | Entradas que direcionam a conversa |
| Fallback | Tratamento de entradas não reconhecidas ou fora do fluxo esperado |
| IA generativa | Apoio à produção de respostas quando aplicável |

## 8. Relação com os demais documentos

- [Arquitetura](../02-arquitetura/README.md)
- [Fluxo conversacional](../03-fluxo-conversacional/README.md)
- [Requisitos](../05-requisitos/README.md)
- [Testes](../06-testes/README.md)
- [Resultados](../07-resultados/README.md)

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado

**Autora:** Nágyla Silva

Projeto integrante do portfólio prático em Inteligência Artificial,
desenvolvido para demonstrar competências em treinamento e avaliação de
sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às
funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em
experiência em QA e Auditoria.