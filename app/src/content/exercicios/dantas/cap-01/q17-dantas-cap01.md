---
id: "q17-dantas-cap01"
titulo: "Questão 17"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Uma urna contém duas bolas brancas e duas pretas. As bolas são retiradas ao acaso, sucessivamente e sem reposição. 
(a) Qual é a probabilidade de sair uma bola preta na primeira retirada? 
(b) Qual é a probabilidade de que a primeira bola preta apareça somente na quarta retirada? 
(c) Qual é a probabilidade de que a segunda bola preta apareça logo na segunda retirada? 
(d) Qual é a probabilidade de que a segunda bola preta apareça somente na quarta retirada?

## Solução

A urna possui inicialmente 4 bolas: 2 Brancas (B) e 2 Pretas (P). As retiradas são sem reposição.

- **(a) Sair uma preta na primeira retirada:**
Como existem 2 bolas pretas entre as 4 bolas totais, a probabilidade é simplesmente:
$$ P(\text{Preta na 1ª}) = \frac{2}{4} = \frac{1}{2} = 0,5 $$

- **(b) A primeira preta aparecer somente na quarta retirada:**
Para que a primeira bola preta saia apenas na 4ª retirada, as três primeiras teriam de ser obrigatoriamente Brancas. 
Porém, como só existem 2 bolas brancas na urna, é um evento **impossível**.
$$ P(\text{1ª preta na 4ª retirada}) = 0 $$

- **(c) A segunda preta aparecer logo na segunda retirada:**
Para que isso aconteça, a primeira bola sorteada deve ser preta e a segunda também.
$$ P(P_1 \cap P_2) = P(P_1) \times P(P_2 \mid P_1) = \left(\frac{2}{4}\right) \times \left(\frac{1}{3}\right) = \frac{2}{12} = \frac{1}{6} \approx 0,1667 $$

- **(d) A segunda preta aparecer somente na quarta retirada:**
Isso significa que, nas primeiras 3 retiradas, saíram **exatamente** 2 bolas brancas e 1 bola preta (em qualquer ordem), e a 4ª retirada foi a última bola preta que restava.
As sequências possíveis para as três primeiras retiradas são: $BBP$, $BPB$ e $PBB$.
A probabilidade de qualquer uma dessas três sequências específicas é a mesma:
$$ P(BBP) = \left(\frac{2}{4}\right) \times \left(\frac{1}{3}\right) \times \left(\frac{2}{2}\right) = \frac{2}{12} = \frac{1}{6} $$
$$ P(BPB) = \left(\frac{2}{4}\right) \times \left(\frac{2}{3}\right) \times \left(\frac{1}{2}\right) = \frac{4}{24} = \frac{1}{6} $$
$$ P(PBB) = \left(\frac{2}{4}\right) \times \left(\frac{2}{3}\right) \times \left(\frac{1}{2}\right) = \frac{4}{24} = \frac{1}{6} $$
A soma destas probabilidades (a chance de termos 2 brancas e 1 preta nas 3 primeiras retiradas) é $\frac{3}{6} = \frac{1}{2}$.
A 4ª retirada, por ser a última bola preta que restou na urna (já que 3 bolas já foram retiradas e sobrou 1), tem probabilidade $\frac{1}{1} = 1$.
Portanto, a probabilidade procurada é:
$$ P(\text{2ª preta na 4ª}) = \frac{1}{2} \times 1 = \frac{1}{2} = 0,5 $$
