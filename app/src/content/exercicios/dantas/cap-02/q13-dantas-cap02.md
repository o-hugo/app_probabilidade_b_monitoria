---
id: "q13-dantas-cap02"
titulo: "Questão 13"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Considere uma variável aleatória $X$ tal que $E(X^2) < \infty$. Seja $f(a) = E[(X - a)^2]$ uma função de $\mathbb{R}$ em $\mathbb{R}$. 
(a) Determine o valor $a^*$ de $a$ que minimiza $f(a)$. 
(b) Calcule $f(a^*)$, onde $a^*$ é o valor de $a$ obtido no item anterior. (Interprete estes resultados.)

## Solução

- **(a) Determine $a^*$ que minimiza $f(a)$:**
Podemos expandir a expressão de $f(a)$:
$$ f(a) = E[(X - a)^2] = E[X^2 - 2aX + a^2] $$
Aplicando a linearidade da esperança:
$$ f(a) = E[X^2] - 2a E[X] + a^2 $$
Temos uma equação polinomial de segundo grau (parábola) na variável $a$. Como o coeficiente de $a^2$ é positivo ($1$), a função possui um valor mínimo global.
Para encontrar o vértice (o ponto de mínimo), podemos derivar a função com relação a $a$ e igualar a zero (ou usar a fórmula de Bhaskara $x_v = \frac{-b}{2a}$):
$$ \frac{df(a)}{da} = -2 E[X] + 2a = 0 $$
$$ 2a = 2 E[X] \implies a^* = E[X] $$
Logo, a função é minimizada quando $a^*$ for a média (esperança) de $X$.

- **(b) Calcule $f(a^*)$:**
Substituindo $a^*$ pela média $\mu = E[X]$ em $f(a)$:
$$ f(E[X]) = E\left[ (X - E[X])^2 \right] $$
Pela definição formal de variância, essa expressão é exatamente:
$$ f(a^*) = \text{Var}(X) $$

**Interpretação dos resultados:**
O problema prova uma propriedade fundamental em estatística: **a variância é o menor erro quadrático médio possível**. 
Se você precisar usar uma constante simples ($a$) para "adivinhar" (ou predizer) o valor de uma variável aleatória $X$, o número que minimizará a soma dos erros quadráticos será sempre a média matemática $E[X]$. E a medida do erro quadrático residual dessa melhor estimativa nada mais é do que a própria variância $\text{Var}(X)$.
