---
id: "questoes-q23-livro-exemplo-281-cauchy"
titulo: "Exemplo 2.8.1 (Cauchy)"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca"]
referencia: "Dantas, Ex. 2.8.1"
---

## Enunciado

Seja X uma variável aleatória com distribuição de Cauchy, isto é, cuja densidade de probabilidade é dada por: $f(x)=\frac{1}{\pi}\frac{1}{1+x^{2}}$ para $-\infty<x<\infty$. Mostre que sua esperança não existe (é infinita).

## Solução

## Passo 1: Condição para a Existência da Esperança

Para que a esperança $E(X) = \int_{-\infty}^{\infty} xf(x)\,dx$ exista, a integral de seu valor absoluto, $E(|X|) = \int_{-\infty}^{\infty} |x|f(x)\,dx$, deve ser finita.

Resumo: A existência da esperança requer convergência absoluta da integral.



## Passo 2: Montar a Integral para $E(|X|)$

$$E(|X|) = \int_{-\infty}^{\infty} \frac{|x|}{\pi(1+x^2)}\,dx$$

Como o integrando $|x|/(1+x^2)$ é uma função par, podemos simplificar a integral:

$$E(|X|) = 2 \int_{0}^{\infty} \frac{x}{\pi(1+x^2)}\,dx = \frac{2}{\pi} \lim_{a \to \infty} \int_{0}^{a} \frac{x}{1+x^2}\,dx$$

Resumo: Usamos a simetria da função para simplificar o cálculo da integral imprópria.



## Passo 3: Resolver a Integral

Usamos a substituição $u = 1+x^2$, então $du=2x\,dx$, ou $x\,dx = du/2$.

$$\int \frac{x}{1+x^2}\,dx = \int \frac{1}{u} \frac{du}{2} = \frac{1}{2} \ln|u| = \frac{1}{2} \ln(1+x^2)$$

Agora, aplicamos os limites de integração:

$$E(|X|) = \frac{2}{\pi} \lim_{a \to \infty} [\frac{1}{2} \ln(1+x^2)]_0^a = \frac{1}{\pi} \lim_{a \to \infty} (\ln(1+a^2) - \ln(1))$$

$$= \frac{1}{\pi} \lim_{a \to \infty} (\ln(1+a^2)) = \infty$$

Como a integral de $|x|f(x)$ diverge, a esperança $E(X)$ não existe.

Resumo: A integral da primitiva resulta em um logaritmo que tende ao infinito, provando que a esperança não é finita.
