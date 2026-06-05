---
id: "lista02-q35-distribuio-de-a-sin"
titulo: "Distribuição de A sin(θ)"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Ache a distribuição de $R=A \sin\theta$, onde A é constante e $\theta \sim U(-\pi/2, \pi/2)$.

## Solução

A FDP de $\theta$ é $f_\theta(\theta) = \frac{1}{\pi/2 - (-\pi/2)} = 1/\pi$ para $\theta \in (-\pi/2, \pi/2)$.<br>O intervalo de R é $(-A, A)$.<br>Método da transformação: $r = g(\theta) = A\sin\theta$. Inversa: $\theta = g^{-1}(r) = \arcsin(r/A)$.<br>Derivada: $\frac{d\theta}{dr} = \frac{1}{\sqrt{1-(r/A)^2}} \cdot \frac{1}{A} = \frac{1}{\sqrt{A^2 - r^2}}$.<br>$f_R(r) = f_\theta(g^{-1}(r)) |\frac{d\theta}{dr}| = \frac{1}{\pi} \frac{1}{\sqrt{A^2-r^2}}$, para $r \in (-A, A)$. Esta é uma distribuição Arco-Seno escalada.
