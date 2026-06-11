---
id: "dantas-cap05-q21"
titulo: "Taxa de Mortalidade Dupla de Fumantes — Interpretação"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["taxa-de-falha", "confiabilidade"]
referencia: "Dantas, Cap. 5, Q. 21"
---

## Enunciado

"A taxa de mortalidade de fumantes é, em cada idade, o dobro da taxa de não-fumantes." O que isto significa? Implica que a probabilidade de sobreviver um número de anos é o dobro para não-fumantes?

## Solução

**Significado formal:** Se $h_F(x)$ e $h_{NF}(x)$ são as taxas de falha (mortalidade) de fumantes e não-fumantes à idade $x$, a afirmação diz $h_F(x) = 2h_{NF}(x)$ para todo $x$.

**Implicação para sobrevivência:** A função de confiabilidade é $R(x) = \exp\!\left(-\int_0^x h(t)dt\right)$.

$$R_F(x) = \exp\!\left(-\int_0^x 2h_{NF}(t)dt\right) = \left[\exp\!\left(-\int_0^x h_{NF}(t)dt\right)\right]^2 = [R_{NF}(x)]^2.$$

**Resposta:** Não — a probabilidade de sobreviver não é o dobro, mas o **quadrado**. Se $R_{NF}(x) = 0{,}9$ (não-fumante sobrevive com prob 0,9), então $R_F(x) = 0{,}81$ (fumante sobrevive com prob 0,81). A relação é $R_F = R_{NF}^2$, não $R_F = R_{NF}/2$.
