---
id: "dantas-cap06-q18"
titulo: "Normal Bivariada para Coordenadas U=X²+Y² e V=X/Y"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano"]
referencia: "Dantas, Cap. 6, Q. 18"
---

## Enunciado

$X,Y$ i.i.d. $N(0,1)$. Ache a distribuição de $(U,V)$ onde $U=X^2+Y^2$ e $V=X/Y$. $U$ e $V$ são independentes?

## Passo 1: Jacobiano

Relação inversa: $X^2=UV^2/(1+V^2)$ — não é direto. Usamos $X=r\cos\theta$, $Y=r\sin\theta$ com $r^2=U$, $\tan\theta=1/V$.

Alternativamente: $(U,V)$, com jacobiano calculado diretamente.

$X=\sqrt{U}\cdot V/\sqrt{1+V^2}$, $Y=\sqrt{U}/\sqrt{1+V^2}$.

$$|J|=\frac{1}{2(1+V^2)}.$$

## Passo 2: Densidade conjunta

$$f_{U,V}(u,v)=f_X(x)f_Y(y)|J|=\frac{1}{2\pi}e^{-u/2}\cdot\frac{1}{2(1+v^2)}, \quad u>0,\ v\in\mathbb{R}.$$

A densidade fatora: $f_{U,V}(u,v)=f_U(u)\cdot f_V(v)$ com:

$$f_U(u)=\frac{1}{2}e^{-u/2} \implies U\sim\text{Exp}(1/2)=\chi^2(2).$$

$$f_V(v)=\frac{1}{\pi(1+v^2)} \implies V\sim\text{Cauchy}(0,1).$$

**$U$ e $V$ são independentes.** $\blacksquare$
