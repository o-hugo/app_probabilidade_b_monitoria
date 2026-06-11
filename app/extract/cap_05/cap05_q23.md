---
id: "dantas-cap05-q23"
titulo: "Tempo Médio de Vida Residual"
topicos: ["03-modelos-continuos"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "falta-de-memoria", "confiabilidade"]
referencia: "Dantas, Cap. 5, Q. 23"
---

## Enunciado

Para $T \ge 0$ contínua, o tempo médio de vida residual é $m(t) = E[T - t \mid T \ge t]$.

(a) Mostre que $m(t) = \dfrac{\int_t^\infty R(x)\,dx}{R(t)}$. (b) $m(t)$ para $T \sim \text{Exp}(\lambda)$. (c) $m(t)$ para $T \sim U(0,A)$.

## Passo 1: Item (a)

$$m(t) = E[T-t \mid T \ge t] = \frac{E[(T-t)\mathbf{1}_{T \ge t}]}{P(T \ge t)} = \frac{\int_t^\infty (x-t)f(x)\,dx}{R(t)}.$$

Integrando por partes ou usando o resultado do Q22 aplicado a $(T-t)^+$:

$$\int_t^\infty (x-t)f(x)\,dx = \int_t^\infty P(T-t > s \mid T \ge t) \cdot R(t)\,ds... $$

Mais diretamente: $\int_t^\infty (x-t)f(x)dx = \left[-(x-t)R(x)\right]_t^\infty + \int_t^\infty R(x)dx = \int_t^\infty R(x)dx$.

Portanto $m(t) = \dfrac{\int_t^\infty R(x)\,dx}{R(t)}$. $\blacksquare$

**Resumo:** Integração por partes converte a esperança em integral da função de sobrevivência.

## Passo 2: Item (b) — Exponencial

$R(x) = e^{-\lambda x}$.

$$m(t) = \frac{\int_t^\infty e^{-\lambda x}dx}{e^{-\lambda t}} = \frac{e^{-\lambda t}/\lambda}{e^{-\lambda t}} = \frac{1}{\lambda}.$$

A vida residual esperada é constante $= 1/\lambda$ — propriedade de falta de memória da exponencial.

**Resumo:** $m(t) = 1/\lambda$ (constante) — falta de memória.

## Passo 3: Item (c) — Uniforme em $(0,A)$

$R(x) = (A-x)/A$ para $0 < x < A$.

$$m(t) = \frac{\int_t^A \frac{A-x}{A}dx}{\frac{A-t}{A}} = \frac{\frac{(A-t)^2}{2A}}{\frac{A-t}{A}} = \frac{A-t}{2}.$$

A vida residual esperada decresce linearmente com $t$ — quanto mais velho, menos tempo resta em média.

**Resumo:** $m(t) = (A-t)/2$ para $U(0,A)$.
