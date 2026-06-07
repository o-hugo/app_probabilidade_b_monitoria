---
id: "dantas-cap02-q25"
titulo: "Combinacoes Convexas de Funcoes Densidade"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida"]
referencia: "Dantas, Cap. 2, Q. 25"
---

## Enunciado
Sejam $f_1, f_2, \dots, f_n$ funções densidade de probabilidade em $\mathbb{R}$. Verifique se as funções apresentadas abaixo são funções densidade de probabilidade.
(a) $\alpha f_1(x) + (1 - \alpha) f_2(x)$, $0 < \alpha < 1$.
(b) $f_i(x) + f_j(x)$, $i, j = 1, 2, \dots, n \text{ e } i \neq j$.
(c) $\alpha_1 f_1(x) + \dots + \alpha_n f_n(x)$, $\alpha_i \ge 0$, $i = 1, \dots, n \text{ e } \sum_{i=1}^n \alpha_i = 1$.

## Solução

Para que uma função $g(x)$ seja validada como uma Função Densidade de Probabilidade (f.d.p.), ela precisa satisfazer a dois requisitos matemáticos fundamentais:
1. Ser não negativa em todo o domínio: $g(x) \ge 0, \forall x$.
2. Ter a área sob a curva (a integral na reta inteira) igual a $1$: $\int_{-\infty}^{\infty} g(x) dx = 1$.

Como $f_k(x)$ já são densidades autênticas, nós temos a certeza de que $\int f_k(x)dx = 1$ e $f_k(x) \ge 0$ para qualquer $k$.

- **(a) $g(x) = \alpha f_1(x) + (1 - \alpha) f_2(x)$, com $0 < \alpha < 1$**
1. Como $0 < \alpha < 1$, tanto $\alpha$ quanto $(1-\alpha)$ são maiores que zero. Isso garante que a soma das funções seja sempre não negativa, $g(x) \ge 0$.
2. $\int [\alpha f_1(x) + (1-\alpha)f_2(x)] dx = \alpha \int f_1(x) dx + (1-\alpha) \int f_2(x) dx = \alpha(1) + (1-\alpha)(1) = \alpha + 1 - \alpha = 1$.
**Conclusão: SIM**, é uma densidade de probabilidade (uma mistura estatística simples).

- **(b) $g(x) = f_i(x) + f_j(x)$, com $i \neq j$**
1. A função é certamente não negativa pois soma duas f.d.p.s que são sempre positivas ou nulas.
2. Porém, $\int [f_i(x) + f_j(x)] dx = \int f_i(x) dx + \int f_j(x) dx = 1 + 1 = 2$.
A integral é diferente de 1.
**Conclusão: NÃO**, não é uma densidade de probabilidade.

- **(c) $g(x) = \sum_{k=1}^n \alpha_k f_k(x)$, com $\alpha_k \ge 0$ e $\sum \alpha_k = 1$**
1. Como todos os $\alpha_k \ge 0$ e $f_k(x) \ge 0$, não é possível que a soma combinada resulte num valor negativo. Logo, $g(x) \ge 0$.
2. $\int \left[ \sum \alpha_k f_k(x) \right] dx = \sum \left[ \alpha_k \int f_k(x) dx \right] = \sum [\alpha_k (1)] = \sum \alpha_k$. Como o enunciado impõe que $\sum \alpha_k = 1$, então a integral inteira será 1.
**Conclusão: SIM**, é uma densidade de probabilidade (isso descreve um modelo formal genérico de Mixture de Distribuições).
