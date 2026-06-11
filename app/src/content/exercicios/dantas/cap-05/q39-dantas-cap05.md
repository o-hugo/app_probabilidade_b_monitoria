---
id: "dantas-cap05-q39"
titulo: "Transformação Gama → Qui-Quadrado"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "metodo-jacobiano"]
referencia: "Dantas, Cap. 5, Q. 39"
---

## Enunciado

$X \sim \text{Gama}(\alpha, \beta)$. $Z = 2\beta X$. Determine $f_Z(z)$ para $2\alpha \in \mathbb{N}$. Qual a distribuição de $Z$ para $\alpha = 1/2$?

## Solução

**Método da FDA:** $F_Z(z) = P(2\beta X \le z) = P(X \le z/(2\beta)) = F_X(z/(2\beta))$.

$$f_Z(z) = \frac{1}{2\beta}f_X\!\left(\frac{z}{2\beta}\right) = \frac{1}{2\beta}\cdot\frac{1}{\beta^\alpha\Gamma(\alpha)}\left(\frac{z}{2\beta}\right)^{\alpha-1}e^{-z/(2\beta^2)\cdot\beta} = \frac{1}{2^\alpha\Gamma(\alpha)}z^{\alpha-1}e^{-z/2}, \quad z>0.$$

Reconhecemos: $f_Z(z) = \frac{1}{2^\alpha\Gamma(\alpha)}z^{\alpha-1}e^{-z/2}$, que é a densidade **Gama$(\alpha, 2)$** = **qui-quadrado** com $\nu = 2\alpha$ graus de liberdade.

**Para $\alpha = 1/2$:** $Z \sim \chi^2(1)$ (qui-quadrado com 1 grau de liberdade — mesmo resultado do Q38).
