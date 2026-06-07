---
id: "q37-dantas-cap02"
titulo: "Questão 37"
topicos: ["03-modelos-continuos","05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Suponha que a densidade da variável aleatória X é dada por $f(x) = \lambda e^{-\lambda x}$ para $x \ge 0$. Seja Y a variável aleatória inteira definida por $Y = m$, se $m < X \le m + 1$, onde m é inteiro não-negativo. 
(a) Obtenha a distribuição de Y. 
(b) Escreva $P(Y = m)$ da forma $P(Y = m) = p^m(1 - p)$, para algum p, $0 < p < 1$. Que distribuição é esta?

## Solução

A variável de origem $X$ tem distribuição Exponencial com parâmetro $\lambda$.

- **(a) Obtenha a distribuição de Y:**
A variável $Y$ mapeia intervalos contínuos de comprimento 1 em números inteiros. 
Para achar a probabilidade de $Y$ assumir o valor inteiro $m$, precisamos integrar a densidade de probabilidade de $X$ no intervalo específico correspondente a esse $m$:
$$ P(Y = m) = P(m < X \le m+1) = \int_{m}^{m+1} \lambda e^{-\lambda x} dx $$
Resolvendo a integral:
$$ P(Y = m) = \left[ -e^{-\lambda x} \right]_m^{m+1} $$
$$ P(Y = m) = (-e^{-\lambda (m+1)}) - (-e^{-\lambda m}) $$
Reorganizando:
$$ P(Y = m) = e^{-\lambda m} - e^{-\lambda(m+1)} $$
Fatorando $e^{-\lambda m}$:
$$ P(Y = m) = e^{-\lambda m} \left( 1 - e^{-\lambda} \right) $$
Essa fórmula é válida para qualquer inteiro não-negativo $m \in \{0, 1, 2, \dots\}$.

- **(b) Conversão para $p^m(1 - p)$ e identificação da distribuição:**
Observe a equação do item anterior: $e^{-\lambda m} \left( 1 - e^{-\lambda} \right)$.
Podemos aplicar propriedades de potenciação: $e^{-\lambda m} = (e^{-\lambda})^m$.
Se definirmos uma nova constante $p$ tal que $p = e^{-\lambda}$, a expressão torna-se:
$$ P(Y = m) = p^m (1 - p) $$
Sendo $\lambda > 0$, a exponencial $e^{-\lambda}$ sempre resultará em um valor estritamente entre 0 e 1, portanto, a condição $0 < p < 1$ está assegurada.
Esta expressão descreve a **Distribuição Geométrica** (modelando o número de falhas sucessivas $m$ antes do primeiro sucesso, onde a probabilidade de falha é $p$ e a de sucesso é $1-p$). 
*(Nota: dependendo da definição formal, a distribuição geométrica pode descrever as tentativas ou as falhas. Aqui, modela o número de intervalos inteiros passados antes do evento contínuo ocorrer).*
