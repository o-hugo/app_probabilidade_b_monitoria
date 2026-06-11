---
id: "dantas-cap05-q41"
titulo: "Família Exponencial Uniparamétrica"
topicos: ["03-modelos-continuos"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida"]
referencia: "Dantas, Cap. 5, Q. 41"
---

## Enunciado

$f(x,\theta) = S(x)\cdot t(\theta)\cdot e^{a(x)b(\theta)}$ é a forma da família exponencial. Verifique quais distribuições pertencem a essa família:

(a) $U(0,A)$; (b) $N(\mu, 4)$; (c) $\text{Exp}(\lambda)$; (d) $\text{Beta}(\alpha,\beta)$ com $\alpha$ conhecido.

## Solução

**(a) $U(0,A)$:** $f(x) = 1/A$ para $0 < x < A$. O suporte $D = (0,A)$ **depende do parâmetro $A$**, violando a condição de que $D$ seja independente de $\theta$. **Não pertence** à família exponencial.

**(b) $N(\mu,4)$:**

$$f(x,\mu) = \frac{1}{2\sqrt{2\pi}}e^{-(x-\mu)^2/8} = \frac{1}{2\sqrt{2\pi}}e^{-x^2/8}\cdot e^{\mu^2/8}\cdot e^{x\mu/4}.$$

Identificando: $S(x) = e^{-x^2/8}$, $t(\mu) = e^{\mu^2/8}/(2\sqrt{2\pi})$, $a(x) = x$, $b(\mu) = \mu/4$. **Pertence** à família exponencial.

**(c) $\text{Exp}(\lambda)$:**

$$f(x,\lambda) = \lambda e^{-\lambda x} = \underbrace{1}_{S(x)}\cdot\underbrace{\lambda}_{t(\lambda)}\cdot e^{\underbrace{x}_{a(x)}\cdot\underbrace{(-\lambda)}_{b(\lambda)}}.$$

**Pertence** à família exponencial.

**(d) $\text{Beta}(\alpha,\beta)$ com $\alpha$ fixo:**

$$f(x,\beta) = \frac{1}{B(\alpha,\beta)}x^{\alpha-1}(1-x)^{\beta-1} = \frac{x^{\alpha-1}}{B(\alpha,\beta)}\cdot e^{(\beta-1)\ln(1-x)}.$$

Identificando: $S(x) = x^{\alpha-1}$, $t(\beta) = 1/B(\alpha,\beta)$, $a(x) = \ln(1-x)$, $b(\beta) = \beta-1$. Suporte $(0,1)$ independente de $\beta$. **Pertence** à família exponencial.
