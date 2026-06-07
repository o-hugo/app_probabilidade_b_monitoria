---
id: "lista02-q02-distribuio-normal-3-9"
titulo: "Distribuição Normal (μ=3, σ²=9)"
topicos: ["distribuicao-normal"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["padronizacao-z"]
---

## Enunciado

Se X é uma variável aleatória normal com $\mu=3$ e $\sigma^{2}=9$, determine: 

 a) $ P(2 < X < 5) $ 

 b) $ P(X > 0) $ 

 c) $ P(|X-3| > 6) $

## Solução

**Definição:** Padronizamos $X \sim N(\mu, \sigma^2)$ para $Z \sim N(0, 1)$ usando $Z = \frac{X - \mu}{\sigma}$. Aqui, $\mu=3$ e $\sigma^2=9 \implies \sigma=3$.

                    
## a) $ P(2 < X < 5) $

**Padronização:**<br>$Z_1 = \frac{2-3}{3} \approx -0.33$ e $Z_2 = \frac{5-3}{3} \approx 0.67$

**Cálculo:**$ P(-0.33 < Z < 0.67) = \Phi(0.67) - \Phi(-0.33) = \Phi(0.67) - (1 - \Phi(0.33)) \approx 0.7486 - (1 - 0.6293) = 0.3779 $

                    
## b) $ P(X > 0) $

**Padronização:** $Z = \frac{0-3}{3} = -1$

**Cálculo:**$ P(Z > -1) = 1 - \Phi(-1) = \Phi(1) \approx 0.8413 $

                    
## c) $ P(|X-3| > 6) $

**Simplificação:** $|X-3| > 6 \implies X > 9$ ou $X < -3$.

**Cálculo:**$ P(X>9) + P(X<-3) = P(Z > \frac{9-3}{3}) + P(Z < \frac{-3-3}{3}) = P(Z > 2) + P(Z < -2) $. Pela simetria, $ = 2 \times P(Z < -2) = 2(1 - \Phi(2)) \approx 0.0456 $
