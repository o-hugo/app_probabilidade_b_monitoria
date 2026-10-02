---
id: "dantas-cap05-q38"
titulo: "Distribuição Qui-Quadrado com 1 Grau de Liberdade: Y = X²"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Y ~ Gama(1/2, 1/2), E(Y)=1, Var(Y)=2"
tags: ["fdp-valida", "esperanca", "variancia", "metodo-fda"]
referencia: "Dantas, Cap. 5, Q. 38"
---

## Enunciado

$X \sim N(0,1)$, $Y = X^2$. (a) Determine $f_Y(y)$. (b) Calcule $E(Y)$ e $\text{Var}(Y)$.

## Passo 1: FDA e densidade de Y

Para $y > 0$:

$$F_Y(y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = 2\Phi(\sqrt{y}) - 1.$$

$$f_Y(y) = F_Y'(y) = \frac{1}{\sqrt{y}}\phi(\sqrt{y}) = \frac{1}{\sqrt{2\pi y}}e^{-y/2}, \quad y > 0.$$

Reconhecemos $f_Y(y) = \frac{1}{\Gamma(1/2)2^{1/2}}y^{1/2-1}e^{-y/2}$, que é a densidade **Gama$(1/2, 1/2)$** (= qui-quadrado com 1 grau de liberdade). $\blacksquare$

**Resumo:** $Y \sim \chi^2(1) = \text{Gama}(1/2, 1/2)$.

## Passo 2: Momentos

A FGM de $X \sim N(0,1)$ é $M_X(t) = e^{t^2/2}$ (caso $\mu = 0$, $\sigma^2 = 1$ de $e^{\mu t + \sigma^2 t^2/2}$, obtida completando o quadrado no expoente). Expandindo em série:

$$M_X(t) = \sum_{k=0}^{\infty}\frac{(t^2/2)^k}{k!} = 1 + \frac{t^2}{2} + \frac{t^4}{8} + \cdots$$

Como $E(X^n)$ é $n!$ vezes o coeficiente de $t^n$: $E(X^2) = 2!\cdot\frac{1}{2} = 1$ e $E(X^4) = 4!\cdot\frac{1}{8} = 3$. Em geral, $E(X^{2k}) = \frac{(2k)!}{2^k k!} = (2k-1)!!$.

$$E(Y) = E(X^2) = 1 = \text{Var}(X).$$

$$E(Y^2) = E(X^4) = 3.$$

$$\text{Var}(Y) = 3 - 1 = 2.$$
