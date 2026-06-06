---
id: "q41-dantas-cap01"
titulo: "Questão 41"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "dificil"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Refaça o exercício 40, supondo bolas idênticas ou indistinguíveis.

## Solução

Se as bolas são indistinguíveis, o estado do sistema é completamente definido apenas pela *quantidade* de bolas em cada urna, ou seja, pela configuração macroscópica da distribuição, não importando *quais* bolas específicas estão em qual urna.

Do ponto de vista combinatório, a quantidade total de distribuições distinguíveis (configurações possíveis) de $r$ bolas idênticas em $n$ urnas é dado pelo número de combinações com repetição (frequentemente resolvido pelo método das "barras e estrelas").
O total de configurações (chamemos de $\Omega'$) é:
$$ n(\Omega') = \binom{r + n - 1}{n - 1} $$

A pergunta do exercício 40 fixava uma única configuração macroscópica específica (urna 1 com $r_1$ bolas, urna 2 com $r_2$ bolas, etc., onde $r_1 + r_2 + \dots + r_n = r$).
Logo, há exatamente **1** resultado favorável em $\Omega'$.

Se adotarmos a interpretação clássica de que as configurações macroscópicas são *equiprováveis* (o que, na Física, corresponde à estatística de Bose-Einstein), a probabilidade será simplesmente 1 dividido pelo total de configurações:
$$ P = \frac{1}{\binom{r + n - 1}{n - 1}} $$

*(Nota: Na realidade física clássica de objetos lançados aleatoriamente em caixas, a estatística correta é a de Maxwell-Boltzmann, que trata as partículas como distinguíveis – que foi a resposta da questão 40. O modelo de equiprobabilidade de estados macroscópicos é apenas um modelo alternativo.)*
