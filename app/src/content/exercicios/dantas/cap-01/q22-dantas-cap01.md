---
id: "q22-dantas-cap01"
titulo: "Questão 22"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

> [!NOTE]
> A questão 21 não existe na numeração original do livro, pulando direto da 20 para a 22.

## Enunciado
Um comitê é formado por quatro homens e duas mulheres. Dois membros do comitê são selecionados sucessivamente, ao acaso e sem reposição. Calcule a probabilidade de cada um dos resultados: HH, HM, MH e MM.

## Solução

Temos um total de 6 pessoas no comitê: 4 Homens (H) e 2 Mulheres (M).
Como os membros são selecionados sem reposição, a probabilidade da segunda escolha depende do que foi sorteado na primeira.

- **Probabilidade de HH (Homem e Homem):**
$$ P(HH) = P(H_1) \times P(H_2 \mid H_1) $$
$$ P(HH) = \left(\frac{4}{6}\right) \times \left(\frac{3}{5}\right) = \frac{12}{30} = \frac{2}{5} = 0,40 $$

- **Probabilidade de HM (Homem e Mulher):**
$$ P(HM) = P(H_1) \times P(M_2 \mid H_1) $$
$$ P(HM) = \left(\frac{4}{6}\right) \times \left(\frac{2}{5}\right) = \frac{8}{30} = \frac{4}{15} \approx 0,2667 $$

- **Probabilidade de MH (Mulher e Homem):**
$$ P(MH) = P(M_1) \times P(H_2 \mid M_1) $$
$$ P(MH) = \left(\frac{2}{6}\right) \times \left(\frac{4}{5}\right) = \frac{8}{30} = \frac{4}{15} \approx 0,2667 $$

- **Probabilidade de MM (Mulher e Mulher):**
$$ P(MM) = P(M_1) \times P(M_2 \mid M_1) $$
$$ P(MM) = \left(\frac{2}{6}\right) \times \left(\frac{1}{5}\right) = \frac{2}{30} = \frac{1}{15} \approx 0,0667 $$

Podemos verificar que a soma de todas as probabilidades é $\frac{12+8+8+2}{30} = \frac{30}{30} = 1$.
