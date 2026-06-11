---
id: "dantas-cap05-q22"
titulo: "Esperança como Integral da Cauda de Sobrevivência"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca"]
referencia: "Dantas, Cap. 5, Q. 22"
---

## Enunciado

Seja $X$ variável aleatória não-negativa e contínua. Mostre que:
$$E(X) = \int_0^\infty P(X > t)\,dt.$$

## Solução

$$\int_0^\infty P(X > t)\,dt = \int_0^\infty \int_t^\infty f(x)\,dx\,dt.$$

Invertendo a ordem de integração (região: $0 \le t \le x < \infty$):

$$= \int_0^\infty f(x) \int_0^x dt\,dx = \int_0^\infty f(x)\cdot x\,dx = E(X). \qquad \blacksquare$$
