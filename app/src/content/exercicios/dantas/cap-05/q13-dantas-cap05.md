---
id: "dantas-cap05-q13"
titulo: "Localização Ótima do Corpo de Bombeiros"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "a = A/2"
tags: ["esperanca"]
referencia: "Dantas, Cap. 5, Q. 13"
---

## Enunciado

Incêndios ocorrem uniformemente em $(0, A)$. Determine $a$ que minimiza $E[|X - a|]$.

## Solução

Para $X \sim U(0, A)$:

$$E[|X-a|] = \frac{1}{A}\int_0^A |x-a|\,dx = \frac{1}{A}\left[\int_0^a (a-x)\,dx + \int_a^A (x-a)\,dx\right]$$

$$= \frac{1}{A}\left[\frac{a^2}{2} + \frac{(A-a)^2}{2}\right].$$

Derivando em $a$ e igualando a zero:

$$\frac{d}{da}E[|X-a|] = \frac{1}{A}[a - (A-a)] = \frac{2a - A}{A} = 0 \implies a = \frac{A}{2}.$$

Como $d^2/da^2 > 0$, este é um mínimo. O corpo de bombeiros deve ser instalado no **meio** da estrada ($a = A/2$), o que coincide com a mediana de $X \sim U(0,A)$.
