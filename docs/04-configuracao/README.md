# 04 — Configuração

## Escopo

Esta seção descreve conceitos e pontos de configuração relacionados ao desafio. Ela não substitui evidências do ambiente original.

## Criação do agente

O Microsoft Copilot Studio fornece recursos para criar agentes e fluxos de trabalho. A documentação oficial reúne orientações de criação, teste, publicação, tópicos, conhecimento e ferramentas. [Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/)

## Criação de tópico

Um tópico pode ser criado a partir de um modelo vazio. A documentação atual descreve o uso da página de tópicos, a opção de adicionar um tópico e a criação a partir do zero. [Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-create-edit-topics)

## Gatilhos

Os tipos de gatilho variam conforme a configuração de orquestração. Entre eles estão `The agent chooses`, `User says a phrase`, recebimento de mensagem e eventos relacionados à execução. [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers)

## Mensagens de erro e Fallback

O tópico de Fallback pode ser personalizado para tratar entradas que não acionam adequadamente um tópico. A Microsoft também documenta o uso da variável `UnrecognizedTriggerPhrase` para armazenar a entrada não reconhecida. [Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-system-fallback-topic)

## IA generativa

O Copilot Studio possui recursos de orquestração generativa. Na orquestração generativa, o agente pode selecionar tópicos, ferramentas e conhecimento com base na solicitação e nas descrições disponíveis. [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions)

## O que deve ser comprovado

Para afirmar exatamente quais opções foram selecionadas no projeto original, devem ser adicionadas capturas de tela reais em `evidencias/`. Não são atribuídas ao projeto configurações que não estejam comprovadas.
