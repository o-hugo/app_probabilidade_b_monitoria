---
id: "dantas-cap02-q14"
titulo: "Variancia de Soma de Variaveis Aleatorias Dependentes"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["variancia"]
referencia: "Dantas, Cap. 2, Q. 14"
---

## Enunciado
Considere dois lançamentos consecutivos de um dado que suporemos equilibrado. Sejam 
$X$: número de vezes em que é obtida a face 1, $x=0,1,2$. 
$Y$: número de vezes em que é obtida a face 6, $y=0,1,2$. 
$Z = X + Y$: número de vezes em que aparece ou uma face 1 ou uma face 6, $z=0,1,2$. 
Determine: $\text{Var}(X)$, $\text{Var}(Y)$ e $\text{Var}(Z)$.
É verdade que $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$?

## Solução

Temos o lançamento de 2 dados independentes.

- **$\text{Var}(X)$:** 
$X$ conta o número de sucessos ("obter a face 1") em $n=2$ lançamentos, logo segue uma distribuição Binomial: $X \sim \text{Bin}(2, \frac{1}{6})$.
A variância de uma binomial é dada por $np(1-p)$.
$$ \text{Var}(X) = 2 \times \frac{1}{6} \times \left(1 - \frac{1}{6}\right) = 2 \times \frac{1}{6} \times \frac{5}{6} = \frac{10}{36} = \frac{5}{18} $$

- **$\text{Var}(Y)$:** 
$Y$ conta o número de sucessos ("obter a face 6") nos mesmos 2 lançamentos. A probabilidade é a mesma, logo a variância é idêntica:
$$ \text{Var}(Y) = \frac{5}{18} $$

- **$\text{Var}(Z)$:** 
A variável $Z = X + Y$ conta o número de lançamentos (em 2) onde saiu face 1 **ou** face 6. A probabilidade de isso ocorrer em um lançamento é $p_z = P(\text{face 1}) + P(\text{face 6}) = \frac{2}{6} = \frac{1}{3}$.
Assim, $Z$ também segue uma distribuição Binomial: $Z \sim \text{Bin}(2, \frac{1}{3})$.
$$ \text{Var}(Z) = 2 \times \frac{1}{3} \times \left(1 - \frac{1}{3}\right) = 2 \times \frac{1}{3} \times \frac{2}{3} = \frac{4}{9} $$

- **A igualdade $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ é verdadeira?**
A soma das variâncias de $X$ e $Y$ é:
$$ \text{Var}(X) + \text{Var}(Y) = \frac{5}{18} + \frac{5}{18} = \frac{10}{18} = \frac{5}{9} $$
No entanto, $\text{Var}(X + Y) = \text{Var}(Z) = \frac{4}{9}$.
$$ \frac{4}{9} \neq \frac{5}{9} $$
Portanto, a igualdade **não é verdadeira**. 

**Justificativa:** 
A regra da soma de variâncias $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$ só é válida se $X$ e $Y$ forem independentes. Neste caso, as variáveis são negativamente correlacionadas, porque ambas derivam dos *mesmos* lançamentos: se em uma jogada o dado der face 1 (sucesso para $X$), ele não poderá dar face 6 (fracasso para $Y$) ao mesmo tempo. Há uma restrição mútua na contagem dos sucessos de um no outro.
