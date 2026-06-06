---
id: "q35-dantas-cap02"
titulo: "Questão 35"
topicos: ["03-modelos-continuos","05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Suponha que X denote a posição de um ponto escolhido uniformemente no intervalo (0,5). Seja Y uma variável aleatória tal que $Y=0$ se $X \le 1$, $Y=5$ se $X \ge 3$ e $Y=X$ caso contrário, determine a função de distribuição de Y.

## Solução

A posição de $X$ segue uma distribuição Uniforme, $X \sim \text{U}(0, 5)$, o que significa que sua densidade de probabilidade é $f_X(x) = \frac{1}{5}$ e sua função de distribuição é $F_X(x) = \frac{x}{5}$ no intervalo $[0, 5]$.

A variável $Y$ funciona como uma função por partes contínua e truncada de $X$:
- $Y = 0$, para $0 < X \le 1$.
- $Y = X$, para $1 < X < 3$.
- $Y = 5$, para $3 \le X < 5$.

Essa operação é conhecida como *censura* em suas pontas. A variável aleatória resultante não será puramente contínua nem puramente discreta, mas sim uma distribuição mista, possuindo massas de probabilidade ("saltos") nos valores limítrofes.

Calculamos essas probabilidades massificadas em $Y=0$ e $Y=5$:
$$ P(Y = 0) = P(X \le 1) = \frac{1}{5} $$
$$ P(Y = 5) = P(X \ge 3) = \frac{5 - 3}{5} = \frac{2}{5} $$

Para todos os valores onde $1 < Y < 3$, a probabilidade de acúmulo será a massa estagnada inicial mais o trecho onde $Y=X$:
$$ P(Y \le y) = P(Y=0) + P(0 < Y \le y) = P(X \le 1) + P(1 < X \le y) = P(X \le y) = \frac{y}{5} $$

Podemos formalizar a Função de Distribuição Acumulada $F_Y(y) = P(Y \le y)$:
- Se $y < 0$: $F_Y(y) = 0$
- Se $0 \le y < 1$: $F_Y(y) = \frac{1}{5}$ (Massa no extremo inferior, permanece estável)
- Se $1 \le y < 3$: $F_Y(y) = \frac{y}{5}$ (Crescimento linear, cópia idêntica do comportamento de $X$)
- Se $3 \le y < 5$: $F_Y(y) = \frac{3}{5}$ (Permanece estável pois não existem valores de $Y$ nessa fenda)
- Se $y \ge 5$: $F_Y(y) = 1$ (Salto final devido à massa no extremo superior, contemplando a totalidade)
