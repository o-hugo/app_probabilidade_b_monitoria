---
id: "lista02-q01-distribuio-uniforme-0-20"
titulo: "Distribuição Uniforme (0, 20)"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["probabilidade"]
---

## Enunciado

Se X é uniformemente distribuída no intervalo (0, 20), calcule a probabilidade de: 

 a) $ X < 3 $ 

 b) $ X > 12 $ 

 c) $ 4 < X < 11 $ 

 d) $ |X-3| < 4 $

## Solução

**Definição:** Para $X \sim U(a, b)$, a Função de Densidade de Probabilidade (FDP) é $f(x) = \frac{1}{b-a}$ para $a < x < b$. Aqui, $a=0, b=20$, então $f(x) = \frac{1}{20}$.

                    
A probabilidade $P(c < X < d)$ é a integral $\int_c^d f(x)dx$, que para a uniforme é a área de um retângulo: $(d-c) \times \frac{1}{b-a}$.

                    
## a) $ P(X < 3) $

Isso equivale a $P(0 < X < 3)$.

$$ P(X < 3) = \int_0^3 \frac{1}{20} dx = \frac{1}{20} [x]_0^3 = \frac{3 - 0}{20} = 0.15 $$

                    
## b) $ P(X > 12) $

Isso equivale a $P(12 < X < 20)$.

$$ P(X > 12) = \int_{12}^{20} \frac{1}{20} dx = \frac{20 - 12}{20} = 0.40 $$

                    
## c) $ P(4 < X < 11) $

$$ P(4 < X < 11) = \int_4^{11} \frac{1}{20} dx = \frac{11 - 4}{20} = 0.35 $$

                    
## d) $ P(|X-3| < 4) $

**Passo 1: Resolver a inequação.** $|X-3| < 4 \implies -4 < X-3 < 4$.

**Passo 2: Isolar X.** Somando 3: $-1 < X < 7$.

**Passo 3: Considerar o domínio de X.** A interseção de $(-1, 7)$ com $(0, 20)$ é $(0, 7)$.

$$ P(0 < X < 7) = \int_0^7 \frac{1}{20} dx = \frac{7-0}{20} = 0.35 $$
