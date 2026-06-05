---
id: "05-funcao-de-variavel-aleatoria"
titulo: "Função de Variável Aleatória Contínua"
ordem: 5
ementa_ref: "Função de variável aleatória contínua"
tags: ["transformacoes", "metodo-fda", "jacobiano"]
---

# Função de Variável Aleatória Contínua

Se conhecemos a FDP de $X$, podemos frequentemente querer encontrar a FDP de uma função ou transformação de $X$, como $Y = g(X)$. Existem diferentes métodos para realizar essa conversão de probabilidade, dependendo da natureza de $g(x)$.

## O Método da Transformação pela FDA

Este é o método mais fundamental e robusto, consistindo em dois passos:
1. Expressar a FDA de $Y$, que é $F_Y(y) = P(Y \le y)$, em termos de eventos relacionados à variável $X$.
2. Diferenciar a $F_Y(y)$ em relação a $y$ para obter a FDP correspondente $f_Y(y)$.

Por exemplo, se $Y = X^2$, então:
$F_Y(y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$.
Derivando com regra da cadeia, obtemos $f_Y(y)$.

## Transformações Monotônicas (Jacobiano)

Se a função $y = g(x)$ for estritamente **crescente** ou estritamente **decrescente** sobre o suporte de $X$, podemos aplicar diretamente o teorema da mudança de variáveis. Nesse caso, a função possui inversa única $x = g^{-1}(y) = h(y)$. A FDP de $Y$ é dada por:

$$f_Y(y) = f_X(h(y)) \left| \frac{dh(y)}{dy} \right|$$

> "O termo $\left| \frac{dh(y)}{dy} \right|$ é o valor absoluto do Jacobiano da transformação."
> -- Morettin & Bussab (2010). Estatística Básica. p. 185.

## Usabilidade e Aplicações

A habilidade de transformar variáveis e determinar a distribuição resultante é essencial na modelagem e inferência:
- **Transformada Integral de Probabilidade e Simulação:** Qualquer função de distribuição contínua pode ser gerada se $Y = F_X^{-1}(U)$ onde $U \sim U(0,1)$. Esta técnica é a base principal dos algoritmos computacionais para gerar números pseudo-aleatórios seguindo qualquer distribuição que possua uma FDA analiticamente inversível.
- **Deduções em Inferência Estatística:** Permite descobrir e justificar as distribuições exatas associadas a estimadores ou estatísticas de testes (como as distribuições $t$ de Student e Qui-Quadrado derivadas a partir de transformações de distribuições normais).
