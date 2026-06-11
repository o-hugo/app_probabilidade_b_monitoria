---
id: "dantas-cap07-q38"
titulo: "TLC — Número de Medições para Estimação de Distância"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z"]
referencia: "Dantas, Cap. 7, Q. 38"
---

## Enunciado

Medições i.i.d. com média $\mu$ e variância $\sigma^2=4$. Quantas medições $n$ para que $P(|\bar{X}_n-\mu|\le 0{,}5)\ge 0{,}99$?

## Solução

$\text{Var}(\bar{X}_n)=4/n$, $\sigma_{\bar{X}}=2/\sqrt{n}$.

Pelo TLC:

$$P(|\bar{X}_n-\mu|\le 0{,}5)\approx 2\Phi\!\left(\frac{0{,}5}{2/\sqrt{n}}\right)-1=2\Phi\!\left(\frac{\sqrt{n}}{4}\right)-1\ge 0{,}99.$$

$$\Phi\!\left(\frac{\sqrt{n}}{4}\right)\ge 0{,}995 \implies \frac{\sqrt{n}}{4}\ge 2{,}576 \implies \sqrt{n}\ge 10{,}304 \implies n\ge 106{,}2.$$

O astrônomo precisa de pelo menos $n=\mathbf{107}$ medições.
