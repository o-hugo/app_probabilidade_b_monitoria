---
id: "dantas-cap02-q36"
titulo: "FDA de Y = max(X, c) para FDP Generica"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["fda", "metodo-fda"]
referencia: "Dantas, Cap. 2, Q. 36"
---

## Enunciado
Seja X uma variável aleatória com função densidade de probabilidade f. Seja c um número real fixo. Determine a função de distribuição de $Y = \max(X, c)$ quando: 
(a) $f(x) = x$, $0 \le x \le 1$ e $c = 1/2$. 
(b) $f(x) = \lambda e^{-\lambda x}$ para $x \ge 0$ e $c = \lambda$.

## Solução

A função geral de distribuição acumulada de uma variável transformada por operador $\max$, neste caso $Y = \max(X, c)$, é calculada observando as condições:
Para encontrarmos $F_Y(y) = P(Y \le y) = P(\max(X, c) \le y)$:
- Se o valor de referência for menor do que o piso inferior arbitrário ($y < c$), então a igualdade é inatingível, pois o máximo tem como patamar inferior cravado a letra c. Portanto, $F_Y(y) = 0$.
- Se o valor de referência for maior ou igual ao piso arbitrário ($y \ge c$), então $\max(X, c)$ restringe-se inteiramente a buscar $X$. Logo, a desigualdade se reduz a $X \le y$. Concluindo: $F_Y(y) = P(X \le y) = F_X(y)$.

O que isto gera é uma variável mista que condensa em $y=c$ todas as probabilidades dos cenários em que $X \le c$.

- **(a) Quando $f(x) = x$ em $[0, 1]$ e $c = 1/2$:**
Primeiro, determinamos a acumulada base de X: 
$F_X(x) = \int_{0}^x t \cdot dt = \frac{x^2}{2}$.
A probabilidade do corte será absorvida pelo limite. Assim, a Função de Distribuição Acumulada $F_Y(y)$ será:
- Para $y < \frac{1}{2}$, $F_Y(y) = 0$.
- Para $\frac{1}{2} \le y \le 1$, $F_Y(y) = F_X(y) = \frac{y^2}{2}$.
- Para $y > 1$, $F_Y(y) = 1$.
*(Nota: há uma massa pontual de probabilidade $\frac{1}{8}$ aglutinada no exato ponto $y = \frac{1}{2}$).*

- **(b) Quando $f(x) = \lambda e^{-\lambda x}$ em $x \ge 0$ e $c = \lambda$:**
A base $X$ tem distribuição exponencial, onde a sua acumulada clássica é:
$F_X(x) = 1 - e^{-\lambda x}$.
Aplicando a regra da dedução geral onde a função original é eclipsada abaixo do limiar $\lambda$:
A Função de Distribuição Acumulada $F_Y(y)$ assume as seguintes formas:
- Para $y < \lambda$, $F_Y(y) = 0$.
- Para $y \ge \lambda$, $F_Y(y) = 1 - e^{-\lambda y}$.
*(Nota: há um aglutinamento massivo no ponto de inflexão da função: $P(Y = \lambda) = F_X(\lambda) = 1 - e^{-\lambda^2}$).*
