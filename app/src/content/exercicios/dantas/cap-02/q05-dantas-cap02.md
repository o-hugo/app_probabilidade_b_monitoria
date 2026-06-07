---
id: "dantas-cap02-q05"
titulo: "Funcao Densidade Arbitraria e Constante Normalizadora"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "probabilidade"]
referencia: "Dantas, Cap. 2, Q. 5"
---

## Enunciado
Seja X uma variável aleatória com densidade $f(x) = cx^2$, $-1 \le x \le 1$, e $f(x) = 0$ caso contrário. 
(a) Determine o valor da constante $c$. 
(b) Calcule $P(|X| > \frac{1}{2})$. 
(c) Ache o valor de $\alpha$ tal que $F_X(\alpha) = P(X \le \alpha) = \frac{1}{4}$ (o valor de $\alpha$ que satisfaz esta relação é denominado primeiro quartil da distribuição de X).

## Solução

- **(a) Determine o valor da constante $c$:**
A área sob a curva da função de densidade de probabilidade deve ser 1.
$$ \int_{-1}^{1} cx^2 \, dx = 1 $$
$$ c \left[ \frac{x^3}{3} \right]_{-1}^{1} = 1 $$
$$ c \left( \frac{1^3}{3} - \frac{(-1)^3}{3} \right) = c \left( \frac{1}{3} + \frac{1}{3} \right) = \frac{2c}{3} = 1 $$
Logo, $c = \frac{3}{2}$.

- **(b) Calcule $P(|X| > \frac{1}{2})$:**
A condição $|X| > \frac{1}{2}$ equivale à união dos intervalos disjuntos $X < -\frac{1}{2}$ e $X > \frac{1}{2}$.
Como a função densidade $f(x) = \frac{3}{2}x^2$ é uma função par (simétrica em relação ao eixo y), as áreas dessas duas caudas são iguais.
$$ P(|X| > \frac{1}{2}) = 2 \times P(X > \frac{1}{2}) $$
$$ P(X > \frac{1}{2}) = \int_{1/2}^{1} \frac{3}{2}x^2 \, dx = \frac{3}{2} \left[ \frac{x^3}{3} \right]_{1/2}^{1} = \frac{1}{2} \left[ 1^3 - \left(\frac{1}{2}\right)^3 \right] = \frac{1}{2} \left(1 - \frac{1}{8}\right) = \frac{1}{2} \left(\frac{7}{8}\right) = \frac{7}{16} $$
$$ P(|X| > \frac{1}{2}) = 2 \times \frac{7}{16} = \frac{7}{8} = 0,875 $$

- **(c) Ache o valor de $\alpha$ tal que $P(X \le \alpha) = \frac{1}{4}$:**
Temos que integrar a densidade a partir do limite inferior ($-1$) até $\alpha$:
$$ \int_{-1}^{\alpha} \frac{3}{2}x^2 \, dx = \frac{1}{4} $$
$$ \frac{3}{2} \left[ \frac{x^3}{3} \right]_{-1}^{\alpha} = \frac{1}{4} $$
$$ \frac{1}{2} \left( \alpha^3 - (-1)^3 \right) = \frac{1}{4} $$
$$ \frac{1}{2} (\alpha^3 + 1) = \frac{1}{4} $$
Multiplicando por 2:
$$ \alpha^3 + 1 = \frac{1}{2} $$
$$ \alpha^3 = \frac{1}{2} - 1 = -\frac{1}{2} $$
Tirando a raiz cúbica (que preserva o sinal):
$$ \alpha = -\sqrt[3]{\frac{1}{2}} \approx -0,7937 $$
