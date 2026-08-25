# 03 — Fluxo conversacional

## Conceito

No Copilot Studio, um tópico define como a conversa do agente avança. Um tópico pode conter diferentes nós para coletar informações, aplicar condições, enviar mensagens, chamar ferramentas, redirecionar a conversa ou encerrá-la. [Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-create-edit-topics)

## Fluxo conceitual

```text
Entrada do usuário
       │
       ▼
Reconhecimento/seleção do tópico
       │
       ▼
Nó inicial do tópico
       │
       ├── Pergunta → coleta informação
       │                  │
       │                  ▼
       │               Condição
       │                /      \
       │              sim       não
       │              │          │
       │              ▼          ▼
       │          Mensagem    Novo caminho
       │
       └──────────────► Encerramento ou redirecionamento
```

## Frases de gatilho

Em orquestração clássica, frases de gatilho ajudam o agente a reconhecer a intenção associada a um tópico. A Microsoft recomenda frases suficientemente distintas e orientadas à intenção do usuário. [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/cux-queries)

## Fallback

Quando a entrada não corresponde adequadamente a um tópico, o sistema pode usar o tópico Fallback. A documentação oficial informa que o Fallback é acionado quando o agente não entende a entrada ou não possui confiança suficiente para acionar um tópico existente. [Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/guidance/fallback-topic)

## Relação com o projeto

O README original informa que o desafio envolveu a criação de um Copilot em branco, a customização de um tópico, a personalização de mensagem de erro e o ajuste da qualidade das respostas com GenAI. Essas afirmações são tratadas como descrição do projeto e devem ser complementadas por evidências visuais na entrega final.
