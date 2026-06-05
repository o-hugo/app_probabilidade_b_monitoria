---
id: "lista02-q04-chegada-do-nibus"
titulo: "Chegada do Ônibus"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Passageiro chega uniformemente entre 7h00 e 7h30. Ônibus chegam às 7h00, 7h15, 7h30. Calcule P(espera < 5 min) e P(espera > 10 min).

## Solução

Seja $T$ o tempo de chegada em minutos após as 7h00, $T \sim U(0, 30)$.

## a) Esperar menos que 5 minutos

Isso acontece se o passageiro chegar nos 5 minutos que antecedem um ônibus. <br>Para o ônibus das 7h15 (T=15): Chegar entre [10, 15].<br>Para o ônibus das 7h30 (T=30): Chegar entre [25, 30].<br>O intervalo total favorável é $(15-10) + (30-25) = 10$ minutos.<br>$ P = \frac{\text{Intervalo Favorável}}{\text{Intervalo Total}} = \frac{10}{30} = \frac{1}{3} $

## b) Esperar mais de 10 minutos

Para o ônibus das 7h15, a espera é $15-T$. $15-T > 10 \implies T < 5$. Intervalo: [0, 5).<br>Para o ônibus das 7h30, a espera é $30-T$. $30-T > 10 \implies T < 20$. Como o ônibus das 7h15 já partiu, o intervalo relevante é [15, 20).<br>O intervalo total favorável é $(5-0) + (20-15) = 10$ minutos.<br>$ P = \frac{10}{30} = \frac{1}{3} $
