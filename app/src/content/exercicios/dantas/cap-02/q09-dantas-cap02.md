---
id: "dantas-cap02-q09"
titulo: "Esperanca e Variancia para Distribuicoes das Questoes 1 a 8"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "variancia"]
referencia: "Dantas, Cap. 2, Q. 9"
---

## Enunciado
Considere novamente as questões de 1 a 8. Determine, em cada caso, $E(X)$ e $\text{Var}(X)$ (para o exercício 3, utilize as igualdades  $\sum_{k=1}^N k^2 = \frac{N(N+1)(2N+1)}{6} \text{ e } \sum_{k=1}^N k^3 = \left[\frac{N(N+1)}{2}\right]^2$).

## Solução

Abaixo calculamos a Esperança Matemática $E(X)$ e Variância $\text{Var}(X) = E(X^2) - [E(X)]^2$ para as distribuições das 8 primeiras questões.

### Questão 1 (Discreta empírica)
$T \in \{2,3,4,5,6,7\}$ com prob $p_i = \{\frac{1}{10}, \frac{1}{10}, \frac{4}{10}, \frac{2}{10}, \frac{1}{10}, \frac{1}{10}\}$.
- $E(T) = \sum t_i p_i = \frac{2(1) + 3(1) + 4(4) + 5(2) + 6(1) + 7(1)}{10} = \frac{44}{10} = \mathbf{4,4}$.
- $E(T^2) = \frac{4(1) + 9(1) + 16(4) + 25(2) + 36(1) + 49(1)}{10} = \frac{212}{10} = 21,2$.
- $\text{Var}(T) = 21,2 - (4,4)^2 = 21,2 - 19,36 = \mathbf{1,84}$.

### Questão 2 (Geométrica deslocada)
$P(X=x) = \left(\frac{1}{2}\right)^{x+1}, x \in \mathbb{N}$.
Esta é uma variável de distribuição geométrica representando os fracassos antes do primeiro sucesso (com $p = 1/2$). 
- $E(X) = \frac{1-p}{p} = \frac{1/2}{1/2} = \mathbf{1}$.
- $\text{Var}(X) = \frac{1-p}{p^2} = \frac{1/2}{1/4} = \mathbf{2}$.

### Questão 3
$P(X=x) = cx = \frac{2x}{N(N+1)}$, $x \in \{1, 2, \dots, N\}$.
- $E(X) = \sum_{x=1}^N x \frac{2x}{N(N+1)} = \frac{2}{N(N+1)} \sum x^2 = \frac{2}{N(N+1)} \frac{N(N+1)(2N+1)}{6} = \mathbf{\frac{2N+1}{3}}$.
- $E(X^2) = \frac{2}{N(N+1)} \sum x^3 = \frac{2}{N(N+1)} \left[\frac{N(N+1)}{2}\right]^2 = \frac{N(N+1)}{2}$.
- $\text{Var}(X) = \frac{N(N+1)}{2} - \left(\frac{2N+1}{3}\right)^2 = \dots = \mathbf{\frac{N^2+N-2}{18}}$.

### Questão 4 (Dois dados)
- **(a) Máximo:** $E(X) = \frac{161}{36} \approx \mathbf{4,472}$. $E(X^2) = \frac{791}{36}$. $\text{Var}(X) = \frac{2555}{1296} \approx \mathbf{1,971}$.
- **(b) Soma:** $E(X) = 2 \times 3,5 = \mathbf{7}$. $\text{Var}(X) = \frac{35}{12} + \frac{35}{12} = \frac{35}{6} \approx \mathbf{5,833}$.
- **(c) Produto:** $E(X) = E(D_1)E(D_2) = (3,5)^2 = \mathbf{12,25}$. $\text{Var}(X) = E(D_1^2)E(D_2^2) - (E(X))^2 = \left(\frac{91}{6}\right)^2 - \left(\frac{49}{4}\right)^2 = \frac{11515}{144} \approx \mathbf{79,965}$.
- **(d) Diferença:** $E(X) = \frac{70}{36} = \mathbf{\frac{35}{18}} \approx 1,944$. $E(X^2) = \frac{210}{36} = \frac{35}{6}$. $\text{Var}(X) = \frac{35}{6} - \left(\frac{35}{18}\right)^2 = \mathbf{\frac{665}{324}} \approx 2,052$.

### Questão 5
$f(x) = \frac{3}{2}x^2$ em $[-1, 1]$.
- $E(X) = \int_{-1}^1 x \left(\frac{3}{2}x^2\right) dx = \mathbf{0}$ (função ímpar em intervalo simétrico).
- $\text{Var}(X) = E(X^2) = \int_{-1}^1 \frac{3}{2}x^4 dx = \frac{3}{2} \left[\frac{x^5}{5}\right]_{-1}^1 = \mathbf{\frac{3}{5}} = 0,6$.

### Questão 6
$f(x) = \lambda e^{-\lambda x}$ (Exponencial).
- $E(X) = \mathbf{\frac{1}{\lambda}}$.
- $\text{Var}(X) = \mathbf{\frac{1}{\lambda^2}}$.

### Questão 7
Distribuição triangular $c=4$ em $[0, 1]$.
- $E(X) = \mathbf{\frac{1}{2}}$ (por simetria).
- $E(X^2) = \int_0^{1/2} 4x^3 dx + \int_{1/2}^1 4x^2(1-x) dx = \dots = \frac{7}{24}$.
- $\text{Var}(X) = \frac{7}{24} - \left(\frac{1}{2}\right)^2 = \frac{7}{24} - \frac{6}{24} = \mathbf{\frac{1}{24}}$.

### Questão 8
$f(x) = -\cos(x)$ em $[\frac{\pi}{2}, \pi]$.
- $E(X) = \int_{\pi/2}^\pi -x\cos(x) dx = \mathbf{1 + \frac{\pi}{2}}$. (Usando integração por partes).
- $E(X^2) = \int_{\pi/2}^\pi -x^2\cos(x) dx = 2\pi + \frac{\pi^2}{4} - 2$.
- $\text{Var}(X) = \left(2\pi + \frac{\pi^2}{4} - 2\right) - \left(1 + \frac{\pi}{2}\right)^2 = \mathbf{\pi - 3}$.
