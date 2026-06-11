---
id: "dantas-cap06-q24"
titulo: "Transformações Jacobianas de Uniformes Independentes"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano"]
referencia: "Dantas, Cap. 6, Q. 24"
---

## Enunciado

$X,Y\sim U(0,1)$ independentes. Determine a densidade conjunta de $U$ e $V$ quando:
(a) $U=X+Y$, $V=X/Y$; (b) $U=X$, $V=X/Y$; (c) $U=X+Y$, $V=X/(X+Y)$.

## Solução

**(a) $U=X+Y$, $V=X/Y$:**

$X=UV/(1+V)$, $Y=U/(1+V)$. Jacobiano: $|J|=u/(1+v)^2$.

Condições: $X,Y\in(0,1)$: $u/(1+v)\in(0,1)$ e $uv/(1+v)\in(0,1)$.

$$f_{U,V}(u,v)=\frac{u}{(1+v)^2},$$

para a região válida (depende de $v$: se $v<1$, $u\in(0,1+v)$; se $v>1$, $u\in(0,(1+v)/v)$).

**(b) $U=X$, $V=X/Y$:**

$X=U$, $Y=U/V$. Jacobiano: $|J|=u/v^2$.

Condições: $U=X\in(0,1)$ e $Y=U/V\in(0,1)$, i.e., $v>u$.

$$f_{U,V}(u,v)=\frac{u}{v^2}, \quad 0<u<1,\ v>u.$$

**(c) $U=X+Y$, $V=X/(X+Y)$:**

$X=UV$, $Y=U(1-V)$. Jacobiano: $|J|=u$.

Condições: $U\in(0,2)$ e $V\in(0,1)$ (com restrições em $U$ dependendo de $V$).

$$f_{U,V}(u,v)=u, \quad \text{para }u\in(0,1/\max(v,1-v)),\ v\in(0,1).$$

Para $v\in(0,1)$: $x=uv<1$ e $y=u(1-v)<1$ exigem $u<1/v$ e $u<1/(1-v)$, logo $u<\min(1/v,1/(1-v))$.
