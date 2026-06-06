---
id: "q30-dantas-cap01"
titulo: "Questão 30"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Em um jornal existem dez jornalistas. Se quisermos colocar três jornalistas trabalhando na sede do jornal, cinco em reportagem externa e dois de reserva, de quantas maneiras isso poderá ser feito?

## Solução

Trata-se de um problema de particionamento de um conjunto de 10 elementos distintos em 3 subconjuntos (grupos) com tamanhos pré-determinados (3, 5 e 2), sendo que a ordem das pessoas dentro de um mesmo grupo não importa.

Isso pode ser resolvido com um coeficiente multinomial, ou usando combinações sucessivas:

1. Vamos escolher primeiro os 3 jornalistas para a Sede, dentre os 10 disponíveis:
   $$ \binom{10}{3} = \frac{10!}{3!7!} = \frac{10 \times 9 \times 8}{6} = 120 $$

2. Agora restam $10 - 3 = 7$ jornalistas. Vamos escolher os 5 para a Reportagem Externa:
   $$ \binom{7}{5} = \frac{7!}{5!2!} = \frac{7 \times 6}{2} = 21 $$

3. Sobraram 2 jornalistas, e temos exatamente as 2 vagas de Reserva:
   $$ \binom{2}{2} = \frac{2!}{2!0!} = 1 $$

A quantidade total de maneiras de alocar os jornalistas é o produto das escolhas possíveis:
$$ \text{Total} = \binom{10}{3} \times \binom{7}{5} \times \binom{2}{2} = 120 \times 21 \times 1 = 2520 $$

*(A fórmula direta pelo coeficiente multinomial é $ \frac{10!}{3! \cdot 5! \cdot 2!} = 2520 $).*

Portanto, isso pode ser feito de **2.520** maneiras.
