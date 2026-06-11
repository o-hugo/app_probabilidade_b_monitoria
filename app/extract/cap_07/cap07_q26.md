---
id: "dantas-cap07-q26"
titulo: "Tamanho de Amostra — Estimação de Proporção"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z"]
referencia: "Dantas, Cap. 7, Q. 26"
---

## Enunciado

Estimar proporção $p$ com erro $<1\%$ e confiança 95%.

(a) Sabe-se que $p<0{,}10$. (b) Nada se sabe sobre $p$.

## Solução

Pelo TLC, $\hat{p}=S_n/n\approx N(p,p(1-p)/n)$.

Condição: $P(|\hat{p}-p|<0{,}01)\ge 0{,}95$, ou seja:

$$1{,}96\sqrt{\frac{p(1-p)}{n}}\le 0{,}01 \implies n\ge\frac{(1{,}96)^2 p(1-p)}{(0{,}01)^2}.$$

**(a) $p<0{,}10$:** Maximizar $p(1-p)$ em $[0,0{,}1]$: máximo em $p=0{,}1$, $p(1-p)=0{,}09$.

$$n\ge\frac{(1{,}96)^2\cdot 0{,}09}{0{,}0001}=\frac{3{,}8416\cdot 0{,}09}{0{,}0001}=3457{,}44 \implies n\ge 3458.$$

**(b) Sem informação sobre $p$:** Maximizar $p(1-p)$ em $[0,1]$: máximo em $p=0{,}5$, $p(1-p)=0{,}25$.

$$n\ge\frac{(1{,}96)^2\cdot 0{,}25}{0{,}0001}=9604.$$
