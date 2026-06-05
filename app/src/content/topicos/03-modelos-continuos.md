---
id: "03-modelos-continuos"
titulo: "Principais Modelos Contínuos"
ordem: 3
ementa_ref: "Principais modelos contínuos"
tags: ["uniforme", "exponencial", "gama", "beta", "pareto", "weibull"]
---

# Principais Modelos Contínuos

Modelos contínuos são a base da estatística para representar incertezas e variabilidades sobre intervalos numéricos.

## Usabilidade e Aplicações na Vida Real

A Estatística não é apenas matemática abstrata. Modelos contínuos resolvem problemas trilionários no mercado e salvam vidas:

- **Simulações Computacionais (Uniforme):** Jogos, modelos climáticos e criptografia dependem de geradores de números aleatórios que seguem distribuições uniformes para evitar padrões previsíveis.
- **Teoria das Filas e Confiabilidade (Exponencial):** Usada por empresas como AWS ou Uber para calcular o tempo esperado até um servidor falhar, ou o tempo de espera do próximo cliente num caixa de supermercado.
- **Meteorologia e Seguros (Gama):** Modelagem de quanto volume de chuva cairá durante uma tempestade, ou previsão do valor agregado de sinistros de seguros de carro ao longo de um mês.
- **Eficácia Médica e Testes A/B (Beta):** Modelagem de conversões (quantas pessoas clicam num anúncio vs ignoram) ou a taxa de sucesso de uma nova vacina. A Beta permite incorporar o nosso conhecimento "prévio" (prior Bayesiano).

## Distribuição Uniforme

A variável aleatória uniforme contínua indica que a probabilidade é distribuída uniformemente sobre um intervalo $[a, b]$. Imagine o tempo de espera de um ônibus que passa **exatamente** a cada 10 minutos; se você chegar na parada num momento aleatório, seu tempo de espera segue uma distribuição uniforme de 0 a 10.


$$X \sim U(a, b)$$

- **FDP:** $f(x) = \frac{1}{b-a}$ para $a \le x \le b$ (e zero caso contrário)
- **FDA:** $F(x) = \frac{x-a}{b-a}$ para $a \le x \le b$
- **Média:** $E[X] = \frac{a+b}{2}$
- **Variância:** $Var(X) = \frac{(b-a)^2}{12}$

## Distribuição Exponencial

Modela o tempo de espera até a ocorrência de um evento em um Processo de Poisson. 

$$X \sim Exp(\lambda)$$

- **FDP:** $f(x) = \lambda e^{-\lambda x}$ para $x \ge 0$
- **FDA:** $F(x) = 1 - e^{-\lambda x}$ para $x \ge 0$
- **Média:** $E[X] = \frac{1}{\lambda}$
- **Variância:** $Var(X) = \frac{1}{\lambda^2}$

### Propriedade de Falta de Memória

A exponencial é a única distribuição contínua com a propriedade de falta de memória (memoryless property):

$$P(X > s + t | X > s) = P(X > t)$$

Isso significa que a probabilidade do componente sobreviver por mais $t$ horas, dado que já sobreviveu $s$ horas, é a mesma que a de um componente novo sobreviver $t$ horas.

## Distribuição Gama

Modela o tempo necessário para observar a ocorrência de $\alpha$ eventos em um Processo de Poisson com taxa $1/\beta$ (usando parametrização de forma e escala).

$$X \sim Gama(\alpha, \beta)$$

- **FDP:** $f(x) = \frac{1}{\Gamma(\alpha)\beta^\alpha} x^{\alpha-1}e^{-x/\beta}$ para $x > 0$
- **Média:** $E[X] = \alpha\beta$
- **Variância:** $Var(X) = \alpha\beta^2$

*Nota:* Quando $\alpha = 1$, a Gama se reduz a uma Exponencial com $\lambda = 1/\beta$.

## Distribuição Beta

Frequentemente usada para modelar variáveis limitadas a um intervalo fixo, especialmente $[0, 1]$, como proporções ou probabilidades na inferência Bayesiana.

$$X \sim Beta(\alpha, \beta)$$

- **FDP:** $f(x) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} x^{\alpha-1}(1-x)^{\beta-1}$ para $0 < x < 1$
- **Média:** $E[X] = \frac{\alpha}{\alpha+\beta}$
- **Variância:** $Var(X) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$
