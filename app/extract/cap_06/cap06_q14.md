---
id: "dantas-cap06-q14"
titulo: "Intensidade Luminosa I = C/D²"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-fda"]
referencia: "Dantas, Cap. 6, Q. 14"
---

## Enunciado

$I=C/D^2$ onde $C\sim U(1,2)$ e $D$ com $f_D(d)=e^{-d}$, $d\ge 0$, independentes. Determine a densidade de $I$.

## Passo 1: FDA de $I$

$$F_I(t)=P(C/D^2\le t)=P(C\le tD^2)=\int_0^\infty\int_1^2 \mathbf{1}_{c\le td^2}f_C(c)f_D(d)\,dc\,dd.$$

$$= \int_0^\infty e^{-d}\!\left(\int_1^{\min(2,td^2)}\frac{1}{1}\,dc\right)^+\!\!dd.$$

Distinguem-se três regiões em $d$ dependendo de $td^2$ vs. 1 e 2.

## Passo 2: Densidade por diferenciação

Alternativamente, pela condicional:

$$f_I(t)=\int_0^\infty f_{C|D}(td^2\mid d)\cdot |J|\cdot f_D(d)\,dd$$

onde a transformação $C=tD^2$ tem jacobiano $d^2$ em $t$.

Dado $D=d$, $I=C/d^2$, logo $f_{I|D}(t|d)=d^2\cdot f_C(td^2)=d^2\cdot\mathbf{1}_{1\le td^2\le 2}$.

$$f_I(t)=\int_0^\infty d^2\cdot\mathbf{1}_{1/t\le d^2\le 2/t}\cdot e^{-d}\,dd = \int_{1/\sqrt{t}}^{\sqrt{2/t}} d^2 e^{-d}\,dd, \quad t>0.$$

**Resumo:** $f_I(t)=\int_{t^{-1/2}}^{(2/t)^{1/2}} d^2 e^{-d}\,dd$, expressão em forma fechada via integração por partes.
