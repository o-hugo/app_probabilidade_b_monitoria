---
id: "q16-dantas-cap02"
titulo: "Questão 16"
topicos: ["03-modelos-continuos","05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Dizemos que a distribuição da variável aleatória X é simétrica (em torno do zero) se $P(X \ge x) = P(X \le -x)$ para todo $x \in \mathbb{R}$. Mostre que: 
(a) Se X é simétrica e $E(|X|) < \infty$, então $E(X) = 0$. 
(b) Se X é simétrica em torno de $\mu$ e $E(|X|) < \infty$, então $E(X) = \mu$ (analogamente a definição apresentada, X é simétrica em torno de $\mu$ se $P(X \ge \mu + x) = P(X \le \mu - x)$, $\forall x \in \mathbb{R}$).

## Solução

- **(a) Mostre que se X é simétrica, $E(X) = 0$:**
Pela definição de simetria $P(X \ge x) = P(X \le -x)$, e diferenciando em relação a $x$ (caso contínuo), concluímos que a função de densidade (ou probabilidade) satisfaz $f_X(x) = f_X(-x)$. Isso significa que $X$ e $-X$ possuem exatamente a mesma distribuição de probabilidade.
Como a esperança matemática depende exclusivamente da distribuição, variáveis aleatórias com a mesma distribuição têm a mesma esperança.
$$ E(X) = E(-X) $$
Pela linearidade da esperança, sabemos que $E(-X) = -E(X)$. Logo:
$$ E(X) = -E(X) \implies 2E(X) = 0 \implies E(X) = 0 $$
*(A condição $E(|X|) < \infty$ apenas garante que a esperança não seja indeterminada da forma $\infty - \infty$).*

- **(b) Mostre que se X é simétrica em torno de $\mu$, então $E(X) = \mu$:**
Seja a variável aleatória auxiliar $Y = X - \mu$.
Sabemos que $X$ é simétrica em torno de $\mu$:
$$ P(X \ge \mu + x) = P(X \le \mu - x) $$
$$ P(X - \mu \ge x) = P(X - \mu \le -x) $$
Substituindo $Y$:
$$ P(Y \ge x) = P(Y \le -x) $$
Isto significa que $Y$ é simétrica em torno do zero. Pelo que acabamos de provar no item (a), $E(Y) = 0$.
Calculando a esperança de $Y$:
$$ E(Y) = E(X - \mu) = 0 $$
$$ E(X) - \mu = 0 \implies E(X) = \mu $$
Portanto, a esperança de uma variável simétrica sempre coincide com seu centro de simetria.
