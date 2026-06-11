---
id: "dantas-cap06-q25"
titulo: "Transformação Linear de Densidade Conjunta — Matriz A"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano"]
referencia: "Dantas, Cap. 6, Q. 25"
---

## Enunciado

$X_1,\ldots,X_n$ com densidade conjunta $f$. $Y_i=\sum_j a_{ij}X_j$, $A=(a_{ij})$ com $\det A\ne 0$.

(a) Mostre que $f_{Y_1,\ldots,Y_n}(y_1,\ldots,y_n)=\dfrac{1}{|\det A|}f(x_1,\ldots,x_n)$.

(b) Determine a distribuição de $X_1,\ldots,X_n$ sabendo que $X_1,X_2-X_1,\ldots,X_n-X_{n-1}$ são i.i.d. $N(0,1)$.

## Solução

**(a)** A transformação $\mathbf{Y}=A\mathbf{X}$ é bijetora ($\det A\ne 0$) com inversa $\mathbf{X}=A^{-1}\mathbf{Y}$. O jacobiano da transformação $\mathbf{Y}\to\mathbf{X}$ é $|\det A^{-1}|=1/|\det A|$.

Pela fórmula de mudança de variáveis:
$$f_\mathbf{Y}(\mathbf{y})=f_\mathbf{X}(A^{-1}\mathbf{y})\cdot|\det A^{-1}|=\frac{1}{|\det A|}f(x_1,\ldots,x_n). \quad\blacksquare$$

**(b)** Defina $Z_1=X_1$, $Z_i=X_i-X_{i-1}$ ($i=2,\ldots,n$) — i.i.d. $N(0,1)$.

Então $X_k=\sum_{i=1}^k Z_i$. A matriz $A$ que expressa $\mathbf{Z}=A\mathbf{X}$ é triangular inferior com uns na diagonal, $\det A=1$.

Por (a): $f_\mathbf{X}(\mathbf{x})=f_\mathbf{Z}(A\mathbf{x})$.

$$f_\mathbf{X}(\mathbf{x})=\prod_{i=1}^n\frac{1}{\sqrt{2\pi}}e^{-z_i^2/2}=\frac{1}{(2\pi)^{n/2}}\exp\!\left\{-\frac{1}{2}\sum_{i=1}^n z_i^2\right\},$$

onde $z_1=x_1$, $z_i=x_i-x_{i-1}$. Esta é a densidade de um **processo de passeio aleatório gaussiano**.
