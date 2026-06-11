---
id: "dantas-cap06-q19"
titulo: "Coordenadas Polares de Normal Bivariada Padrão"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano", "fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 19"
---

## Enunciado

$(X,Y)$ com $X,Y\sim N(0,1)$ independentes. Determine a densidade conjunta das coordenadas polares $R=\sqrt{X^2+Y^2}$ e $\Theta=\text{arctg}(Y/X)$.

## Passo 1: Jacobiano

$X=R\cos\Theta$, $Y=R\sin\Theta$. Jacobiano da transformação inversa:

$$|J|=\begin{vmatrix}\cos\theta & -r\sin\theta\\\sin\theta & r\cos\theta\end{vmatrix}=r.$$

## Passo 2: Densidade conjunta de $(R,\Theta)$

$$f_{R,\Theta}(r,\theta)=f_X(r\cos\theta)f_Y(r\sin\theta)\cdot r = \frac{1}{2\pi}e^{-r^2/2}\cdot r, \quad r>0,\ \theta\in[0,2\pi).$$

## Passo 3: Independência e marginais

A densidade fatora:

$$f_{R,\Theta}(r,\theta)=\underbrace{re^{-r^2/2}}_{f_R(r)}\cdot\underbrace{\frac{1}{2\pi}}_{f_\Theta(\theta)}.$$

- $\Theta\sim U(0,2\pi)$.
- $R$ tem densidade $f_R(r)=re^{-r^2/2}$, $r>0$ — distribuição de Rayleigh (ou $R^2\sim\text{Exp}(1/2)$).
- $R$ e $\Theta$ são **independentes**.

(Fundamento do método de Box-Muller.)
