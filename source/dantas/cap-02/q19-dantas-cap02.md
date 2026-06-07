---
id: "q19-dantas-cap02"
titulo: "Questão 19"
topicos: ["03-modelos-continuos","02-funcao-geradora-momentos"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Definimos a função geradora de probabilidades da variável aleatória X (inteira não-negativa) como sendo: $\varphi_X(t) = E(t^X)$, $t \in \mathbb{R}$. 
(a) Verifique que $\varphi_X(t) = \phi_X(\log t)$ e que $\phi_X(t) = \varphi_X(e^t)$, onde $\phi_X(t)$ é a função geradora de momentos de X. 
(b) Mostre que $\left.\frac{d\varphi_X(t)}{dt}\right|_{t=1} = E(X)$. 
(c) $\left.\frac{d^{(n)}\varphi_X(t)}{dt^{(n)}}\right|_{t=0} = n!P(X=n)$.

## Solução

A função $\varphi_X(t) = E[t^X]$ é usualmente chamada de Função Geradora de Probabilidades (FGP).

- **(a) Relação entre FGP e FGM:**
Sabemos que a FGM é $\phi_X(s) = E[e^{sX}]$. (Usaremos $s$ para não confundir com o $t$ da FGP).
A base exponencial pode ser reescrita usando logaritmos, já que $t = e^{\log t}$. Assim:
$$ \varphi_X(t) = E[t^X] = E\left[ (e^{\log t})^X \right] = E\left[ e^{(\log t)X} \right] $$
O lado direito é exatamente a definição da FGM avaliada no ponto $s = \log t$. Logo:
$$ \varphi_X(t) = \phi_X(\log t) $$
Analogamente, definindo $t = e^s$:
$$ \phi_X(s) = E[e^{sX}] = E\left[ (e^s)^X \right] = \varphi_X(e^s) $$

- **(b) Mostre que a 1ª derivada em $t=1$ é igual a $E(X)$:**
Como $X$ é inteira não-negativa, $\varphi_X(t) = \sum_{x=0}^{\infty} t^x P(X=x)$.
Derivando com respeito a $t$ dentro do operador de esperança (ou somatório):
$$ \frac{d\varphi_X(t)}{dt} = \frac{d}{dt} \sum_{x=0}^{\infty} t^x P(X=x) = \sum_{x=0}^{\infty} \left(\frac{d}{dt} t^x\right) P(X=x) $$
$$ \frac{d\varphi_X(t)}{dt} = \sum_{x=1}^{\infty} x t^{x-1} P(X=x) $$
(O termo $x=0$ desaparece porque a derivada de uma constante é 0).
Avaliando a derivada em $t = 1$:
$$ \left.\frac{d\varphi_X(t)}{dt}\right|_{t=1} = \sum_{x=1}^{\infty} x (1)^{x-1} P(X=x) = \sum_{x=1}^{\infty} x P(X=x) = E(X) $$

- **(c) Mostre que a n-ésima derivada em $t=0$ é igual a $n!P(X=n)$:**
Tomando a n-ésima derivada do polinômio $t^x$:
Se derivarmos $\varphi_X(t)$ repetidas $n$ vezes, o termo genérico $t^x$ se torna $x(x-1)\cdots(x-n+1)t^{x-n}$.
$$ \frac{d^n \varphi_X(t)}{dt^n} = \sum_{x=n}^{\infty} x(x-1)\cdots(x-n+1) t^{x-n} P(X=x) $$
(Os termos onde $x < n$ se anulam e desaparecem ao longo das derivadas).
Agora, avaliamos toda a soma no ponto $t = 0$.
Para qualquer termo onde $x > n$, teremos $0$ elevado a uma potência positiva, resultando em $0$.
O único termo da soma infinita que "sobrevive" é aquele onde $x = n$, pois a potência de $t$ fica $t^{n-n} = t^0 = 1$.
$$ \left.\frac{d^n \varphi_X(t)}{dt^n}\right|_{t=0} = n(n-1)\cdots(n-n+1) (1) P(X=n) $$
$$ \left.\frac{d^n \varphi_X(t)}{dt^n}\right|_{t=0} = n! P(X=n) $$
