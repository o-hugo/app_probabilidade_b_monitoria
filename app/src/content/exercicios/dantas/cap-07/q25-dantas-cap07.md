---
id: "dantas-cap07-q25"
titulo: "TLC — Aproximação Normal para Gama(n,λ)"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z"]
referencia: "Dantas, Cap. 7, Q. 25"
---

## Enunciado

$X\sim\text{Gama}(n,\lambda)$, $n\in\mathbb{N}$. Justifique o emprego da distribuição normal e mostre como calcular $P(X\le x)$.

## Solução

**Justificativa:** $X\overset{d}{=}\sum_{i=1}^n Y_i$ onde $Y_i\sim\text{Exp}(\lambda)$ i.i.d. (pois Gama$(n,\lambda)$ é soma de $n$ exponenciais independentes com parâmetro $\lambda$).

Pelo **Teorema do Limite Central**:

$$\frac{X-E(X)}{\sqrt{\text{Var}(X)}}=\frac{X-n/\lambda}{\sqrt{n}/\lambda}\xrightarrow{d}N(0,1) \text{ quando }n\to\infty.$$

**Cálculo de $P(X\le x)$:**

$$P(X\le x)\approx\Phi\!\left(\frac{x-n/\lambda}{\sqrt{n}/\lambda}\right)=\Phi\!\left(\frac{\lambda x-n}{\sqrt{n}}\right).$$
