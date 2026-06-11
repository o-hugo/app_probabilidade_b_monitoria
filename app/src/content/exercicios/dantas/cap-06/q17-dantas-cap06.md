---
id: "dantas-cap06-q17"
titulo: "Densidade Conjunta de X+Y e 3X+2Y"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano"]
referencia: "Dantas, Cap. 6, Q. 17"
---

## Enunciado

$X,Y$ independentes, $f(x)=e^{-x}$ para $x>0$. Obtenha a densidade conjunta de $U=X+Y$ e $V=3X+2Y$. $U$ e $V$ são independentes?

## Passo 1: Inversão

$U=X+Y$, $V=3X+2Y$. Resolvendo: $X=V-2U$, $Y=3U-V$.

Condições: $X>0\Rightarrow V>2U$; $Y>0\Rightarrow V<3U$.

$$J=\begin{vmatrix}-2&1\\3&-1\end{vmatrix}=2-3=-1,\quad |J|=1.$$

## Passo 2: Densidade conjunta

$$f_{U,V}(u,v)=f_X(v-2u)f_Y(3u-v)\cdot|J|=e^{-(v-2u)}e^{-(3u-v)}=e^{-u},$$
para $2u<v<3u$, $u>0$.

## Passo 3: Independência

$f_{U,V}(u,v)=e^{-u}$ não fatora em $g(u)h(v)$ isoladamente (o suporte depende de ambas), logo **$U$ e $V$ não são independentes**.

**Resumo:** $f_{U,V}(u,v)=e^{-u}$ para $2u<v<3u$, $u>0$. $U$ e $V$ não são independentes.
