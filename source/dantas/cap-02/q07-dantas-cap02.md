---
id: "q07-dantas-cap02"
titulo: "Questão 7"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Dizemos que uma variável aleatória tem distribuição triangular no intervalo $[0, 1]$ se sua densidade é dada por $f(x) = cx$ para $0 \le x \le 1/2$, $f(x) = c(1-x)$ para $1/2 < x < 1$, e $f(x) = 0$ para os demais valores de $x$.
(a) Determine o valor da constante $c$.
(b) Esboce o gráfico de $f(x)$.
(c) Calcule $P(X > 8/10)$ e $P(1/4 < X < 3/4)$.

## Solução

- **(a) Determine o valor da constante $c$:**
Como é uma densidade de probabilidade, a área sob a curva no intervalo $[0, 1]$ deve ser 1.
Esta figura geométrica forma um triângulo com base de $0$ a $1$ (largura = 1).
O pico da função ocorre em $x = 1/2$, onde $f(1/2) = c(1/2) = c/2$.
A área do triângulo é $\frac{\text{base} \times \text{altura}}{2}$:
$$ \text{Área} = \frac{1 \times (c/2)}{2} = \frac{c}{4} = 1 \implies c = 4 $$
Portanto, a densidade é $f(x) = 4x$ (para $x \le 1/2$) e $f(x) = 4(1-x)$ (para $x > 1/2$).

- **(b) Esboço do gráfico de $f(x)$:**
O gráfico é um triângulo isósceles posicionado acima do eixo X.
Seus vértices são $(0, 0)$, $(1, 0)$ e o topo em $(0.5, 2)$. A inclinação da reta de subida é 4 e da reta de descida é -4.

- **(c) Calcule $P(X > 8/10)$ e $P(1/4 < X < 3/4)$:**

Para $P(X > 8/10)$:
O intervalo $[0.8, 1]$ cai totalmente na parte direita do triângulo, onde $f(x) = 4(1-x)$.
Esta probabilidade é a área de um pequeno triângulo cuja base é o intervalo de $0.8$ até $1$ (largura = $0.2$).
A altura no ponto $x=0.8$ é $f(0.8) = 4(1 - 0.8) = 4 \times 0.2 = 0.8$.
$$ \text{Área} = \frac{0.2 \times 0.8}{2} = \frac{0.16}{2} = 0,08 = \frac{2}{25} $$

Para $P(1/4 < X < 3/4)$:
Podemos calcular pela área complementar: $1 - P(X < 1/4) - P(X > 3/4)$.
Como o triângulo é simétrico, $P(X < 1/4) = P(X > 3/4)$.
$P(X < 1/4)$ é a área de um triângulo à esquerda de base $1/4$.
Altura em $x=1/4$ é $f(1/4) = 4(1/4) = 1$.
$$ P(X < 1/4) = \frac{(1/4) \times 1}{2} = \frac{1}{8} $$
Logo:
$$ P(1/4 < X < 3/4) = 1 - \frac{1}{8} - \frac{1}{8} = 1 - \frac{2}{8} = \frac{6}{8} = \frac{3}{4} = 0,75 $$
