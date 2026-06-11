---
id: "dantas-cap05-q25"
titulo: "Distribuição Beta — Esperança, Variância e Moda"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "E(X) = α/(α+β), Var(X) = αβ/[(α+β)²(α+β+1)], moda = (α-1)/(α+β-2)"
tags: ["esperanca", "variancia", "moda"]
referencia: "Dantas, Cap. 5, Q. 25"
---

## Enunciado

$X \sim \text{Beta}(\alpha,\beta)$ com $f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$, $0<x<1$.

(a) Determine $E(X)$ e $\text{Var}(X)$. (b) Para $\alpha>1, \beta>1$, determine a moda $x^* = \arg\max f(x)$.

## Passo 1: $E(X)$

$$E(X) = \frac{1}{B(\alpha,\beta)}\int_0^1 x^\alpha(1-x)^{\beta-1}dx = \frac{B(\alpha+1,\beta)}{B(\alpha,\beta)} = \frac{\Gamma(\alpha+1)\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\alpha+\beta+1)} = \frac{\alpha}{\alpha+\beta}.$$

**Resumo:** $E(X) = \alpha/(\alpha+\beta)$.

## Passo 2: $E(X^2)$ e $\text{Var}(X)$

$$E(X^2) = \frac{B(\alpha+2,\beta)}{B(\alpha,\beta)} = \frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}.$$

$$\text{Var}(X) = E(X^2) - [E(X)]^2 = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.$$

**Resumo:** $\text{Var}(X) = \alpha\beta/[(\alpha+\beta)^2(\alpha+\beta+1)]$.

## Passo 3: Moda (item b)

Maximizar $\ln f(x) = (\alpha-1)\ln x + (\beta-1)\ln(1-x) + \text{const}$:

$$\frac{d}{dx}\ln f = \frac{\alpha-1}{x} - \frac{\beta-1}{1-x} = 0 \implies x^* = \frac{\alpha-1}{\alpha+\beta-2}, \quad \alpha>1, \beta>1.$$
