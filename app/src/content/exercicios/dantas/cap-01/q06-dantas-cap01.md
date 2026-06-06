---
id: "q06-dantas-cap01"
titulo: "Questão 6"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Prove e interprete as seguintes identidades:
(a) $\binom{n}{r} = \binom{n}{n-r}$ ;
(b) $\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1}$ .

## Solução

- **(a) $\binom{n}{r} = \binom{n}{n-r}$**
  - **Prova analítica:** Pela definição algébrica do coeficiente binomial, temos:
    $$ \binom{n}{r} = \frac{n!}{r!(n-r)!} $$
    $$ \binom{n}{n-r} = \frac{n!}{(n-r)!(n - (n-r))!} = \frac{n!}{(n-r)!r!} $$
    Portanto, os valores são idênticos.
  - **Interpretação combinatória:** Escolher $r$ elementos de um conjunto de $n$ elementos para formar um grupo é exatamente a mesma coisa que escolher $n-r$ elementos que ficarão **de fora** do grupo.

- **(b) $\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1}$** (Identidade de Pascal)
  - **Prova analítica:**
    $$ \binom{n}{r} + \binom{n}{r-1} = \frac{n!}{r!(n-r)!} + \frac{n!}{(r-1)!(n-r+1)!} $$
    Colocando o termo comum em evidência (multiplicando a primeira por $(n-r+1)/(n-r+1)$ e a segunda por $r/r$):
    $$ = \frac{n!(n-r+1)}{r!(n-r+1)!} + \frac{n!r}{r!(n-r+1)!} $$
    $$ = \frac{n!(n-r+1+r)}{r!(n-r+1)!} = \frac{n!(n+1)}{r!(n+1-r)!} = \frac{(n+1)!}{r!(n+1-r)!} = \binom{n+1}{r} $$
  - **Interpretação combinatória:** Suponha que queremos escolher um comitê de $r$ pessoas de um grupo de $n+1$ pessoas. Fixemos uma pessoa específica desse grupo, digamos, "João". Há dois casos possíveis para o comitê:
    1. **João não faz parte do comitê:** Precisamos então escolher as $r$ pessoas do restante do grupo de $n$ pessoas, o que nos dá $\binom{n}{r}$ maneiras.
    2. **João faz parte do comitê:** Como ele já está escolhido, precisamos escolher as $r-1$ pessoas restantes dentre as outras $n$ pessoas do grupo, o que nos dá $\binom{n}{r-1}$ maneiras.
    A soma das duas possibilidades cobre todos os comitês possíveis, resultando em $\binom{n+1}{r}$.
