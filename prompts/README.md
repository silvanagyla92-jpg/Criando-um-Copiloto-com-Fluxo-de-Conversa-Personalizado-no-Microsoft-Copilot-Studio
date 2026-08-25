# Prompts e Uso da Inteligência Artificial

## 1. Objetivo

Esta pasta registra os prompts utilizados como apoio à elaboração da documentação técnica do projeto **Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado**.

O registro demonstra como a Inteligência Artificial foi utilizada para apoiar a estruturação, análise e revisão do conteúdo, mantendo separadas a geração de conteúdo, a análise crítica e a validação das informações.

---

## 2. Ferramenta utilizada

A ferramenta utilizada como apoio foi o **Microsoft Copilot**.

A IA foi utilizada para apoiar:

- estruturação do cenário;
- definição do fluxo conversacional;
- elaboração de requisitos;
- criação de casos de teste planejados;
- organização da documentação;
- revisão conceitual;
- identificação de informações que precisam de validação.

---

## 3. Prompt 01 — Definição do cenário

```text
Projete um cenário conceitual para um agente conversacional chamado
"Assistente de Atendimento e Suporte".

O cenário deve possuir três caminhos principais:
1. Dúvidas;
2. Suporte;
3. Informações.

Inclua também tratamento para entradas fora do escopo, continuidade da
conversa e encerramento.

Diferencie claramente decisões de projeto, fatos técnicos e informações que
dependam de implementação em uma plataforma específica.
```

**Finalidade:** definir o cenário-base utilizado na arquitetura e no fluxo conversacional.

---

## 4. Prompt 02 — Especificação técnica

```text
Elabore uma especificação técnica para o cenário de um Assistente de
Atendimento e Suporte.

Inclua:
- visão geral;
- objetivo;
- escopo;
- público-alvo;
- requisitos funcionais;
- requisitos não funcionais;
- componentes conceituais;
- tópicos conversacionais;
- fluxo principal;
- fluxos alternativos;
- tratamento de entradas fora do escopo;
- uso conceitual de IA generativa;
- arquitetura conceitual;
- exemplos de diálogo;
- critérios de teste;
- resultados esperados;
- limitações.

Não apresente como implementadas funcionalidades que não tenham sido
executadas ou verificadas.
```

**Finalidade:** gerar uma primeira estrutura de documentação posteriormente analisada e reorganizada.

---

## 5. Prompt 03 — Arquitetura

```text
Projete uma arquitetura conceitual para um agente conversacional de
atendimento e suporte.

Mostre a relação entre:
- usuário;
- interface de interação;
- agente conversacional;
- identificação da necessidade;
- Dúvidas;
- Suporte;
- Informações;
- entrada ambígua;
- tratamento fora do escopo;
- resposta;
- continuidade;
- encerramento.

Deixe explícito que se trata de uma arquitetura conceitual e não de uma
configuração comprovada no Microsoft Copilot Studio.
```

**Finalidade:** apoiar `docs/02-arquitetura/` e o diagrama de arquitetura conceitual.

---

## 6. Prompt 04 — Fluxo conversacional

```text
Transforme o cenário do Assistente de Atendimento e Suporte em um fluxo
conversacional detalhado.

Inclua:
- saudação;
- identificação da necessidade;
- Dúvidas;
- Suporte;
- Informações;
- entrada ambígua;
- solicitação de esclarecimento;
- fora do escopo;
- continuidade;
- encerramento;
- exemplos de diálogos;
- fluxos alternativos.

Crie também casos de teste planejados para validar esses comportamentos em
uma futura implementação.
```

**Finalidade:** apoiar `docs/03-fluxo-conversacional/` e a definição inicial dos casos CT-01 a CT-08.

---

## 7. Prompt 05 — Requisitos

```text
Converta o cenário conversacional em requisitos funcionais e não funcionais.

Use identificadores RF-01, RF-02 etc. para requisitos funcionais e RNF-01,
RNF-02 etc. para requisitos não funcionais.

Depois crie uma matriz de rastreabilidade relacionando requisitos, fluxos e
casos de teste.

Não classifique como implementado ou testado aquilo que não tenha sido
executado em ambiente real.
```

**Finalidade:** apoiar `docs/05-requisitos/` e sua matriz de rastreabilidade.

---

## 8. Prompt 06 — Testes

```text
Crie um plano de testes para o fluxo conversacional descrito.

Para cada teste informe:
- ID;
- objetivo;
- entrada;
- resultado esperado;
- status.

Inclua cenários de saudação, dúvidas, suporte, informações, fora do escopo,
entrada ambígua, continuidade e encerramento.

Como não existe implementação funcional disponível, marque os testes como
"Planejado — não executado" e não invente resultados ou evidências.
```

**Finalidade:** apoiar `docs/06-testes/` sem transformar resultados esperados em resultados reais.

---

## 9. Prompt 07 — Análise crítica

```text
Analise criticamente a especificação produzida.

Separe:
- fatos que precisam de fonte;
- decisões de projeto;
- inferências;
- informações não confirmadas;
- funcionalidades que dependem de implementação no Microsoft Copilot Studio.

Identifique também afirmações que não devem ser apresentadas como resultado
real porque não foram testadas.
```

**Finalidade:** reduzir o risco de apresentar conteúdo gerado pela IA como fato confirmado.

---

## 10. Prompt 08 — Validação de fontes

```text
Para cada afirmação técnica sobre Microsoft Copilot Studio, priorize
informações da documentação oficial da Microsoft Learn.

Diferencie fatos documentados de decisões de projeto, inferências e
informações não confirmadas.

Não apresente como fato uma configuração específica que não esteja
comprovada.
```

**Finalidade:** apoiar a rastreabilidade e a confiabilidade das afirmações técnicas.

---

## 11. Prompt 09 — Melhoria da documentação

```text
Revise a documentação técnica para melhorar:
- clareza;
- organização;
- consistência terminológica;
- rastreabilidade;
- distinção entre conceito e implementação;
- identificação de limitações;
- qualidade dos casos de teste.

Não remova informações válidas sem justificar a alteração.
```

**Finalidade:** apoiar a revisão e padronização dos documentos do projeto.

---

## 12. Processo de validação

Os prompts não são tratados como fontes técnicas.

A saída produzida pela IA foi considerada **material de apoio** e passou por análise crítica.

Quando uma afirmação depende de uma funcionalidade específica do Microsoft Copilot Studio, ela deve ser confirmada na documentação oficial da Microsoft antes de ser apresentada como fato técnico.

---

## 13. Limitações

O projeto não possui acesso ao ambiente original do Microsoft Copilot Studio utilizado no desafio.

Por esse motivo, os prompts deste documento não são evidência de que o agente tenha sido implementado e não comprovam que os fluxos tenham sido executados com sucesso.

---

## 14. Rastreabilidade

| Prompt | Resultado relacionado |
|---|---|
| Prompt 01 | Definição do cenário |
| Prompt 02 | Especificação técnica |
| Prompt 03 | `docs/02-arquitetura/` e diagrama de arquitetura |
| Prompt 04 | `docs/03-fluxo-conversacional/` e diagrama de fluxo |
| Prompt 05 | `docs/05-requisitos/` |
| Prompt 06 | `docs/06-testes/` |
| Prompt 07 | Análise crítica transversal |
| Prompt 08 | Validação das afirmações técnicas |
| Prompt 09 | Padronização da documentação |

---

## 15. Observação sobre autoria

Os prompts foram utilizados como instrumentos de apoio. A organização final,
seleção, revisão crítica, classificação das informações e decisão sobre o que
seria incorporado à documentação fazem parte do processo de elaboração do
projeto.

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado

**Autora:** Nágyla Silva

Projeto integrante do portfólio prático em Inteligência Artificial,
desenvolvido para demonstrar competências em treinamento e avaliação de
sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às
funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em
experiência em QA e Auditoria.