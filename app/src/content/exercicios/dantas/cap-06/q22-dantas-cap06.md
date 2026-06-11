---
id: "dantas-cap06-q22"
titulo: "Transformação Box-Muller"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano", "fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 22"
---

## Enunciado

$U\sim U(0,2\pi)$ e $Z\sim\text{Exp}(1)$, independentes. Mostre que $X=\sqrt{2Z}\cos U$ e $Y=\sqrt{2Z}\sin U$ são independentes, cada uma $N(0,1)$.

## Passo 1: Inversão e Jacobiano

$Z=(X^2+Y^2)/2$, $U=\text{arctg}(Y/X)$. Jacobiano inverso (de $(X,Y)$ para $(Z,U)$):

$$|J_{(X,Y)\to(Z,U)}|=\frac{1}{|J_{(Z,U)\to(X,Y)}|}.$$

Calculando $|J_{(Z,U)\to(X,Y)}|$:
$$\frac{\partial(x,y)}{\partial(z,u)}=\begin{pmatrix}\cos u/\sqrt{2z}&-\sqrt{2z}\sin u\\\sin u/\sqrt{2z}&\sqrt{2z}\cos u\end{pmatrix}, \quad |J|=\cos^2u+\sin^2u=1.$$

Logo $|J_{(X,Y)\to(Z,U)}|=1$.

## Passo 2: Densidade conjunta de $(X,Y)$

$$f_{X,Y}(x,y)=f_Z(z)f_U(u)\cdot|J_{(Z,U)\to(X,Y)}|=e^{-z}\cdot\frac{1}{2\pi}\cdot 1=\frac{1}{2\pi}e^{-(x^2+y^2)/2}.$$

## Passo 3: Independência e marginalização

$$f_{X,Y}(x,y)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\cdot\frac{1}{\sqrt{2\pi}}e^{-y^2/2}=f_X(x)f_Y(y).$$

Portanto $X\sim N(0,1)$, $Y\sim N(0,1)$ e são **independentes**. $\blacksquare$
