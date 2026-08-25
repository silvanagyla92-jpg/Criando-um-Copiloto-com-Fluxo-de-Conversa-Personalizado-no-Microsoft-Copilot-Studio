# 02 — Arquitetura

## Visão conceitual

O projeto documentado utiliza o Microsoft Copilot Studio como plataforma de criação do agente conversacional. A arquitetura conceitual pode ser representada assim:

```text
Usuário
   │
   ▼
Entrada em linguagem natural
   │
   ▼
Agente no Copilot Studio
   │
   ├── Seleção/acionamento de tópico
   │       │
   │       ├── Pergunta
   │       ├── Condição
   │       ├── Mensagem
   │       └── Encerramento/redirecionamento
   │
   └── Fallback quando a intenção não é reconhecida
           │
           ▼
      Tratamento da entrada
```

## Tópicos

A documentação oficial define tópico como a estrutura que determina como uma conversa do agente progride. O Copilot Studio permite criar tópicos a partir do zero ou com apoio de IA. Os tipos de nós incluem pergunta, condição, ferramenta, mensagem, redirecionamento e encerramento. [Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-create-edit-topics)

## Acionamento

Os tópicos podem ser acionados por consulta do usuário ou por redirecionamento. Em orquestração clássica, frases de gatilho são usadas para associar a entrada a uma intenção; em orquestração generativa, o agente pode selecionar o tópico considerando seu nome e descrição. [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/triggering-topics)

## Fallback

O tópico Fallback trata entradas que não são reconhecidas. A Microsoft documenta que ele pode ser personalizado e que pode utilizar a entrada não reconhecida para integração com outros componentes. [Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-system-fallback-topic)

## Limite da documentação

Este diagrama é uma representação conceitual baseada na documentação oficial. Ele não afirma que todos os componentes apresentados foram configurados no projeto original. As configurações efetivamente realizadas devem ser comprovadas pelas evidências em `evidencias/`.
