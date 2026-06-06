---
id: "q23-dantas-cap02"
titulo: "Questão 23"
topicos: ["03-modelos-continuos"]
dificuldade: "dificil"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Seja X uma variável aleatória cuja função de distribuição é dada por: 
$F(x)=0, x<0$
$F(x)=x/3, 0\leq x<1$
$F(x)=x/2, 1\leq x<2$
$F(x)=1, x\geq 2.$ 
(a) Esboce o gráfico de F e verifique se X é uma variável aleatória contínua. 
(b) Calcule $P(\frac{1}{2} \le X \le \frac{3}{2}), P(\frac{1}{2} \le X < \frac{3}{2}), P(\frac{1}{2} \le X \le 1), P(\frac{1}{2} \le X < 1), P(1 < X < 2) \text{ e } P(1 \le X \le 2)$.

## Solução

- **(a) Esboço do gráfico e verificação de continuidade:**
Para verificar se $X$ é estritamente contínua, precisamos garantir que sua Função de Distribuição Acumulada $F(x)$ seja contínua em toda a reta real, sem nenhum "salto" ou descontinuidade.
As transições ocorrem em $x=0, x=1$ e $x=2$.
No ponto $x=0$:
$\lim_{x \to 0^-} F(x) = 0$ e $F(0) = 0/3 = 0$. (É contínua).
No ponto $x=1$:
$\lim_{x \to 1^-} F(x) = 1/3$ e $F(1) = 1/2$. (Temos uma descontinuidade de salto!)
O tamanho do salto em $x=1$ é $\Delta P = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$. Isso indica que há uma massa de probabilidade concentrada pontualmente em $X=1$: $P(X=1) = \frac{1}{6}$.
No ponto $x=2$:
$\lim_{x \to 2^-} F(x) = 2/2 = 1$ e $F(2) = 1$. (É contínua).
**Conclusão:** Como $F(x)$ apresenta um salto em $x=1$, $X$ **não é** uma variável aleatória contínua (ela é mista: contínua na maior parte do domínio, mas com uma probabilidade discreta em $x=1$). O gráfico possui uma rampa do ponto $(0,0)$ até o ponto aberto $(1, 1/3)$, um salto para o ponto fechado $(1, 1/2)$, uma rampa de $(1, 1/2)$ até o ponto contínuo $(2, 1)$, e torna-se constante em $y=1$ para todo $x \ge 2$.

- **(b) Cálculos de probabilidade:**
Sabendo que $P(a < X \le b) = F(b) - F(a)$ e que $P(X=x)$ só existe para $x=1$ (com valor $1/6$).

1. **$P(\frac{1}{2} \le X \le \frac{3}{2})$:**
$$ P(\frac{1}{2} \le X \le \frac{3}{2}) = F(1.5) - F(0.5^-) = \frac{1.5}{2} - \frac{0.5}{3} = \frac{3}{4} - \frac{1}{6} = \frac{9}{12} - \frac{2}{12} = \frac{7}{12} $$
2. **$P(\frac{1}{2} \le X < \frac{3}{2})$:**
Como em $x=1.5$ não há salto de probabilidade, o sinal "menor" vs "menor ou igual" não afeta o resultado.
$$ P = F(1.5^-) - F(0.5^-) = \frac{3}{4} - \frac{1}{6} = \frac{7}{12} $$
3. **$P(\frac{1}{2} \le X \le 1)$:**
O valor superior inclui $X=1$, onde há salto.
$$ P = F(1) - F(0.5^-) = \frac{1}{2} - \frac{1}{6} = \frac{3}{6} - \frac{1}{6} = \frac{2}{6} = \frac{1}{3} $$
4. **$P(\frac{1}{2} \le X < 1)$:**
O valor superior **não** inclui o ponto $x=1$, então paramos o acúmulo no limite à esquerda.
$$ P = F(1^-) - F(0.5^-) = \frac{1}{3} - \frac{1}{6} = \frac{2}{6} - \frac{1}{6} = \frac{1}{6} $$
5. **$P(1 < X < 2)$:**
Não inclui o salto de $X=1$.
$$ P = F(2^-) - F(1) = 1 - \frac{1}{2} = \frac{1}{2} $$
6. **$P(1 \le X \le 2)$:**
Inclui todo o intervalo entre 1 e 2, bem como a massa de probabilidade do salto exato em $X=1$.
$$ P = F(2) - F(1^-) = 1 - \frac{1}{3} = \frac{2}{3} $$
