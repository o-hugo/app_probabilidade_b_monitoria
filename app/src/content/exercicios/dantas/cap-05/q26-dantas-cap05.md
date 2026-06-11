---
id: "dantas-cap05-q26"
titulo: "Função de Distribuição da Laplace"
topicos: ["03-modelos-continuos"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Cap. 5, Q. 26"
---

## Enunciado

$X$ tem distribuição de Laplace com parâmetro $\lambda > 0$: $f(x) = \frac{\lambda}{2}e^{-\lambda|x|}$, $x \in \mathbb{R}$. Determine $F(x)$.

## Solução

**Para $x < 0$:**
$$F(x) = \int_{-\infty}^x \frac{\lambda}{2}e^{\lambda t}dt = \frac{1}{2}e^{\lambda x}.$$

**Para $x \ge 0$:**
$$F(x) = \frac{1}{2} + \int_0^x \frac{\lambda}{2}e^{-\lambda t}dt = \frac{1}{2} + \frac{1}{2}(1 - e^{-\lambda x}) = 1 - \frac{1}{2}e^{-\lambda x}.$$

Portanto:
$$F(x) = \begin{cases} \dfrac{1}{2}e^{\lambda x} & x < 0 \\[6pt] 1 - \dfrac{1}{2}e^{-\lambda x} & x \ge 0 \end{cases}$$
