# Diagramas

Esta pasta reúne os diagramas utilizados para explicar visualmente a solução proposta no projeto **Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado**.

## 1. Objetivo

Os diagramas têm a finalidade de facilitar a compreensão da arquitetura e do fluxo conversacional.

Eles representam **decisões e modelos conceituais deste projeto**. Não devem ser interpretados como capturas da configuração real do Microsoft Copilot Studio.

---

## 2. Diagrama de arquitetura conceitual

O diagrama de arquitetura deve representar, em alto nível, a relação entre:

```text
Usuário
   │
   ▼
Interface de interação
   │
   ▼
Agente conversacional
   │
   ▼
Identificação da necessidade
   │
   ├───────────────┬────────────────┬──────────────────┐
   ▼               ▼                ▼                  ▼
Dúvidas         Suporte        Informações       Fora do escopo
   │               │                │                  │
   └───────────────┴────────────────┴──────────────────┘
                           │
                           ▼
                       Resposta
                           │
                    ┌──────┴──────┐
                    ▼             ▼
              Continuar       Encerrar
```

### Interpretação

- **Usuário:** inicia a interação e fornece a solicitação.
- **Interface:** representa o ponto de entrada e saída da conversa.
- **Agente conversacional:** recebe e processa a solicitação segundo o cenário definido.
- **Identificação da necessidade:** determina o caminho conceitual da conversa.
- **Dúvidas:** trata perguntas e esclarecimentos.
- **Suporte:** trata problemas e solicitações de assistência.
- **Informações:** trata solicitações informativas dentro do escopo.
- **Fora do escopo:** trata solicitações que não pertencem à finalidade definida.
- **Resposta:** apresenta a orientação correspondente.
- **Continuar:** permite uma nova solicitação.
- **Encerrar:** finaliza a interação.

---

## 3. Diagrama do fluxo conversacional

O fluxo principal é representado conceitualmente por:

```text
[Início]
    │
    ▼
[Saudação]
    │
    ▼
[Identificar necessidade]
    │
    ├──► [Dúvidas] ───────┐
    │                     │
    ├──► [Suporte] ───────┤
    │                     │
    ├──► [Informações] ───┤
    │                     │
    ├──► [Ambígua] ──► [Solicitar esclarecimento]
    │                     │
    └──► [Fora do escopo] ┘
                          │
                          ▼
                       [Resposta]
                          │
                   ┌──────┴──────┐
                   ▼             ▼
              [Continuar]    [Encerrar]
                   │
                   └──────► [Nova solicitação]
```

### Fluxos alternativos

1. **Entrada ambígua:** o agente solicita esclarecimentos antes de escolher um caminho.
2. **Fora do escopo:** o agente informa sua limitação e orienta o usuário sobre os caminhos disponíveis.
3. **Continuidade:** o usuário apresenta uma nova solicitação e o fluxo retorna à identificação da necessidade.
4. **Encerramento:** o usuário sinaliza que não deseja continuar e a interação é finalizada.

---

## 4. Relação com a documentação

| Diagrama | Documento relacionado |
|---|---|
| Arquitetura conceitual | `../docs/02-arquitetura/README.md` |
| Fluxo conversacional | `../docs/03-fluxo-conversacional/README.md` |
| Requisitos | `../docs/04-requisitos/README.md` |
| Testes | `../docs/05-testes/README.md` |

---

## 5. Status dos diagramas

| Item | Status |
|---|---|
| Arquitetura conceitual | Documentada |
| Fluxo conversacional | Documentado |
| Diagrama PNG da arquitetura | Não disponível |
| Diagrama PNG do fluxo | Não disponível |
| Captura do Copilot Studio | Não disponível |

Os diagramas textuais acima são representações conceituais. Ainda não há arquivos PNG reais no repositório.

---

## 6. Evidência e transparência

Um diagrama produzido para explicar o projeto não constitui evidência de que a configuração tenha sido realizada no Microsoft Copilot Studio.

Caso futuramente sejam produzidos arquivos PNG, eles deverão ser identificados como **diagramas conceituais do projeto**, salvo quando houver uma captura real de uma implementação, que deverá ser identificada separadamente como evidência.

Não serão utilizados screenshots simulados ou imagens de terceiros apresentadas como se fossem da implementação deste projeto.

---

## 7. Referências técnicas

Para afirmações sobre recursos específicos do Microsoft Copilot Studio, deve-se priorizar a documentação oficial da Microsoft Learn.

- [Criar e editar tópicos — Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-create-edit-topics)
- [Gatilhos de tópicos — Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/triggering-topics)
- [Tópico de fallback do sistema — Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-system-fallback-topic)

Essas referências servem para validar conceitos da plataforma; não constituem evidência de implementação deste projeto.

---

## 8. Limitações

A autora não possui acesso ao ambiente original do Copilot Studio utilizado no desafio. Por isso, a documentação não afirma que os fluxos descritos tenham sido configurados ou executados na plataforma.

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado

**Autora:** Nágyla Silva

Projeto integrante do portfólio prático em Inteligência Artificial,
desenvolvido para demonstrar competências em treinamento e avaliação de
sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às
funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em
experiência em QA e Auditoria.