---
id: "dantas-cap07-q35"
titulo: "TLC — Intervalo de Confiança para Proporção de Eleitores"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 35"
---

## Enunciado

$X_i=\mathbf{1}_{\{\text{eleitor vota no candidato}\}}$, $p=P(X_i=1)$. $S_n=\sum X_i$.

(a) $P(|S_n/n - p|\ge 0{,}025)$ para $n=900$.
(b) Tamanho $n$ tal que $P(|S_n/n-p|\ge 0{,}025)=0{,}01$.

## Solução

$E(S_n/n)=p$, $\text{Var}(S_n/n)=p(1-p)/n$. Pelo TLC:

$$P\!\left(\left|\frac{S_n}{n}-p\right|\ge 0{,}025\right)\approx 2\left[1-\Phi\!\left(\frac{0{,}025}{\sqrt{p(1-p)/n}}\right)\right].$$

**(a) $n=900$:** Limitante com $p(1-p)\le 1/4$:

$$P\le 2\!\left[1-\Phi\!\left(\frac{0{,}025}{\sqrt{1/(4\cdot 900)}}\right)\right]=2[1-\Phi(1{,}5)]\approx 2(0{,}0668)=0{,}1336.$$

**Interpretação:** Com $n=900$, no máximo 13,36% de probabilidade de erro $\ge 2{,}5\%$.

**(b) $P=0{,}01$:** $2[1-\Phi(z)]=0{,}01\Rightarrow\Phi(z)=0{,}995\Rightarrow z=2{,}576$.

$$\frac{0{,}025}{\sqrt{p(1-p)/n}}\ge 2{,}576 \implies n\ge\frac{(2{,}576)^2\cdot p(1-p)}{(0{,}025)^2}.$$

Usando $p(1-p)\le 1/4$: $n\ge\frac{6{,}635\cdot 0{,}25}{0{,}000625}=2654$.
