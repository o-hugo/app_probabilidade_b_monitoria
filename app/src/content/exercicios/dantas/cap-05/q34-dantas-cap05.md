---
id: "dantas-cap05-q34"
titulo: "Densidade de Y = |X| com X ~ U(-1,1)"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "f_Y(y) = 1, 0 < y < 1"
tags: ["metodo-fda"]
referencia: "Dantas, Cap. 5, Q. 34"
---

## Enunciado

$X \sim U(-1,1)$. Determine a densidade de $Y = |X|$.

## Solução

Para $0 < y < 1$:

$$F_Y(y) = P(|X| \le y) = P(-y \le X \le y) = \frac{2y}{2} = y.$$

Derivando: $f_Y(y) = 1$, $0 < y < 1$.

Portanto $Y \sim U(0,1)$. Intuitivamente, a simetria de $U(-1,1)$ em torno de 0 faz com que $|X|$ seja uniforme em $(0,1)$.
