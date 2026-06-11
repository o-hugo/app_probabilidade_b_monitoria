---
id: "dantas-cap07-q33"
titulo: "TLC — Distribuição Assintótica do Número de Carros (Binomial Negativa)"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z"]
referencia: "Dantas, Cap. 7, Q. 33"
---

## Enunciado

Cada carro compra um jornal com probabilidade $1/3$. $Y=$ número de carros até vender 90 jornais. Determine a distribuição assintótica de $Y$.

## Solução

$Y\sim\text{BinNeg}(r=90, p=1/3)$: número de tentativas para $r=90$ sucessos.

$Y=\sum_{i=1}^{90}G_i$ onde $G_i\sim\text{Geom}(1/3)$ i.i.d.: $E(G_i)=3$, $\text{Var}(G_i)=\frac{1-p}{p^2}=6$.

$E(Y)=270$, $\text{Var}(Y)=540$, $\sigma_Y=\sqrt{540}=6\sqrt{15}\approx 23{,}24$.

Pelo TLC:

$$Y\xrightarrow{d}N(270,540).$$

**Resumo:** $Y$ tem distribuição assintótica $N(\mu=270,\sigma^2=540)$.
