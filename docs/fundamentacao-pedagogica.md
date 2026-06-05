# Fundamentacao Pedagogica

Este documento resume as estrategias de aprendizagem baseadas em evidencia que guiam o design do aplicativo de ensino de Probabilidade B.

---

## 1. Pratica de Teste (Practice Testing)

**Fonte:** Dunlosky et al. (2013); Roediger & Karpicke (2006)

**Principio:** Recuperar informacao da memoria via testes e quizzes e significativamente mais eficaz do que reler ou destacar texto. Cada tentativa de recuperacao fortalece os caminhos neurais associados a memoria.

**Implementacao no app:**
- Modo de autoavaliacao com exercicios apresentados sem solucao visivel
- Estagio explicito de "tente resolver" antes de revelar qualquer passo da solucao
- Registro de autoavaliacao (acertei / errei / parcial) que alimenta o sistema de revisao espacada

**Evidencia:** Roediger & Karpicke (2006) demonstraram que estudantes que fizeram testes de pratica retiveram 80% do material apos uma semana, contra 36% dos que apenas releram.

---

## 2. Pratica Espacada (Distributed Practice)

**Fonte:** Dunlosky et al. (2013); Bjork & Bjork (2011)

**Principio:** Revisar conteudo em intervalos crescentes ao longo do tempo combate diretamente a curva de esquecimento de Ebbinghaus. O momento ideal de revisao e logo antes de esquecer, fortalecendo a consolidacao na memoria de longo prazo.

**Implementacao no app:**
- Sistema de repeticao espacada ativa baseado em data de ultimo acesso e resultado de autoavaliacao
- Notificacoes de revisao que sugerem topicos a revisar
- Algoritmo baseado no modelo SM-2 simplificado

---

## 3. Pratica Intercalada (Interleaved Practice)

**Fonte:** Dunlosky et al. (2013); Bjork & Bjork (2011)

**Principio:** Misturar tipos de problemas diferentes em uma sessao de estudo, em vez de resolver blocos de um unico tipo, leva a compreensao conceitual mais profunda e melhor capacidade de resolver problemas novos. O custo e que a pratica "parece" mais dificil no momento (dificuldade desejavel).

**Implementacao no app:**
- Modo "simulado" que gera conjuntos de exercicios misturados de diferentes topicos
- Filtros que permitem escolher entre pratica bloqueada (um topico) e intercalada (multiplos topicos)

---

## 4. Efeito do Exemplo Trabalhado (Worked Example Effect)

**Fonte:** Sweller, Ayres & Kalyuga (2011) -- Cognitive Load Theory

**Principio:** Em dominios de alta complexidade procedural (como manipulacao de integrais e transformacoes), estudar solucoes completas e estruturadas reduz a carga cognitiva extrinseca. A revelacao progressiva permite que o estudante processe cada etapa antes de avancar.

**Implementacao no app:**
- Resolucoes completas estruturadas em passos ordenados
- Revelacao progressiva: o estudante revela passo a passo ou de uma vez, por escolha explicita
- Cada passo com titulo descritivo e corpo com explicacao detalhada

---

## 5. Codificacao Dupla (Dual Coding)

**Fonte:** Paivio (1986); Weinstein, Sumeracki & Caviglioli (2019)

**Principio:** Combinar representacao verbal (texto e formula) com representacao visual (grafico e diagrama) ativa dois canais de processamento distintos, reduzindo a sobrecarga cognitiva e fortalecendo a retencao.

**Implementacao no app:**
- Visualizadores interativos parametricos acoplados a cada modelo continuo
- Graficos da fdp e fda com controles de parametros em tempo real
- Visualizadores de transformacoes que mostram visualmente como uma fdp se mapeia em outra

---

## 6. Exemplos Concretos (Concrete Examples)

**Fonte:** The Learning Scientists (2019); Weinstein et al. (2019)

**Principio:** Usar aplicacoes do mundo real para ancorar conceitos abstratos. Quando um estudante ve que a distribuicao exponencial modela o tempo de vida de um HD, o conceito ganha significado e ancoragem na experiencia. Esta estrategia e especialmente importante em matematica e estatistica.

**Implementacao no app:**
- Cada topico teorico inclui uma secao de "Aplicacoes" com exemplos reais em:
  - Engenharia de confiabilidade (tempo de vida de componentes)
  - Financas (retornos de acoes, risco de portfolio)
  - Medicina (dosagem e tempo de recuperacao)
  - Telecomunicacoes (filas, tempos de espera)
  - Controle de qualidade (inspecao de produtos)
  - Ciencias atuariais (sinistros, premios de seguro)
  - Fisica (mecanica quantica, termodinamica)
  - Simulacao estocastica (geracao de numeros pseudo-aleatorios)

---

## 7. Metacognicao

**Fonte:** Dunlosky et al. (2013); Freeman et al. (2014)

**Principio:** Incentivar o estudante a pensar sobre como ele aprende melhora a autorregulacao e a eficacia do estudo. Estudantes que monitoram seu proprio progresso tomam decisoes de estudo melhores.

**Implementacao no app:**
- Dashboard de progresso que mostra:
  - Topicos fortes e fracos (baseado em autoavaliacoes)
  - Frequencia de revisao por topico
  - Exercicios vistos vs. nao vistos
  - Historico de autoavaliacoes ao longo do tempo
- Sugestoes de revisao baseadas no desempenho

---

## 8. Interrogacao Elaborativa (Elaborative Interrogation)

**Fonte:** Dunlosky et al. (2013)

**Principio:** Perguntar "por que?" sobre cada fato e gerar uma explicacao para si mesmo aprofunda a compreensao, mesmo que a explicacao nao seja perfeita.

**Implementacao no app:**
- Prompt de "por que este passo?" antes de revelar a justificativa de cada etapa da resolucao
- Campos opcionais de anotacoes do estudante por exercicio

---

## Referencias

BJORK, R. A.; BJORK, E. L. Making things hard on yourself, but in a good way: creating desirable difficulties to enhance learning. In: *Psychology and the Real World*. Worth Publishers, 2011.

DUNLOSKY, J. et al. Improving students' learning with effective learning techniques: promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest*, v. 14, n. 1, p. 4-58, 2013.

FREEMAN, S. et al. Active learning increases student performance in science, engineering, and mathematics. *PNAS*, v. 111, n. 23, p. 8410-8415, 2014.

PAIVIO, A. *Mental Representations: A Dual Coding Approach*. Oxford University Press, 1986.

ROEDIGER, H. L.; KARPICKE, J. D. Test-enhanced learning: taking memory tests improves long-term retention. *Psychological Science*, v. 17, n. 3, p. 249-255, 2006.

SWELLER, J.; AYRES, P.; KALYUGA, S. *Cognitive Load Theory*. New York: Springer, 2011.

WEINSTEIN, Y.; SUMERACKI, M.; CAVIGLIOLI, O. *Understanding How We Learn: A Visual Guide*. Routledge, 2019.
