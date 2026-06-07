---
id: "questoes-q21-livro-exemplo-244"
titulo: "Exemplo 2.4.4"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["confiabilidade", "esperanca"]
referencia: "Dantas, Ex. 2.4.4"
---

## Enunciado

Considere uma variável aleatória cuja densidade de probabilidade é dada por: $f(x)=0$ para $x\le0$ e $f(x)=2e^{-2x}$ para $x>0$. Determinar a função de distribuição de X e calcular $P[0,5<X<2]$.

## Solução

## Passo 1: Identificar a Distribuição

A fdp $f(x) = \lambda e^{-\lambda x}$ para $x>0$ é a da distribuição Exponencial. Neste caso, o parâmetro $\lambda=2$.



## Passo 2: Calcular a FDA

Para $x>0$, a FDA é:

$$F(x) = \int_0^x 2e^{-2t}\,dt = 2 [\frac{e^{-2t}}{-2}]_0^x = [-e^{-2t}]_0^x$$

$$= (-e^{-2x}) - (-e^0) = -e^{-2x} - (-1) = 1 - e^{-2x}$$

A FDA completa é $F(x) = 1 - e^{-2x}$ para $x>0$ e $F(x)=0$ para $x \le 0$.

Resumo: Integramos a fdp exponencial de 0 a x para encontrar a fórmula geral da sua FDA.



## Passo 3: Calcular $P[0,5<X<2]$

Usamos a propriedade $P[a < X < b] = F(b) - F(a)$.

$$P[0,5<X<2] = F(2) - F(0.5)$$

$$= (1 - e^{-2(2)}) - (1 - e^{-2(0.5)}) = (1 - e^{-4}) - (1 - e^{-1})$$

$$= 1 - e^{-4} - 1 + e^{-1} = e^{-1} - e^{-4}$$

Numericamente, isso é aproximadamente $0.3678 - 0.0183 = 0.3495$.

Resumo: Aplicamos a propriedade da FDA para encontrar a probabilidade no intervalo desejado.
