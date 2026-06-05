---
id: "questoes-q02-lista-questo-2"
titulo: "Questão 2"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

A percentagem de álcool (100X) em certo composto pode ser considerada uma variável aleatória, onde X, $0<X<1$, tem a seguinte fdp: $f(x)=20x^{3}(1-x)$, $0<x<1$.

(a) Estabeleça a expressão da função de distribuição acumulada F e esboce seu gráfico.

(b) Calcule $P(X\le\frac{2}{5})$.

(c) Suponha que o preço de venda desse composto dependa do conteúdo de álcool. Especificamente, se $\frac{1}{3}<X<\frac{2}{3}$, o composto se vende por $C_{1}$ dólares/galão; caso contrário, ele se vende por $C_{2}$ dólares/galão. Calcule a distribuição de probabilidade do lucro líquido por galão.

## Solução

## Parte (a): Função de Distribuição Acumulada (FDA)


## Passo 1: Definir a FDA

A Função de Distribuição Acumulada, $F(x)$, representa a probabilidade $P(X \le x)$. Ela é calculada integrando-se a função densidade de probabilidade (fdp) desde o limite inferior do domínio até $x$.

$$F(x) = \int_{0}^{x} f(t) \,dt = \int_{0}^{x} 20t^{3}(1-t) \,dt$$

Resumo: A FDA é a integral da fdp, acumulando a probabilidade até um ponto x.



## Passo 2: Resolver a Integral

Primeiro, expandimos o integrando: $20t^{3}(1-t) = 20t^{3} - 20t^{4}$.

$$F(x) = \int_{0}^{x} (20t^{3} - 20t^{4}) \,dt = [20\frac{t^{4}}{4} - 20\frac{t^{5}}{5}]_{0}^{x}$$

$$= [5t^{4} - 4t^{5}]_{0}^{x} = (5x^{4} - 4x^{5}) - (0) = 5x^{4} - 4x^{5}$$

A FDA completa, definida por partes, é: $F(x) = \begin{cases} 0, & \text{se } x \le 0 \\ 5x^{4} - 4x^{5}, & \text{se } 0 < x < 1 \\ 1, & \text{se } x \ge 1 \end{cases}$

Resumo: Realizamos a integração do polinômio para encontrar a expressão da FDA para o intervalo $0<x<1$.



<h5 class="text-center font-semibold">Gráfico da fdp: $f(x)$</h5>

<h5 class="text-center font-semibold">Gráfico da FDA: $F(x)$</h5>


## Parte (b): Cálculo de $P(X\le\frac{2}{5})$


## Passo 1: Utilizar a FDA

A probabilidade $P(X \le a)$ é, por definição, o valor da FDA no ponto $a$, ou seja, $F(a)$.

$$P(X \le \frac{2}{5}) = F(\frac{2}{5})$$

$$= 5(\frac{2}{5})^{4} - 4(\frac{2}{5})^{5} = 5(\frac{16}{625}) - 4(\frac{32}{3125}) = \frac{80}{625} - \frac{128}{3125}$$

$$= \frac{400}{3125} - \frac{128}{3125} = \frac{272}{3125} \approx 0.08704$$

Resumo: Substituímos o valor $x = 2/5$ na fórmula da FDA encontrada na parte (a) para obter a probabilidade.


## Parte (c): Distribuição de probabilidade do lucro


## Passo 1: Calcular $P(Y=C_1)$

O preço é $C_1$ quando $\frac{1}{3}<X<\frac{2}{3}$. Usamos a FDA para calcular essa probabilidade:

$$P(\frac{1}{3} < X < \frac{2}{3}) = F(\frac{2}{3}) - F(\frac{1}{3})$$

Calculando cada termo:

$F(\frac{2}{3}) = 5(\frac{2}{3})^4 - 4(\frac{2}{3})^5 = 5(\frac{16}{81}) - 4(\frac{32}{243}) = \frac{80}{81} - \frac{128}{243} = \frac{240-128}{243} = \frac{112}{243}$

$F(\frac{1}{3}) = 5(\frac{1}{3})^4 - 4(\frac{1}{3})^5 = 5(\frac{1}{81}) - 4(\frac{1}{243}) = \frac{5}{81} - \frac{4}{243} = \frac{15-4}{243} = \frac{11}{243}$

$$P(Y=C_1) = \frac{112}{243} - \frac{11}{243} = \frac{101}{243} \approx 0.4156$$

Resumo: A probabilidade de o preço ser $C_1$ é a área sob a fdp entre 1/3 e 2/3, calculada pela diferença dos valores da FDA.



## Passo 2: Calcular $P(Y=C_2)$

O preço é $C_2$ em "caso contrário", ou seja, com a probabilidade complementar.

$$P(Y=C_2) = 1 - P(Y=C_1) = 1 - \frac{101}{243} = \frac{243 - 101}{243} = \frac{142}{243} \approx 0.5844$$

Resumo: A probabilidade do evento complementar é 1 menos a probabilidade do evento original.
