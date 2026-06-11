---
id: "dantas-cap02-q08"
titulo: "FDP Cosseno: Constante e Probabilidade"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "probabilidade"]
referencia: "Dantas, Cap. 2, Q. 8"
---

## Enunciado
Considere a variável aleatória cuja função densidade de probabilidade é: $f(x) = c\cdot\cos(x), \frac{\pi}{2} \le x \le \pi, \text{ e } f(x) = 0$ caso contrário. 
(a) Determine o valor de $c$. 
(b) Calcule $P(X < \frac{3\pi}{4})$.

## Solução

- **(a) Determine o valor de $c$:**
A área sob a curva deve ser igual a 1.
$$ \int_{\pi/2}^{\pi} c \cdot \cos(x) \, dx = 1 $$
A integral de $\cos(x)$ é $\sin(x)$.
$$ c \left[ \sin(x) \right]_{\pi/2}^{\pi} = 1 $$
$$ c \left( \sin(\pi) - \sin\left(\frac{\pi}{2}\right) \right) = 1 $$
$$ c (0 - 1) = 1 \implies -c = 1 \implies c = -1 $$
A densidade é $f(x) = -\cos(x)$. 
*(Nota: Lembre-se que no segundo quadrante, entre $\pi/2$ e $\pi$, a função cosseno é negativa. Sendo $c = -1$, garantimos que $f(x) \ge 0$, uma exigência para qualquer densidade de probabilidade).*

- **(b) Calcule $P(X < \frac{3\pi}{4})$:**
Devemos integrar a densidade desde o limite inferior ($\pi/2$) até $\frac{3\pi}{4}$:
$$ P(X < \frac{3\pi}{4}) = \int_{\pi/2}^{3\pi/4} (-\cos(x)) \, dx $$
A integral de $-\cos(x)$ é $-\sin(x)$.
$$ P(X < \frac{3\pi}{4}) = \left[ -\sin(x) \right]_{\pi/2}^{3\pi/4} $$
$$ P(X < \frac{3\pi}{4}) = -\sin\left(\frac{3\pi}{4}\right) - \left(-\sin\left(\frac{\pi}{2}\right)\right) $$
Lembrando que $\sin(\frac{3\pi}{4}) = \frac{\sqrt{2}}{2}$ e $\sin(\frac{\pi}{2}) = 1$:
$$ P(X < \frac{3\pi}{4}) = -\frac{\sqrt{2}}{2} - (-1) = 1 - \frac{\sqrt{2}}{2} \approx 0,2929 $$
