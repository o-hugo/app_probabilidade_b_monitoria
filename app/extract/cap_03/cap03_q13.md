---
id: "dantas-cap03-q13"
titulo: "E[g(X)f(Y)] = E[g(X)]E[f(Y)] para X, Y discretas independentes"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "Demonstrado usando a fatoração da distribuição conjunta"
tags: ["esperanca"]
referencia: "Dantas, Cap. 3, Q. 13"
---

# Exercício 13

Sejam $X$ e $Y$ variáveis aleatórias discretas independentes, e $g$ e $f$ funções quaisquer (para as quais as esperanças existem). Mostre que:

$$E[g(X)\, f(Y)] = E[g(X)] \cdot E[f(Y)].$$

---

## Solução

Pela definição de esperança para funções de variáveis aleatórias discretas:

$$E[g(X)\, f(Y)] = \sum_{x}\sum_{y} g(x)\, f(y)\, p(x,y),$$

onde a soma é sobre todos os pares $(x,y)$ no suporte de $(X,Y)$.

Como $X$ e $Y$ são **independentes**, a distribuição conjunta fatora:

$$p(x,y) = p_X(x)\cdot p_Y(y) \quad \text{para todo } (x,y).$$

Substituindo:

$$E[g(X)\, f(Y)] = \sum_{x}\sum_{y} g(x)\, f(y)\, p_X(x)\, p_Y(y).$$

Reagrupando (a dupla soma se fatora em produto de somas simples):

$$= \left(\sum_{x} g(x)\, p_X(x)\right) \cdot \left(\sum_{y} f(y)\, p_Y(y)\right) = E[g(X)] \cdot E[f(Y)]. \qquad \square$$

> **Observação:** O resultado é válido contanto que $E[|g(X)|] < \infty$ e $E[|f(Y)|] < \infty$. A recíproca não vale em geral: $E[g(X)f(Y)] = E[g(X)]E[f(Y)]$ para toda $g,f$ implica independência, mas para funções específicas não.
