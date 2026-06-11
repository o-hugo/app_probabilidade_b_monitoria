---
id: "dantas-cap03-q44"
titulo: "Modelo de Ehrenfest: Equilíbrio Térmico"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
resposta_final: "lim E[X_n] = 1/2"
tags: ["esperanca", "condicional"]
referencia: "Dantas, Cap. 3, Q. 44"
---

## Enunciado

$k$ bolas numeradas distribuídas entre urna I e urna II. A cada passo: sorteia-se um número em $\{1,\ldots,k\}$ e transfere-se a bola sorteada para a outra urna. $X_n$ = proporção de bolas na urna I após o $n$-ésimo passo. $X$ = proporção inicial.

**(a)** Determine $E[X_n]$ expressando em função de $E[X_{n-1}]$.

**(b)** Verifique que $\lim_{n\to\infty} E[X_n] = \frac{1}{2}$ para toda configuração inicial.

## Passo 1: Item (a) — Recorrência para $E[X_n]$

Condicione em $X_{n-1}$. Se há $j = kX_{n-1}$ bolas na urna I, então:
- Com prob $j/k = X_{n-1}$: a bola sorteada está na urna I → vai para a II. Urna I fica com $j-1$ bolas: $X_n = (j-1)/k = X_{n-1} - 1/k$.
- Com prob $1 - X_{n-1}$: a bola sorteada está na urna II → vai para a I. Urna I fica com $j+1$ bolas: $X_n = X_{n-1} + 1/k$.

Portanto:

$$E[X_n \mid X_{n-1}] = X_{n-1}\!\left(X_{n-1} - \frac{1}{k}\right) + (1-X_{n-1})\!\left(X_{n-1} + \frac{1}{k}\right)$$

$$= X_{n-1} - \frac{X_{n-1}}{k} + \frac{1-X_{n-1}}{k} = X_{n-1} + \frac{1-2X_{n-1}}{k} = X_{n-1}\!\left(1 - \frac{2}{k}\right) + \frac{1}{k}.$$

Tomando a esperança:

$$E[X_n] = \left(1 - \frac{2}{k}\right) E[X_{n-1}] + \frac{1}{k}.$$

**Resumo:** $E[X_n] = (1-2/k)E[X_{n-1}] + 1/k$ — recorrência linear de primeira ordem.

## Passo 2: Item (b) — Limite quando $n \to \infty$

Seja $r = 1 - 2/k \in (-1, 1)$ para $k \geq 2$. A recorrência $a_n = r\,a_{n-1} + 1/k$ tem ponto fixo $a^* = (1/k)/(1-r) = (1/k)/(2/k) = 1/2$.

A solução geral é $E[X_n] = 1/2 + (E[X_0] - 1/2) r^n$.

Como $|r| < 1$, temos $r^n \to 0$, portanto:

$$\lim_{n \to \infty} E[X_n] = \frac{1}{2},$$

independentemente da proporção inicial $E[X_0] = X$. $\blacksquare$

**Interpretação:** A longo prazo, a proporção esperada de bolas na urna I converge para $1/2$ — analogamente ao equilíbrio térmico entre dois corpos isolados.

**Resumo:** $|r| < 1$ garante convergência geométrica para o equilíbrio $1/2$.
