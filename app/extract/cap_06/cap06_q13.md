---
id: "dantas-cap06-q13"
titulo: "Potência Elétrica W = RI²"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano", "esperanca", "probabilidade"]
referencia: "Dantas, Cap. 6, Q. 13"
---

## Enunciado

$W=RI^2$ onde $I$ e $R$ independentes, $f_I(x)=6x(1-x)$ e $f_R(x)=2x$ para $0\le x\le 1$. Determine: (a) a fdp de $W$; (b) $E(W)$; (c) $P(W>0{,}5)$.

## Passo 1: Item (b) — $E(W)$

Por independência: $E(W)=E(R)E(I^2)$.

$$E(R)=\int_0^1 2x^2\,dx=\frac{2}{3},\quad E(I^2)=\int_0^1 x^2\cdot 6x(1-x)dx=6\!\int_0^1(x^3-x^4)dx=6\!\left(\frac{1}{4}-\frac{1}{5}\right)=\frac{3}{10}.$$

$$E(W)=\frac{2}{3}\cdot\frac{3}{10}=\frac{1}{5}.$$

## Passo 2: Item (a) — fdp de $W$

Para $w\in(0,1)$:

$$F_W(w)=P(RI^2\le w)=\int_0^1\int_0^1 \mathbf{1}_{ri^2\le w}f_R(r)f_I(i)\,dr\,di.$$

Dado $I=i$: $R\le w/i^2$ (se $w/i^2<1$, i.e., $i>\sqrt{w}$); caso contrário a condição é sempre satisfeita.

$$F_W(w)=\int_0^{\sqrt{w}} f_I(i)di + \int_{\sqrt{w}}^1\!\left(\int_0^{w/i^2}2r\,dr\right)f_I(i)di = F_I(\sqrt{w})+\int_{\sqrt{w}}^1 \frac{w^2}{i^4}\cdot 6i(1-i)di.$$

Diferenciando em relação a $w$ obtém-se $f_W(w)$.

## Passo 3: Item (c) — $P(W>0{,}5)$

$$P(W>0{,}5)=1-F_W(0{,}5)\approx 1-\int\ldots$$

(Cálculo numérico recomendado por integração direta.)
