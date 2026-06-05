---
id: "lista02-q25-distribuio-beta"
titulo: "Distribuição Beta"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Para $X \sim Beta(\alpha, \beta)$, determine a) E(X) e Var(X); b) a moda para $\alpha, \beta > 1$.

## Solução

**Definição:** FDP $f(x) = \frac{1}{B(\alpha, \beta)} x^{\alpha-1}(1-x)^{\beta-1}$, onde $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$.

## a) Média e Variância

O k-ésimo momento é $E[X^k] = \frac{B(\alpha+k, \beta)}{B(\alpha, \beta)}$.<br>**Média (k=1):** $E[X] = \frac{B(\alpha+1, \beta)}{B(\alpha, \beta)} = \frac{\Gamma(\alpha+1)\Gamma(\beta)}{\Gamma(\alpha+\beta+1)} \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}$. Usando $\Gamma(z+1)=z\Gamma(z)$, simplifica para $E[X] = \frac{\alpha}{\alpha+\beta}$.<br>**E[X²] (k=2):** $E[X^2] = \frac{B(\alpha+2, \beta)}{B(\alpha, \beta)} = \frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}$.<br>**Variância:** $Var(X) = E[X^2] - (E[X])^2 = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$.

## b) Moda

Maximizamos $\ln(f(x)) = C + (\alpha-1)\ln(x) + (\beta-1)\ln(1-x)$.<br>$\frac{d}{dx}\ln(f(x)) = \frac{\alpha-1}{x} - \frac{\beta-1}{1-x} = 0 \implies x_{moda} = \frac{\alpha-1}{\alpha+\beta-2}$.
