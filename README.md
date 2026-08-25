# Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado

> Projeto desenvolvido com **Microsoft Copilot Studio** e documentado com apoio de ferramentas de Inteligência Artificial, com foco em documentação técnica clara, organizada, verificável e visual.

## 1. Sobre o projeto

Este repositório apresenta a documentação técnica do projeto **Criando um Copiloto com Fluxo de Conversa Personalizado no Microsoft Copilot Studio**, realizado no contexto do desafio da DIO.

O objetivo desta entrega é demonstrar como ferramentas de Inteligência Artificial podem apoiar a análise, organização, revisão e aprimoramento da documentação de um projeto de IA conversacional.

A documentação diferencia informações comprovadas sobre o projeto de explicações técnicas baseadas em documentação oficial. Configurações específicas do Copilot devem ser confirmadas pelas evidências visuais disponíveis no repositório.

## 2. Objetivos

### 2.1 Objetivo do projeto original

Documentar a criação de um Copilot com fluxo de conversa personalizado, contemplando a criação do agente, configuração de tópicos, tratamento de situações de fallback e utilização de recursos de IA generativa, conforme o escopo registrado no desafio original.

### 2.2 Objetivo desta documentação

- Organizar as informações técnicas do projeto.
- Explicar a arquitetura e o fluxo conversacional.
- Registrar a metodologia utilizada.
- Documentar os prompts empregados no processo de documentação.
- Separar fatos, inferências e informações que dependem de evidências.
- Disponibilizar referências oficiais para conceitos do Microsoft Copilot Studio.
- Reunir evidências e diagramas em uma estrutura de fácil navegação.

## 3. Microsoft Copilot Studio

O Microsoft Copilot Studio é uma plataforma da Microsoft para criação e configuração de agentes e experiências conversacionais com recursos de IA. A documentação oficial apresenta recursos relacionados a tópicos, gatilhos, orquestração, respostas generativas e tópicos de fallback.

Os tópicos podem ser acionados de diferentes maneiras. Em agentes com orquestração generativa, o gatilho padrão pode ser **O agente escolhe**; em cenários de orquestração clássica, pode ser utilizado **O usuário diz uma frase**, com frases de gatilho configuradas para o tópico. citeturn0search2turn0search3

O tópico de fallback pode ser utilizado quando o agente não consegue determinar a intenção do usuário com confiança suficiente para acionar um tópico existente, permitindo personalizar o comportamento para entradas não reconhecidas. citeturn0search0turn0search4

O Copilot Studio também oferece respostas generativas, que podem utilizar fontes de conhecimento para produzir respostas quando os tópicos configurados não atendem à consulta. citeturn0search1turn0search10

## 4. O que foi desenvolvido no desafio

Com base no registro original do projeto, foram trabalhados os seguintes pontos:

### 4.1 Criação de um Copilot em branco

Criação inicial de um agente conversacional a partir de uma configuração em branco, permitindo estruturar a solução de acordo com o objetivo do exercício.

### 4.2 Personalização de tópico

Configuração de um tópico para organizar o fluxo de conversa. No Copilot Studio, tópicos representam unidades de comportamento conversacional e podem utilizar gatilhos e diferentes nós para conduzir a interação. citeturn0search11turn0search2

### 4.3 Tratamento de entradas não reconhecidas

Configuração de comportamento relacionado a mensagens de erro ou fallback. O fallback é utilizado para lidar com situações em que a entrada do usuário não corresponde adequadamente aos tópicos disponíveis. citeturn0search0turn0search4

### 4.4 Utilização de IA generativa

Exploração de recursos de IA generativa para respostas conversacionais. A documentação oficial diferencia respostas generativas e outras configurações de IA generativa, incluindo fontes de conhecimento e instruções personalizadas. citeturn0search1turn0search9

> **Critério de evidência:** os detalhes específicos da configuração realizada no ambiente original não são inferidos apenas a partir da documentação do produto. Eles devem ser comprovados pelas capturas de tela e demais evidências do projeto.

## 5. Tecnologias e recursos utilizados

- **Microsoft Copilot Studio** — criação e configuração do agente.
- **Inteligência Artificial Generativa (GenAI)** — recursos de geração e apoio à interação conversacional.
- **Microsoft Learn** — fonte oficial utilizada para validação dos conceitos técnicos.
- **GitHub** — hospedagem, versionamento e organização da documentação.
- **Markdown** — estruturação dos arquivos de documentação.

## 6. Estrutura do repositório

A documentação foi organizada em pastas para separar metodologia, arquitetura, fluxo conversacional, configuração, resultados, prompts, diagramas e evidências.

### 6.1 `docs/` — Documentação técnica

Concentra a documentação principal do projeto e funciona como índice para os conteúdos técnicos.

- [**Documentação técnica**](./docs/README.md) — visão geral e navegação da documentação.
- [**01 — Metodologia**](./docs/01-metodologia/README.md) — método utilizado, critérios de análise, confiabilidade e validação.
- [**02 — Arquitetura**](./docs/02-arquitetura/README.md) — arquitetura conceitual e relação entre usuário, Copilot, tópicos, fluxo e respostas.
- [**03 — Fluxo conversacional**](./docs/03-fluxo-conversacional/README.md) — tópicos, gatilhos, caminhos de conversa e fallback.
- [**04 — Configuração**](./docs/04-configuracao/README.md) — orientações e informações relacionadas à configuração do Copilot.
- [**05 — Resultados**](./docs/05-resultados/README.md) — resultados, interpretação e critérios de validação.

### 6.2 `prompts/` — Prompts utilizados

Reúne os prompts e orientações utilizados para apoiar a análise e a produção da documentação com Inteligência Artificial.

- [**Prompts utilizados**](./prompts/README.md) — análise, estruturação, revisão crítica e validação.

### 6.3 `diagramas/` — Representações visuais

Destinada aos diagramas utilizados para representar a arquitetura e o fluxo conversacional do projeto.

- [**Diagramas**](./diagramas/README.md) — orientações e documentação dos diagramas.

### 6.4 `evidencias/` — Evidências do projeto

Reúne as evidências visuais que deverão comprovar as configurações e os resultados efetivamente observados no Microsoft Copilot Studio.

- [**01 — Criação do Copilot**](./evidencias/01-copilot/README.md) — evidências da criação e configuração inicial.
- [**02 — Fluxo**](./evidencias/02-fluxo/README.md) — evidências do tópico, gatilhos, fluxo e tratamento de erro.
- [**03 — Resultados**](./evidencias/03-resultados/README.md) — evidências dos testes e resultados observados.

> **Importante:** as evidências visuais devem ser capturas reais do projeto. Imagens genéricas ou capturas de outros projetos não devem ser apresentadas como comprovação da implementação.

## 7. Metodologia de documentação com IA

A Inteligência Artificial foi utilizada como ferramenta de apoio, e não como substituta da validação humana.

O processo documental considera as seguintes etapas:

1. Levantamento das informações existentes.
2. Identificação de lacunas na documentação.
3. Organização das informações em seções técnicas.
4. Utilização de IA para sugestões de estrutura e redação.
5. Verificação das afirmações técnicas em fontes confiáveis.
6. Separação entre informações confirmadas e inferências.
7. Revisão crítica do conteúdo gerado.
8. Organização das evidências e referências.
9. Revisão final da consistência dos documentos.

## 8. Fontes técnicas oficiais

As informações técnicas sobre o Microsoft Copilot Studio foram verificadas prioritariamente na documentação oficial da Microsoft:

- [Microsoft Copilot Studio — documentação oficial](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/)
- [Criar e editar tópicos](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-create-edit-topics?tabs=webApp)
- [Definir gatilhos de tópicos](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-triggers)
- [Disparar tópicos](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/guidance/triggering-topics)
- [Criar frases de gatilho eficazes](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/guidance/trigger-phrases-best-practices)
- [Usar o tópico de fallback](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/guidance/fallback-topic)
- [Configurar o tópico de fallback do sistema](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/authoring-system-fallback-topic)
- [Perguntas frequentes para respostas generativas](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/faqs-generative-answers)
- [Otimizar prompts e configuração de tópicos](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/guidance/optimize-prompts-topic-configuration)

## 9. Status da documentação

**Situação atual:** documentação estruturada e organizada, com áreas específicas reservadas para evidências visuais e diagramas.

Antes da entrega final, recomenda-se verificar:

- se todas as capturas reais do projeto foram adicionadas;
- se os diagramas representam fielmente a implementação;
- se os links internos continuam funcionando;
- se as configurações descritas correspondem ao ambiente utilizado;
- se não existem afirmações técnicas sem fonte ou evidência;
- se a documentação está consistente com o projeto original.

## 10. Contato

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