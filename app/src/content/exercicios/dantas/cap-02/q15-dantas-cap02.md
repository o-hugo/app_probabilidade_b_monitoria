---
id: "dantas-cap02-q15"
titulo: "Distribuicao com Esperanca Finita mas Variancia Infinita"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "variancia"]
referencia: "Dantas, Cap. 2, Q. 15"
---

## Enunciado
Seja $X$ uma variável aleatória cuja função densidade é dada por: $f(x) = \frac{2}{x^3}$ para $1 \le x \le \infty$ e zero no complementar. 
Verifique que $E(X) = 2$, mas não existe $\text{Var}(X)$ (isto é, $\text{Var}(X) = \infty$).

## Solução

- **Cálculo da Esperança $E(X)$:**
A esperança de uma variável contínua é a integral de $x \cdot f(x)$ em todo o domínio:
$$ E(X) = \int_{1}^{\infty} x \left(\frac{2}{x^3}\right) \, dx = \int_{1}^{\infty} \frac{2}{x^2} \, dx $$
Esta integral é convergente e sua primitiva é $-\frac{2}{x}$:
$$ E(X) = \left[ -\frac{2}{x} \right]_1^\infty $$
Avalia-se do limite:
$$ E(X) = \lim_{x \to \infty} \left(-\frac{2}{x}\right) - \left(-\frac{2}{1}\right) = 0 - (-2) = 2 $$
O valor da esperança foi verificado com sucesso ($E(X) = 2$).

- **Cálculo da Variância $\text{Var}(X)$:**
A variância necessita que o segundo momento, $E(X^2)$, seja finito. Vamos investigar $E(X^2)$:
$$ E(X^2) = \int_{1}^{\infty} x^2 \left(\frac{2}{x^3}\right) \, dx = \int_{1}^{\infty} \frac{2}{x} \, dx $$
A primitiva de $\frac{1}{x}$ é o logaritmo natural $\ln(x)$:
$$ E(X^2) = \left[ 2 \ln(x) \right]_1^\infty $$
Avalia-se do limite:
$$ E(X^2) = \lim_{x \to \infty} (2 \ln(x)) - (2 \ln(1)) = \infty - 0 = \infty $$
A integral para o segundo momento diverge (vai para o infinito).
Uma vez que a fórmula da variância é $\text{Var}(X) = E(X^2) - (E(X))^2$, o termo infinito domina a equação, fazendo com que a variância assuma um valor matematicamente infinito.
$$ \text{Var}(X) = \infty - (2)^2 = \infty $$
Portanto, a variância não existe como um número real finito.
