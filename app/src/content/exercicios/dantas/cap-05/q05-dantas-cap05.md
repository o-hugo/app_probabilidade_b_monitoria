---
id: "dantas-cap05-q05"
titulo: "Aproximação Normal para Binomial — 40 Lançamentos"
topicos: ["04-distribuicao-normal"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "tlc", "padronizacao-z"]
referencia: "Dantas, Cap. 5, Q. 5"
---

## Enunciado

Seja $X$ o número de caras em 40 lançamentos de uma moeda honesta. Determine $P(X = 20)$ pela aproximação normal e compare com o valor exato pela distribuição binomial.

## Passo 1: Parâmetros

$X \sim \text{Bin}(40, 1/2)$, $\mu = 20$, $\sigma^2 = 10$, $\sigma = \sqrt{10} \approx 3{,}162$.

**Resumo:** $\mu = np = 20$, $\sigma = \sqrt{10}$.

## Passo 2: Aproximação normal com correção de continuidade

$$P(X = 20) \approx P(19{,}5 < Y < 20{,}5), \quad Y \sim N(20, 10).$$

$$= P\!\left(\frac{-0{,}5}{\sqrt{10}} < Z < \frac{0{,}5}{\sqrt{10}}\right) = P(-0{,}158 < Z < 0{,}158) \approx 2\Phi(0{,}158) - 1 \approx 0{,}1256.$$

**Resumo:** $P(X=20) \approx 0{,}1256$ pela normal.

## Passo 3: Valor exato

$$P(X=20) = \binom{40}{20}\left(\frac{1}{2}\right)^{40} \approx 0{,}1268.$$

**Resumo:** A aproximação normal ($0{,}1256$) é muito próxima do valor exato ($0{,}1268$).
