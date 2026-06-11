---
id: "dantas-cap06-q26"
titulo: "Distribuição Normal Bivariada — Correlação e Independência"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "variancia"]
referencia: "Dantas, Cap. 6, Q. 26"
---

## Enunciado

$(X,Y)$ com densidade normal bivariada:
$$f(x,y)=\frac{1}{2\pi\sigma_x\sigma_y\sqrt{1-\rho^2}}\exp\!\left\{-\frac{1}{2(1-\rho^2)}\!\left[\left(\frac{x-\mu_x}{\sigma_x}\right)^2+\left(\frac{y-\mu_y}{\sigma_y}\right)^2-\frac{2\rho(x-\mu_x)(y-\mu_y)}{\sigma_x\sigma_y}\right]\right\}.$$

(a) Mostre que $\rho$ é o coeficiente de correlação de $X$ e $Y$.
(b) Para que valores de $\rho$, $X$ e $Y$ são independentes?

## Solução

**(a)** As marginais obtidas integrando a normal bivariada são $X\sim N(\mu_x,\sigma_x^2)$ e $Y\sim N(\mu_y,\sigma_y^2)$.

Para calcular $\text{Cov}(X,Y)$, padronize $U=(X-\mu_x)/\sigma_x$ e $V=(Y-\mu_y)/\sigma_y$:

$$E[UV]=\int\!\int uv\cdot f(u,v)\,du\,dv=\rho$$

(integral gaussiana padrão). Portanto $\text{Cov}(X,Y)=\rho\sigma_x\sigma_y$, e

$$\text{Corr}(X,Y)=\frac{\text{Cov}(X,Y)}{\sigma_x\sigma_y}=\rho. \quad\blacksquare$$

**(b)** $X$ e $Y$ são independentes $\Leftrightarrow$ $f(x,y)=f_X(x)f_Y(y)$.

Quando $\rho=0$, o expoente em $f$ separa em soma de termos independentes em $x$ e $y$:

$$f(x,y)\big|_{\rho=0}=\frac{1}{\sigma_x\sqrt{2\pi}}e^{-(x-\mu_x)^2/(2\sigma_x^2)}\cdot\frac{1}{\sigma_y\sqrt{2\pi}}e^{-(y-\mu_y)^2/(2\sigma_y^2)}=f_X(x)f_Y(y).$$

Portanto $X$ e $Y$ são independentes **se e somente se $\rho=0$**.
