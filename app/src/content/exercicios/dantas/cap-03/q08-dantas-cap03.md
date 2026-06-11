---
id: "dantas-cap03-q08"
titulo: "Covariância e independência no problema da urna (Ex. 1)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Cov(X,Y) = -9/44; X e Y não são independentes"
tags: ["variancia", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 8"
---

# Exercício 8

Com base no Exercício 1 (urna com 3 vermelhas, 4 brancas, 5 azuis; 3 retiradas sem reposição; $X$ = nº vermelhas, $Y$ = nº brancas):

**(a)** Calcule $\text{Cov}(X, Y)$.

**(b)** $X$ e $Y$ são independentes?

---

## Passo 1: Esperanças marginais $E[X]$ e $E[Y]$

**Resumo:** $X \sim \text{Hipergeométrica}(12, 3, 3)$ e $Y \sim \text{Hipergeométrica}(12, 4, 3)$, com médias $n K/N$.

$$E[X] = 3 \cdot \frac{3}{12} = \frac{3}{4}, \qquad E[Y] = 3 \cdot \frac{4}{12} = 1.$$

---

## Passo 2: $E[XY]$

**Resumo:** Calcula-se $\sum_{x,y} xy \cdot p(x,y)$ usando a tabela do Exercício 1.

Os únicos pares com $xy \neq 0$ são $(1,1)$, $(1,2)$, $(2,1)$:

$$E[XY] = 1\cdot 1 \cdot \frac{60}{220} + 1 \cdot 2 \cdot \frac{18}{220} + 2 \cdot 1 \cdot \frac{12}{220}$$

$$= \frac{60 + 36 + 24}{220} = \frac{120}{220} = \frac{6}{11}.$$

---

## Passo 3: Covariância

**Resumo:** Aplica-se $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$.

$$\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = \frac{6}{11} - \frac{3}{4} \cdot 1 = \frac{6}{11} - \frac{3}{4} = \frac{24 - 33}{44} = -\frac{9}{44}.$$

$$\boxed{\text{Cov}(X,Y) = -\frac{9}{44} \approx -0{,}205}$$

O sinal negativo é intuitivo: quanto mais bolas vermelhas, menos brancas podem ser retiradas (a soma é limitada a 3).

---

## Passo 4: Independência

**Resumo:** $\text{Cov}(X,Y) \neq 0$ implica dependência; verificação direta confirma.

Como $\text{Cov}(X,Y) = -9/44 \neq 0$, $X$ e $Y$ **não são independentes**.

(Verificação: $p_X(1) \cdot p_Y(1) = \frac{108}{220} \cdot \frac{112}{220} \neq \frac{60}{220} = p(1,1)$.)
