# Decisoes de Conteudo

Registro de decisoes editoriais sobre o que entra ou nao no app, para referencia
de futuros colaboradores e agentes de IA.

## Capitulo 4 do Dantas (modelos discretos) nao integrado

**Data:** 2026-06-11
**Decisao:** as 41 questoes de `app/extract/cap_04/` NAO foram integradas ao app.

**Motivo:** o Capitulo 4 do Dantas cobre os principais modelos discretos
(Binomial, Poisson, Hipergeometrica, Geometrica, Binomial Negativa). Esse
assunto nao e de interesse para a disciplina Probabilidade B, cuja ementa
e centrada em variaveis aleatorias continuas. Alem disso, as questoes vieram
no extract marcadas com o topico `03-modelos-continuos`, o que poluiria o
filtro de exercicios com conteudo discreto.

**Consequencias praticas:**

- Os arquivos permanecem em `app/extract/cap_04/` como material-fonte, sem
  processamento, caso a decisao seja revista no futuro.
- Nao existe diretorio `app/src/content/exercicios/dantas/cap-04/`.
- Se um dia for desejavel integra-las, recomenda-se criar um topico proprio
  de modelos discretos (marcado como conteudo extra, fora da ementa) em vez
  de reaproveitar `03-modelos-continuos`.

## Capitulo 7 do Dantas integrado como topicos extras

**Data:** 2026-06-11
**Decisao:** o conteudo do Capitulo 7 (desigualdades e convergencia) foi
integrado em dois topicos novos marcados como extras, fora da ementa:
`07-desigualdades-concentracao` e `07-convergencia-e-tlc`.

As questoes q01 a q08 do extract vieram marcadas com o topico
`07-convergencia-e-tlc`, mas tratam de desigualdades (Markov, Tchebyschev,
Chernoff) e foram reclassificadas para `07-desigualdades-concentracao`
durante a integracao.
