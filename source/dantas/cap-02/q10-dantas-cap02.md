---
id: "q10-dantas-cap02"
titulo: "Questão 10"
topicos: ["03-modelos-continuos","05-funcao-de-variavel-aleatoria"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Demonstre a generalização do resultado apresentado no lema 2.5.2, isto é, se $X_1, \dots, X_n$ são variáveis aleatórias com esperança finita e $\alpha_1, \dots, \alpha_n$ constantes reais, mostre que 
$E\left[\sum_{i=1}^n \alpha_i X_i\right] = \sum_{i=1}^n \alpha_i E[X_i]$.

## Solução

A propriedade estabelecida no Lema 2.5.2 atesta a linearidade do operador de Esperança Matemática para a soma ponderada de duas variáveis aleatórias. Ou seja, sabemos que:
$$ E[aX + bY] = aE[X] + bE[Y] $$
para quaisquer variáveis $X, Y$ e constantes $a, b$.

A generalização para $n$ variáveis é provada facilmente utilizando o **Princípio da Indução Matemática**.

1. **Base da Indução ($n=2$):**
A propriedade para $n=2$ já é verdadeira e dada pelo Lema 2.5.2:
$$ E[\alpha_1 X_1 + \alpha_2 X_2] = \alpha_1 E[X_1] + \alpha_2 E[X_2] $$

2. **Hipótese de Indução:**
Supomos que a igualdade seja verdadeira para um inteiro arbitrário $k = n - 1$. Isto é, assumimos como verdade que:
$$ E\left[\sum_{i=1}^{n-1} \alpha_i X_i\right] = \sum_{i=1}^{n-1} \alpha_i E[X_i] $$

3. **Passo Indutivo:**
Queremos mostrar que a propriedade também vale para $n$.
O somatório de $n$ termos pode ser reescrito separando o último termo dos demais:
$$ \sum_{i=1}^n \alpha_i X_i = \left(\sum_{i=1}^{n-1} \alpha_i X_i\right) + \alpha_n X_n $$
Aplicando o operador de esperança $E[\cdot]$ em ambos os lados:
$$ E\left[\sum_{i=1}^n \alpha_i X_i\right] = E\left[ \left(\sum_{i=1}^{n-1} \alpha_i X_i\right) + \alpha_n X_n \right] $$
Agora, notamos que a expressão interna é a soma de *duas* variáveis aleatórias: uma é $Y = \sum_{i=1}^{n-1} \alpha_i X_i$ e a outra é $W = \alpha_n X_n$.
Pela linearidade para duas variáveis (Base da Indução):
$$ E[Y + W] = E[Y] + E[W] $$
$$ E\left[\sum_{i=1}^n \alpha_i X_i\right] = E\left[\sum_{i=1}^{n-1} \alpha_i X_i\right] + E[\alpha_n X_n] $$
Pela propriedade da constante e pela Hipótese de Indução aplicada no primeiro termo, substituímos:
$$ E\left[\sum_{i=1}^n \alpha_i X_i\right] = \left(\sum_{i=1}^{n-1} \alpha_i E[X_i]\right) + \alpha_n E[X_n] $$
Ao juntarmos o último termo de volta ao somatório, obtemos:
$$ E\left[\sum_{i=1}^n \alpha_i X_i\right] = \sum_{i=1}^n \alpha_i E[X_i] $$

Logo, por indução, a propriedade está validada para qualquer valor inteiro $n \ge 1$.
