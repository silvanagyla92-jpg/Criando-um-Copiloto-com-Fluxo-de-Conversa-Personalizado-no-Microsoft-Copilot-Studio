# Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado

> Projeto documental desenvolvido para o desafio **Criando um Copiloto com Fluxo de Conversa Personalizado no Microsoft Copilot Studio**, utilizando Inteligência Artificial como ferramenta de apoio à concepção, organização, análise crítica e documentação técnica.

## 1. Sobre o projeto

Este repositório apresenta uma documentação técnica conceitual para um cenário de **Assistente de Atendimento e Suporte**, inspirado no desafio da DIO sobre criação de um Copiloto com fluxo de conversa personalizado.

O objetivo desta entrega é demonstrar como ferramentas de Inteligência Artificial podem apoiar a criação de documentação técnica clara, estruturada, rastreável e verificável.

**Importante:** esta versão do repositório não deve ser interpretada como comprovação de uma implementação funcional própria no Microsoft Copilot Studio. A autora não possui acesso ao ambiente original utilizado no desafio. Por isso, configurações, testes e resultados específicos da plataforma são classificados como não confirmados quando não existe evidência correspondente.

## 2. Objetivos

### 2.1 Objetivo do projeto documental

- Documentar um cenário de agente conversacional com fluxo personalizado.
- Explicar sua arquitetura e seus caminhos conversacionais.
- Definir requisitos funcionais e não funcionais.
- Elaborar casos de teste planejados.
- Registrar os prompts utilizados no processo de documentação com IA.
- Separar fatos documentados, decisões de projeto, inferências e informações não confirmadas.
- Organizar referências técnicas oficiais.
- Estruturar evidências e diagramas sem fabricar comprovações de execução.

### 2.2 Relação com o desafio

O desafio propõe a documentação de um projeto utilizando ferramentas de Inteligência Artificial e solicita uma entrega organizada em um repositório GitHub, com seções e imagens.

Neste repositório, a parte documental foi estruturada mesmo sem acesso ao ambiente original. As imagens que seriam evidências de configuração ou execução são tratadas separadamente e não são inventadas.

## 3. Microsoft Copilot Studio

O Microsoft Copilot Studio é uma plataforma da Microsoft para criação e configuração de agentes conversacionais. A documentação oficial apresenta recursos relacionados a tópicos, gatilhos, orquestração, respostas generativas e fallback.

Neste projeto, esses conceitos são utilizados como referência técnica para a modelagem do cenário. A configuração exata de um agente no ambiente do desafio não é atribuída ao projeto sem evidência.

Consulte as [referências técnicas oficiais](./referencias/README.md) para os conceitos específicos utilizados na documentação.

## 4. Cenário documentado

O cenário conceitual utiliza um **Assistente de Atendimento e Suporte** com os seguintes caminhos:

- **Dúvidas** — perguntas e esclarecimentos dentro do escopo.
- **Suporte** — problemas ou dificuldades que exigem orientação.
- **Informações** — solicitações informativas relacionadas ao cenário.
- **Entrada ambígua** — solicitação de esclarecimentos antes do direcionamento.
- **Fora do escopo** — tratamento transparente de solicitações não relacionadas.
- **Continuidade** — possibilidade de iniciar uma nova solicitação.
- **Encerramento** — finalização da interação.

Esses caminhos são **decisões de projeto**, não configurações atribuídas automaticamente ao Microsoft Copilot Studio.

## 5. Tecnologias utilizadas

- **Microsoft Copilot / Inteligência Artificial** — apoio à concepção, redação, análise e revisão da documentação.
- **Microsoft Copilot Studio** — plataforma de referência do desafio e dos conceitos técnicos documentados.
- **Microsoft Learn** — fonte oficial para validação de conceitos do Copilot Studio.
- **GitHub** — hospedagem, versionamento e organização dos artefatos.
- **Markdown** — estruturação dos arquivos de documentação.

## 6. Estrutura do repositório

### 6.1 `docs/` — Documentação técnica

- [**Documentação técnica**](./docs/README.md) — índice geral da documentação.
- [**01 — Metodologia**](./docs/01-metodologia/README.md) — método, critérios de análise e validação.
- [**02 — Arquitetura**](./docs/02-arquitetura/README.md) — arquitetura conceitual do agente.
- [**03 — Fluxo conversacional**](./docs/03-fluxo-conversacional/README.md) — caminhos, entradas alternativas e continuidade.
- [**04 — Configuração**](./docs/04-configuracao/README.md) — conceitos e pontos de configuração da plataforma, sem afirmar configuração própria não comprovada.
- [**05 — Requisitos**](./docs/05-requisitos/README.md) — requisitos funcionais, não funcionais e rastreabilidade.
- [**06 — Testes**](./docs/06-testes/README.md) — casos de teste planejados e critérios de execução.
- [**07 — Resultados**](./docs/07-resultados/README.md) — resultados documentais atuais e limitações.

### 6.2 `prompts/` — Prompts utilizados

- [**Prompts e uso da IA**](./prompts/README.md) — prompts utilizados para cenário, arquitetura, fluxo, requisitos, testes, análise crítica e validação.

### 6.3 `diagramas/` — Diagramas

- [**Diagramas**](./diagramas/README.md) — arquitetura e fluxo conversacional em representação conceitual.

### 6.4 `evidencias/` — Evidências

- [**Evidências**](./evidencias/README.md) — classificação, limitações e critérios para evidências reais.
- [**01 — Criação do Copilot**](./evidencias/01-copilot/README.md) — espaço destinado a evidências reais da criação/configuração.
- [**02 — Fluxo**](./evidencias/02-fluxo/README.md) — espaço destinado a evidências reais do fluxo.
- [**03 — Resultados**](./evidencias/03-resultados/README.md) — espaço destinado a evidências reais dos testes e resultados.

### 6.5 `referencias/` — Referências técnicas

- [**Referências técnicas**](./referencias/README.md) — fontes oficiais e critérios de confiabilidade.

## 7. Metodologia de documentação com IA

A Inteligência Artificial foi utilizada como ferramenta de apoio, e não como substituta da validação humana.

O processo considera:

1. levantamento das informações disponíveis;
2. identificação de lacunas;
3. definição do cenário documental;
4. organização das informações em seções técnicas;
5. utilização de IA para sugestões e redação;
6. análise crítica das respostas geradas;
7. verificação de afirmações técnicas em fontes confiáveis;
8. separação entre fatos, decisões de projeto, inferências e informações não confirmadas;
9. organização de referências, diagramas e evidências;
10. auditoria de consistência do repositório.

## 8. Evidências e limitações

Atualmente, o repositório **não contém screenshots reais de uma implementação no Copilot Studio**.

Isso é intencional: imagens genéricas, imagens de terceiros ou diagramas conceituais não serão apresentados como evidência de execução.

Os testes em `docs/06-testes/` são planejados e não executados. Os diagramas em `diagramas/` são conceituais. A pasta `evidencias/` registra o que seria necessário comprovar em uma futura implementação.

## 9. Fontes técnicas oficiais

As informações específicas sobre o Microsoft Copilot Studio devem ser verificadas prioritariamente na documentação oficial da Microsoft.

- [Microsoft Copilot Studio — documentação oficial](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/)
- [Criar e editar tópicos](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-create-edit-topics)
- [Gatilhos de tópicos](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-triggers)
- [Tópico de fallback do sistema](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-system-fallback-topic)
- [Respostas generativas](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/faqs-generative-answers)

A lista organizada e contextualizada está em [Referências técnicas](./referencias/README.md).

## 10. Status do projeto

| Item | Status |
|---|---|
| Estrutura documental | Concluída nesta etapa |
| Metodologia | Documentada |
| Arquitetura conceitual | Documentada |
| Fluxo conversacional | Documentado |
| Configuração específica do Copilot Studio | Não confirmada |
| Requisitos | Documentados |
| Testes | Planejados, não executados |
| Resultados funcionais | Não disponíveis |
| Evidências visuais reais | Não disponíveis |
| Diagrama PNG | Ainda não disponível |
| Referências técnicas | Organizadas |
| Prompts utilizados | Documentados |

## 11. Contato

**Autor:** Nágyla Silva  
**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado  
**Desafio:** Criando um Copiloto com Fluxo de Conversa Personalizado no Microsoft Copilot Studio

**GitHub:** [`silvanagyla92-jpg`](https://github.com/silvanagyla92-jpg)

**LinkedIn:** [`Nágyla Silva`](https://www.linkedin.com/in/n%C3%A1gyla-silva-215aba35/)

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado

**Autora:** Nágyla Silva

Projeto integrante do portfólio prático em Inteligência Artificial,
desenvolvido para demonstrar competências em treinamento e avaliação de
sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às
funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em
experiência em QA e Auditoria.