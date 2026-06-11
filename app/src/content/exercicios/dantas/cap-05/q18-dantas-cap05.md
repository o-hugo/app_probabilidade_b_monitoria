---
id: "dantas-cap05-q18"
titulo: "Tamanho de Amostra para Estimação de Proporção"
topicos: ["04-distribuicao-normal"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "n = 40000; para p ≤ 0,20: n = 16000"
tags: ["tlc", "padronizacao-z"]
referencia: "Dantas, Cap. 5, Q. 18"
---

## Enunciado

Proporção de fumantes $p$ desconhecida. Quer-se $P(|\hat{p} - p| \le 0{,}005) \ge 0{,}95$. (a) Qual o tamanho amostral $n$? (b) Se $p \le 0{,}20$, qual $n$?

## Passo 1: Pela aproximação normal (TLC)

$\hat{p} = X/n$ com $X \sim \text{Bin}(n,p)$. Pelo TLC: $\hat{p} \approx N(p, p(1-p)/n)$.

$$P(|\hat{p}-p| \le 0{,}005) = P\!\left(|Z| \le \frac{0{,}005}{\sqrt{p(1-p)/n}}\right) \ge 0{,}95.$$

Para $P(|Z| \le z_{0{,}025}) = 0{,}95$: $z_{0{,}025} = 1{,}96$.

$$\frac{0{,}005}{\sqrt{p(1-p)/n}} \ge 1{,}96 \implies n \ge \frac{(1{,}96)^2 p(1-p)}{(0{,}005)^2}.$$

**Resumo:** $n \ge (1{,}96)^2 p(1-p) / (0{,}005)^2$.

## Passo 2: Item (a) — $p$ desconhecido

$p(1-p) \le 1/4$ para todo $p$. Usando o pior caso $p = 0{,}5$:

$$n \ge \frac{(1{,}96)^2 \cdot 0{,}25}{(0{,}005)^2} = \frac{3{,}8416 \cdot 0{,}25}{0{,}000025} = \frac{0{,}9604}{0{,}000025} = 38.416 \approx 38.416.$$

Arredondando: $n = 38.416$ (ou usando $z=2$: $n = 40.000$).

**Resumo:** $n \approx 38.416$ com $z=1{,}96$; usa-se frequentemente $n=40.000$ com $z=2$.

## Passo 3: Item (b) — $p \le 0{,}20$

Máximo de $p(1-p)$ para $p \le 0{,}20$ é em $p = 0{,}20$: $p(1-p) = 0{,}16$.

$$n \ge \frac{(1{,}96)^2 \cdot 0{,}16}{(0{,}005)^2} \approx \frac{3{,}8416 \cdot 0{,}16}{0{,}000025} \approx 24.586.$$

Usando $z=2$: $n = (4)(0{,}16)/0{,}000025 = 25.600$.

**Resumo:** Com $p \le 0{,}20$, basta $n \approx 24.586$ (ou 25.600 com $z=2$).
