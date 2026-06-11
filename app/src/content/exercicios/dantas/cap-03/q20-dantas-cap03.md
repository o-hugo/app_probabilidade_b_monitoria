---
id: "dantas-cap03-q20"
titulo: "Análise de matriz de covariância 4×4: correlações e pares especiais"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "ρ(X1,(X2+X3)/2) = -1/(2*sqrt(61))"
tags: ["variancia", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 20"
---

# Exercício 20

As variâncias e covariâncias de $(X_1, X_2, X_3, X_4)$ são dadas pela matriz de covariâncias:

$$\Sigma = \begin{pmatrix} 25 & -3 & 2 & 2 \\ -3 & 36 & 2 & 0 \\ 2 & 2 & 100 & 2 \\ 2 & 0 & 2 & 400 \end{pmatrix}$$

Ou seja: $\text{Var}(X_1)=25$, $\text{Var}(X_2)=36$, $\text{Var}(X_3)=100$, $\text{Var}(X_4)=400$; e $\text{Cov}(X_1,X_2)=-3$, $\text{Cov}(X_1,X_3)=2$, $\text{Cov}(X_1,X_4)=2$, $\text{Cov}(X_2,X_3)=2$, $\text{Cov}(X_2,X_4)=0$, $\text{Cov}(X_3,X_4)=2$.

Determine:

**(a)** O par com correlação negativa.

**(b)** Os pares não-correlacionados.

**(c)** O par com maior correlação (em valor absoluto).

**(d)** $\rho\!\left(X_1,\; \dfrac{X_2+X_3}{2}\right)$.

---

## Passo 1: Calcular todos os coeficientes de correlação

**Resumo:** $\rho(X_i, X_j) = \text{Cov}(X_i,X_j)/(\sigma_i \sigma_j)$ com $\sigma_1=5$, $\sigma_2=6$, $\sigma_3=10$, $\sigma_4=20$.

| Par | Cov | $\sigma_i \sigma_j$ | $\rho$ |
|:---:|:---:|:---:|:---:|
| $(1,2)$ | $-3$ | $5 \cdot 6 = 30$ | $-3/30 = -0{,}10$ |
| $(1,3)$ | $2$ | $5 \cdot 10 = 50$ | $2/50 = 0{,}04$ |
| $(1,4)$ | $2$ | $5 \cdot 20 = 100$ | $2/100 = 0{,}02$ |
| $(2,3)$ | $2$ | $6 \cdot 10 = 60$ | $2/60 \approx 0{,}033$ |
| $(2,4)$ | $0$ | $6 \cdot 20 = 120$ | $0$ |
| $(3,4)$ | $2$ | $10 \cdot 20 = 200$ | $2/200 = 0{,}01$ |

---

## Passo 2: Respostas (a), (b), (c)

**Resumo:** Identifica-se os casos especiais diretamente da tabela acima.

**(a)** Par com correlação **negativa**: $(X_1, X_2)$ com $\rho = -0{,}10$.

**(b)** Par **não-correlacionado** ($\rho = 0$): $(X_2, X_4)$.

**(c)** Par com **maior correlação** (em valor absoluto): $(X_1, X_2)$ com $|\rho| = 0{,}10$.

---

## Passo 3: $\rho\!\left(X_1, \frac{X_2+X_3}{2}\right)$

**Resumo:** Calcula-se covariância e variância da média aritmética $W = (X_2+X_3)/2$.

$$\text{Cov}\!\left(X_1, \frac{X_2+X_3}{2}\right) = \frac{1}{2}\text{Cov}(X_1, X_2+X_3) = \frac{1}{2}[\text{Cov}(X_1,X_2) + \text{Cov}(X_1,X_3)]$$

$$= \frac{1}{2}(-3 + 2) = -\frac{1}{2}.$$

$$\text{Var}\!\left(\frac{X_2+X_3}{2}\right) = \frac{1}{4}\text{Var}(X_2+X_3) = \frac{1}{4}[\text{Var}(X_2) + \text{Var}(X_3) + 2\text{Cov}(X_2,X_3)]$$

$$= \frac{1}{4}(36 + 100 + 4) = \frac{140}{4} = 35.$$

$$\rho\!\left(X_1, \frac{X_2+X_3}{2}\right) = \frac{-1/2}{\sqrt{25} \cdot \sqrt{35}} = \frac{-1/2}{5\sqrt{35}} = \frac{-1}{10\sqrt{35}} = \frac{-1}{10\sqrt{35}} \approx -0{,}0169.$$

$$\boxed{\rho\!\left(X_1, \frac{X_2+X_3}{2}\right) = -\frac{1}{10\sqrt{35}} \approx -0{,}017}$$
