---
id: "q29-dantas-cap01"
titulo: "Questão 29"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Suponha que existam dez livros que devem ser colocados em uma estante, sendo quatro de matemática, três de química, dois de física e um dicionário. Se quisermos que os livros de mesmo assunto fiquem juntos, de quantas maneiras isso será possível?

## Solução

Neste problema de Análise Combinatória, queremos calcular as permutações de itens, com a restrição de que itens do mesmo "assunto" permaneçam em blocos contíguos.

Podemos imaginar cada grupo de livros de um mesmo assunto como um "bloco" fechado. 
Temos 4 blocos de matérias (Matemática, Química, Física e Dicionário).
Primeiro, vamos calcular de quantas maneiras podemos arranjar esses blocos entre si na estante:
$$ P_4 = 4! = 24 \text{ maneiras} $$

Agora, para cada arranjo de blocos, podemos permutar os livros *dentro* do próprio bloco:
- Permutações dos 4 livros de Matemática: $4! = 24$ maneiras
- Permutações dos 3 livros de Química: $3! = 6$ maneiras
- Permutações dos 2 livros de Física: $2! = 2$ maneiras
- Permutações do único Dicionário: $1! = 1$ maneira

Para obter o número total de possibilidades, multiplicamos o número de arranjos dos blocos pelas permutações internas de cada bloco (Princípio Fundamental da Contagem):
$$ \text{Total} = 4! \times (4! \times 3! \times 2! \times 1!) $$
$$ \text{Total} = 24 \times (24 \times 6 \times 2 \times 1) $$
$$ \text{Total} = 24 \times 288 = 6912 $$

Portanto, existem **6.912** maneiras de dispor os dez livros de forma que os livros do mesmo assunto fiquem juntos.
