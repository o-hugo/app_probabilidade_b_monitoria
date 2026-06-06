---
id: "q36-dantas-cap01"
titulo: "Questão 36"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Numa urna onde existiam oito bolas brancas e seis azuis, foi perdida uma bola de cor desconhecida. Uma bola foi retirada da urna. Qual é a probabilidade de a bola perdida ser branca, dado que a bola retirada é branca?

## Solução

Esse é um excelente problema de Teorema de Bayes.
A composição inicial da urna era de 14 bolas (8 Brancas e 6 Azuis). 

Houve um evento inicial onde uma bola foi perdida. Vamos definir os eventos:
- $L_B$: a bola perdida era branca.
- $L_A$: a bola perdida era azul.

Como a bola perdida caiu da urna inicial por acaso, as probabilidades a priori são proporcionais à quantidade original de bolas:
$$ P(L_B) = \frac{8}{14} = \frac{4}{7} $$
$$ P(L_A) = \frac{6}{14} = \frac{3}{7} $$

Após a perda, restam 13 bolas na urna, mas a composição depende de qual foi perdida:
- Se foi perdida uma Branca ($L_B$), restam 7 Brancas e 6 Azuis. A probabilidade de retirar uma branca agora ($R_B$) será:
  $$ P(R_B \mid L_B) = \frac{7}{13} $$
- Se foi perdida uma Azul ($L_A$), restam 8 Brancas e 5 Azuis. A probabilidade de retirar uma branca será:
  $$ P(R_B \mid L_A) = \frac{8}{13} $$

O problema nos pede a probabilidade de a bola perdida ter sido branca, SABENDO que a bola retirada em seguida foi branca: $P(L_B \mid R_B)$.
Usamos a fórmula de Bayes:
$$ P(L_B \mid R_B) = \frac{P(L_B) \times P(R_B \mid L_B)}{P(R_B)} $$

Primeiro, calculamos a probabilidade total de retirar uma bola branca $P(R_B)$:
$$ P(R_B) = P(L_B) \times P(R_B \mid L_B) + P(L_A) \times P(R_B \mid L_A) $$
$$ P(R_B) = \left(\frac{4}{7} \times \frac{7}{13}\right) + \left(\frac{3}{7} \times \frac{8}{13}\right) $$
$$ P(R_B) = \frac{28}{91} + \frac{24}{91} = \frac{52}{91} = \frac{4}{7} $$
*(Note que $52 \div 13 = 4$ e $91 \div 13 = 7$, o que prova um resultado clássico: se retirarmos uma bola aleatória depois que uma bola desconhecida cai, a probabilidade é igual à da urna original).*

Agora aplicamos no Teorema de Bayes:
$$ P(L_B \mid R_B) = \frac{\frac{28}{91}}{\frac{52}{91}} = \frac{28}{52} = \frac{7}{13} \approx 0,5385 $$

Portanto, a probabilidade de a bola perdida ter sido branca é **$7/13$**.
