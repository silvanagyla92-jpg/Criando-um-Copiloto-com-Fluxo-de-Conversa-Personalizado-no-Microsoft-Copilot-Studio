# 1. Metodologia

## 1.1 Objetivo

Esta etapa apresenta a metodologia utilizada para elaborar a documentação técnica do projeto **Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado**.

O trabalho utiliza Inteligência Artificial como ferramenta de apoio à concepção, estruturação, revisão e documentação do projeto.

A ferramenta utilizada para apoio à elaboração do conteúdo foi o **Microsoft Copilot**. As informações técnicas relacionadas ao Microsoft Copilot Studio são verificadas, quando aplicável, por meio da documentação oficial da Microsoft.

## 1.2 Ferramenta de Inteligência Artificial utilizada

### Microsoft Copilot

O Microsoft Copilot foi utilizado como ferramenta de apoio para:

- estruturar a especificação técnica;
- propor um cenário conversacional;
- organizar requisitos;
- elaborar fluxos conversacionais;
- sugerir critérios de teste;
- identificar possíveis limitações;
- revisar a estrutura da documentação;
- apoiar a elaboração de diagramas conceituais.

A utilização da IA não substituiu a análise crítica humana. As respostas produzidas pela ferramenta foram analisadas antes de serem incorporadas à documentação.

## 1.3 Processo de elaboração

### Etapa 1 — Definição do cenário

Foi definido o cenário conceitual de um agente denominado **Assistente de Atendimento e Suporte**.

O agente foi projetado para trabalhar com três caminhos principais:

- Dúvidas;
- Suporte;
- Informações.

Também foi previsto o tratamento de solicitações fora do escopo.

### Etapa 2 — Geração inicial com IA

O Microsoft Copilot recebeu instruções para produzir uma especificação técnica do projeto.

A solicitação incluiu requisitos para que a IA:

- diferenciasse fatos de decisões de projeto;
- não inventasse configurações;
- identificasse informações que dependessem do Microsoft Copilot Studio;
- apontasse informações que precisariam ser verificadas.

### Etapa 3 — Análise crítica

A resposta produzida pela IA foi analisada criticamente. Durante essa análise foram identificados:

- simplificações conceituais;
- terminologia que precisava ser refinada;
- informações dependentes da configuração do Copilot Studio;
- necessidade de diferenciar projeto conceitual de implementação real;
- necessidade de classificar resultados como esperados ou efetivamente testados.

### Etapa 4 — Validação das informações

As informações técnicas relacionadas ao Microsoft Copilot Studio são comparadas, quando aplicável, com a documentação oficial da Microsoft.

A validação busca evitar:

- informações desatualizadas;
- afirmações sem evidência;
- funcionalidades atribuídas incorretamente à plataforma;
- resultados apresentados como comprovados sem execução real.

### Etapa 5 — Documentação

Após a análise e validação, o conteúdo aprovado é organizado no GitHub em documentação, diagramas, evidências, prompts, testes e referências.

## 1.4 Classificação das informações

Para aumentar a rastreabilidade, as informações são classificadas em quatro categorias:

### Fato confirmado

Informação sustentada por documentação oficial ou evidência disponível.

### Decisão de projeto

Elemento definido especificamente para este projeto conceitual.

### Inferência

Conclusão derivada de informações disponíveis, mas que não constitui comprovação de uma implementação específica.

### Não confirmado

Informação que não pode ser comprovada devido à ausência de documentação original ou de acesso ao ambiente de implementação.

## 1.5 Limitações

A autora não possui acesso ao ambiente original do Microsoft Copilot Studio utilizado no projeto apresentado no desafio. Também não está disponível a documentação original da implementação.

Por esse motivo:

- não são apresentadas configurações específicas como comprovadas;
- não são apresentados resultados de execução como resultados reais;
- não são utilizadas capturas de tela de ambientes que não foram acessados;
- os fluxos apresentados são conceituais;
- os testes apresentados são casos de teste planejados.

## 1.6 Transparência sobre o uso de IA

A Inteligência Artificial foi utilizada como ferramenta de apoio e não como fonte única de validação.

As respostas geradas pelo Microsoft Copilot foram submetidas a análise crítica. Quando uma afirmação dependia de funcionalidades específicas do Microsoft Copilot Studio, a informação foi tratada como dependente de validação.

Essa abordagem busca preservar a rastreabilidade e reduzir o risco de incorporação de informações incorretas ou não comprovadas.

## 1.7 Resultado da metodologia

A metodologia resultou em uma documentação estruturada do projeto conceitual, incluindo:

- especificação técnica;
- requisitos;
- arquitetura conceitual;
- fluxo conversacional;
- fluxos alternativos;
- critérios de teste;
- limitações;
- registro do uso de Inteligência Artificial.

O projeto não deve ser interpretado como comprovação de uma implementação funcional no Microsoft Copilot Studio.

---

**Projeto:** Documentação Técnica de um Copiloto com Fluxo de Conversa Personalizado  
**Autora:** Nágyla Silva  

Projeto integrante do portfólio prático em Inteligência Artificial, desenvolvido para demonstrar competências em treinamento e avaliação de sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em experiência em QA e Auditoria.