---
id: "dantas-cap03-q42"
titulo: "Esperança do Número de Sobreviventes"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "E[λ_{x+t}] = ℓ_{x+t}"
tags: ["esperanca", "probabilidade"]
referencia: "Dantas, Cap. 3, Q. 42"
---

## Enunciado

Considere um grupo de $\ell_x$ pessoas de idade $x$, mutuamente independentes quanto a vida e morte. Seja $\lambda_{x+t}$ o número dessas pessoas que sobreviverão à idade $x+t$. Mostre que $E[\lambda_{x+t}] = \ell_{x+t}$.

## Solução

Para cada pessoa $i = 1, \ldots, \ell_x$, defina o indicador:

$$I_i = \begin{cases} 1 & \text{se a pessoa } i \text{ sobrevive até } x+t \\ 0 & \text{caso contrário} \end{cases}$$

Então $\lambda_{x+t} = \sum_{i=1}^{\ell_x} I_i$ e, por linearidade da esperança:

$$E[\lambda_{x+t}] = \sum_{i=1}^{\ell_x} E[I_i] = \sum_{i=1}^{\ell_x} P[\text{sobrevive } t \text{ anos} \mid \text{idade } x] = \ell_x \cdot {_tP_x}.$$

Pelo resultado do Exercício 41, $_tP_x = \ell_{x+t}/\ell_x$, portanto:

$$E[\lambda_{x+t}] = \ell_x \cdot \frac{\ell_{x+t}}{\ell_x} = \ell_{x+t}. \qquad \blacksquare$$
