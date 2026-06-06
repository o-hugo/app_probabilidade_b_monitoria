---
id: "q24-dantas-cap01"
titulo: "Questão 24"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
É dada a distribuição de 300 estudantes segundo o sexo e a área de concentração:

|           | Biologia | Exatas | Humanas |
|-----------|----------|--------|---------|
| Masculino | 52       | 40     | 58      |
| Feminino  | 38       | 32     | 80      |

Um estudante é sorteado ao acaso.
(a) Qual é a probabilidade de que ele seja do sexo feminino e da área de humanas? 
(b) Qual é a probabilidade de que ele seja do sexo masculino e não seja da área de biológicas? 
(c) Dado que foi sorteado um estudante da área de humanas, qual é a probabilidade de que ele seja do sexo feminino?

## Solução

Podemos preencher os totais marginais da tabela para facilitar as contas:
- Total Masculino: $52 + 40 + 58 = 150$
- Total Feminino: $38 + 32 + 80 = 150$
- Total Biologia: $52 + 38 = 90$
- Total Exatas: $40 + 32 = 72$
- Total Humanas: $58 + 80 = 138$
Total Geral = $300$

- **(a) Probabilidade de ser feminino e de humanas:**
Observamos diretamente a célula correspondente: Feminino $\cap$ Humanas = 80.
$$ P(F \cap H) = \frac{80}{300} = \frac{4}{15} \approx 0,2667 $$

- **(b) Probabilidade de ser masculino e não ser de biológicas:**
Não ser de biológicas significa ser de Exatas ou Humanas.
Alunos masculinos em Exatas = 40. Alunos masculinos em Humanas = 58. Total = $40 + 58 = 98$.
$$ P(M \cap B^c) = \frac{98}{300} = \frac{49}{150} \approx 0,3267 $$

- **(c) Probabilidade de ser feminino, dado que é de humanas:**
Sabemos que o estudante é de Humanas, logo nosso novo espaço amostral tem tamanho $138$ (o total de humanas).
Dentre esses 138, a quantidade de mulheres é 80.
Usando a fórmula de probabilidade condicional:
$$ P(F \mid H) = \frac{P(F \cap H)}{P(H)} = \frac{80/300}{138/300} = \frac{80}{138} = \frac{40}{69} \approx 0,5797 $$
