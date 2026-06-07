---
id: "dantas-cap01-q20"
titulo: "Probabilidade em Espacos Equiprovaveis"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 1, Q. 20"
---

## Enunciado
No exercício 1 considere os pontos amostrais em a) e c) equiprováveis. Em a) calcule a probabilidade da soma dos pontos dos dois dados ser igual a seis. Em c) calcule a probabilidade de uma família ter três filhos do sexo masculino.

## Solução

O espaço amostral equiprovável do exercício 1-(a) é o lançamento de dois dados, e do 1-(c) é o registro do sexo dos 4 filhos de uma família.

- **Para o caso (a): Lançamento de dois dados**
O espaço amostral $\Omega$ possui $6 \times 6 = 36$ resultados equiprováveis.
Queremos o evento $S = \{\text{soma igual a 6}\}$.
Os resultados que dão soma 6 são: $(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)$.
Temos 5 resultados favoráveis.
$$ P(S) = \frac{5}{36} \approx 0,1389 $$

- **Para o caso (c): Quatro filhos**
O espaço amostral $\Omega$ possui $2^4 = 16$ combinações equiprováveis de sexo.
Queremos o evento $F = \{\text{exatamente três meninos (M) e uma menina (F)}\}$.
As combinações favoráveis (variando a posição em que nasce a menina) são:
$\{ (F, M, M, M), (M, F, M, M), (M, M, F, M), (M, M, M, F) \}$
Temos 4 resultados favoráveis.
$$ P(F) = \frac{4}{16} = \frac{1}{4} = 0,25 $$
