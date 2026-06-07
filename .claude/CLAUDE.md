# CLAUDE.md — Guia para Agentes de IA

Este documento orienta agentes de IA (Claude, Antigravity, etc.) que trabalhem neste repositório.
Leia-o antes de qualquer modificação.

**Regra geral: nunca use emojis em código, comentários, commits ou documentação.**

---

## Visão Geral do Projeto

Aplicação web estática para o ensino de Probabilidade B (IEE055 — UFAM), construída com Astro 5.
O conteúdo (tópicos, exercícios, revisão) vive em arquivos Markdown com frontmatter YAML validado
por Zod via Astro Content Collections. Não há backend.

**Repositório GitHub:** `o-hugo/app_probabilidade_b_monitoria`
**Deploy:** GitHub Pages via GitHub Actions
**URL de produção:** `https://o-hugo.github.io/app_probabilidade_b_monitoria/`

---

## Estrutura de Diretórios

```
app_probabilidade_b_monitoria/   <- Raiz do repositório git (o que vai para o GitHub)
├── .github/workflows/deploy.yml <- Workflow de deploy automático (não modificar)
├── app/                         <- Código-fonte da aplicação Astro
│   ├── astro.config.mjs         <- Configuração central do Astro
│   ├── src/
│   │   ├── content/             <- Todo o conteúdo educacional
│   │   │   ├── topicos/         <- Teoria por tópico (.md)
│   │   │   ├── exercicios/      <- Exercícios com resolução (.md)
│   │   │   └── revisao/         <- Cheatsheets e resumos (.md)
│   │   ├── content.config.ts    <- Schema das Content Collections (Zod)
│   │   ├── layouts/Layout.astro <- Layout base e navegação
│   │   ├── pages/               <- Rotas da aplicação
│   │   └── styles/global.css    <- Design system (variáveis CSS)
│   └── package.json
└── docs/                        <- Documentação do projeto
```

> Atenção: O repositório git está em `app_probabilidade_b_monitoria/`, não na raiz
> `APP_ENSINO_MONITORIA/`. Ao editar arquivos localmente, edite em `app/src/`
> e sincronize para `app_probabilidade_b_monitoria/app/src/` antes do commit.

---

## Regra Critica: Links e Navegacao

**Todo link interno deve usar `import.meta.env.BASE_URL`**, nunca caminhos absolutos hardcoded.

```astro
<!-- ERRADO — nao funciona no GitHub Pages -->
<a href="/topicos">Topicos</a>
<a href={`/exercicios/${id}`}>Exercicio</a>

<!-- CORRETO -->
<a href={`${import.meta.env.BASE_URL}topicos`}>Topicos</a>
<a href={`${import.meta.env.BASE_URL}exercicios/${id}`}>Exercicio</a>
```

**Por que isso importa:** O site e servido em `/app_probabilidade_b_monitoria/` no GitHub Pages.
Links que comecam com `/` ignoram esse prefixo e geram URLs quebradas.

O `BASE_URL` e definido em `astro.config.mjs`:

```js
base: '/app_probabilidade_b_monitoria/',  // inclui a barra final — obrigatoria
```

A barra final e obrigatoria. Sem ela, `BASE_URL + "topicos"` vira `.../monitoriapicos`.

---

## Workflow de Deploy

O deploy e totalmente automatico via GitHub Actions (`.github/workflows/deploy.yml`).
Qualquer push na branch `main` dispara o workflow:

1. Instala dependencias (`npm install` em `app/`)
2. Roda o build (`npm run build` em `app/`)
3. Publica `app/dist/` no GitHub Pages

**Nao e necessario rodar o build manualmente.** Basta fazer push na `main`.

O status do deploy pode ser acompanhado em:
`https://github.com/o-hugo/app_probabilidade_b_monitoria/actions`

### Push via terminal (quando o GitHub Desktop nao estiver disponivel)

```bash
cd app_probabilidade_b_monitoria
git add -A
git commit -m "tipo: descricao curta e objetiva"
git push https://o-hugo:$(gh auth token)@github.com/o-hugo/app_probabilidade_b_monitoria.git main
```

O `gh auth token` usa o GitHub CLI, que ja esta autenticado como `o-hugo`.

---

## Adicionando Conteudo

Nao e necessario alterar codigo para adicionar topicos ou exercicios.
Consulte `docs/guia-autoria.md` para o formato completo.

### Topico teorico (`app/src/content/topicos/`)

```markdown
---
id: "exponencial"
titulo: "Distribuicao Exponencial"
ordem: 3.2
ementa_ref: "Modelos continuos"
tags: ["modelo-continuo", "falta-de-memoria"]
visualizador: "exponencial"   # opcional
---

Conteudo em Markdown com formulas KaTeX ($inline$ e $$bloco$$).
```

### Exercicio (`app/src/content/exercicios/`)

```markdown
---
id: "lista02-q06"
titulo: "Duracao Exponencial de Ligacao"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"          # baixa | media | alta
origem: "lista-02"            # lista | lista-02 | prova-3 | slide | slides | livro | aula (opcional)
solucao_verificada: false     # mude para true somente apos revisar todos os passos
resposta_final: "0.3679"      # opcional — habilita validacao numerica
tags: ["fdp-valida", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 7"   # opcional — para questoes de livro
---

## Enunciado

Texto do enunciado.

## Passo 1: Identificar a distribuicao

Conteudo do passo.

Resumo: Uma linha descrevendo o que foi feito neste passo.

## Passo 2: Calcular a probabilidade

Conteudo do passo.

Resumo: Uma linha descrevendo o que foi feito neste passo.
```

**Regra de verificacao:** `solucao_verificada: false` exibe aviso para o aluno.
Nunca mude para `true` sem conferir cada passo matematicamente.

---

## Adicionando Exercicios em Lote (de Livro ou Lista)

Quando o usuario fornecer arquivos-fonte de exercicios (ex: `source/dantas/cap-03/`), siga
este fluxo antes de qualquer escrita:

### Perguntas obrigatorias ao usuario

Antes de processar qualquer lote de questoes, pergunte:

1. **Origem:** De onde sao as questoes? (Dantas Cap. X, Lista N, Prova, Slides...)
2. **Solucoes:** Os arquivos ja tem solucoes escritas, ou precisam ser geradas?
3. **Formato de solucao desejado:** Solucao em bloco unico (`## Solucao`) ou passos
   progressivos (`## Passo 1:`, `## Passo 2:`, ...)? O formato de passos e preferivel
   pois habilita a revelacao progressiva no app.
4. **Topicos:** A que topicos do app essas questoes pertencem? (ver lista abaixo)
5. **`solucao_verificada`:** O usuario revisou matematicamente as solucoes? Se sim,
   pode marcar `true`; caso contrario deixar `false`.

### Topicos disponiveis (IDs validos para o campo `topicos`)

| ID | Descricao |
|----|-----------|
| `variaveis-aleatorias-continuas` | FDP, FDA, E[X], Var[X], mediana, moda |
| `02-funcao-geradora-momentos` | FGM M_X(t), cumulantes |
| `03-modelos-continuos` | Uniforme, Exponencial, Gama, Beta, Pareto, Weibull, etc. |
| `04-distribuicao-normal` | Normal, padronizacao Z, TLC |
| `05-funcao-de-variavel-aleatoria` | Transformacoes: metodo FDA, jacobiano |
| `06-distribuicoes-bivariadas` | Distribuicoes conjuntas, marginais, covariancia |

### Tags disponiveis (campo `tags`)

| Tag | Quando usar |
|-----|-------------|
| `fdp-valida` | Verificar/encontrar constante normalizadora de FDP |
| `probabilidade` | Calcular P(a <= X <= b) por integracao |
| `fda` | Construir ou usar a FDA F(x) |
| `esperanca` | Calcular E[X] ou E[g(X)] |
| `variancia` | Calcular Var[X] |
| `mediana` | Encontrar mediana |
| `moda` | Encontrar moda |
| `condicional` | Probabilidade condicional, Bayes |
| `padronizacao-z` | Padronizacao Z para Normal |
| `tlc` | Teorema do Limite Central / aproximacao Normal |
| `falta-de-memoria` | Propriedade falta de memoria (Exponencial) |
| `taxa-de-falha` | Taxa de falha h(t) |
| `confiabilidade` | Confiabilidade R(t) |
| `fgm` | Funcao geradora de momentos |
| `metodo-fda` | Transformacao de VA pelo metodo da FDA |
| `metodo-jacobiano` | Transformacao de VA pelo jacobiano |

### Estrutura de diretorios

Arquivos-fonte (originais, sem processamento) ficam em `source/`:

```
source/
  dantas/
    cap-01/   <- questoes originais do capitulo 1 (ja integradas)
    cap-02/   <- questoes originais do capitulo 2 (ja integradas)
    cap-03/   <- futuras questoes
  listas/
    lista-03/ <- questoes de lista de exercicios
```

Arquivos processados (com frontmatter completo) ficam em:

```
app/src/content/exercicios/
  dantas/
    cap-01/   <- 42 questoes integradas (probabilidade classica)
    cap-02/   <- 42 questoes integradas (VA discretas/continuas, E[X], FGM)
  questoes/   <- questoes de listas e exemplos do livro principal
  lista-02/   <- questoes da lista 02
```

### Formato de passos (preferivel)

O app renderiza `## Passo N:` como revelacao progressiva: cada passo e escondido ate
o aluno clicar "Revelar proximo passo". Use este formato sempre que possivel:

```markdown
## Passo 1: Titulo claro do que sera feito

Conteudo matematico do passo com KaTeX.

Resumo: Uma frase resumindo o resultado deste passo.

## Passo 2: Proximo calculo

...

Resumo: ...
```

O `## Solucao` em bloco unico tambem funciona — e escondido ate o usuario clicar —
mas nao tem revelacao passo a passo. Use quando a solucao e curta ou quando nao
houver tempo para estruturar em passos.

### Estado atual das questoes Dantas

As 84 questoes do Dantas (cap-01 e cap-02) usam `## Solucao` em bloco unico, sem
passos progressivos. A revelacao progressiva funciona (esconde tudo ate o clique),
mas nao divide em sub-passos. Reformatacao futura e possivel mas trabalhosa.

---

## Schemas das Content Collections

Definidos em `app/src/content.config.ts`. Os campos obrigatorios sao:

**Topicos:** `id`, `titulo`, `ordem`, `ementa_ref`, `tags`

**Exercicios:** `id`, `titulo`, `topicos`, `dificuldade`, `origem`, `solucao_verificada`

**Revisao:** `id`, `titulo`, `topicos`

Se adicionar um campo novo ao frontmatter, adicione tambem ao schema em `content.config.ts`,
caso contrario o build falha com erro de validacao.

---

## Boas Praticas de Desenvolvimento

### Codigo

- Nunca use emojis em codigo, comentarios, mensagens de commit ou documentacao.
- Todo link interno deve usar `import.meta.env.BASE_URL` (ver secao acima).
- Mantenha o CSS no design system (`global.css`) em vez de estilos inline ou ad-hoc.
- Componentes interativos devem ser `.astro` com `<script>` client-side isolado.
- Nao adicione dependencias npm sem justificativa clara.

### Commits

Use o formato convencional:

```
feat: adiciona exercicios da lista 03
fix: corrige link quebrado na pagina de topicos
chore: atualiza dependencias
docs: expande guia de autoria
```

Mensagens em portugues, sem ponto final, sem emojis.

### Sincronizacao entre pastas

O repositorio git (`app_probabilidade_b_monitoria/`) e separado do diretorio de trabalho
principal (`APP_ENSINO_MONITORIA/`). Ao editar qualquer arquivo em `APP_ENSINO_MONITORIA/app/`,
copie para `app_probabilidade_b_monitoria/app/` antes do commit.

Exemplo:

```bash
cp APP_ENSINO_MONITORIA/app/src/pages/topicos/index.astro \
   app_probabilidade_b_monitoria/app/src/pages/topicos/index.astro
```

O ideal e que os dois diretorios sejam consolidados no futuro, mantendo apenas o repositorio git.

### Desenvolvimento local

```bash
cd app_probabilidade_b_monitoria/app
npm install
npm run dev     # servidor em http://localhost:4321
```

Em desenvolvimento local, `BASE_URL` e `/` (sem o prefixo do GitHub Pages), entao os links
funcionam normalmente. O prefixo so e aplicado no build de producao.

---

## Problemas Conhecidos e Solucoes

| Problema | Causa | Solucao |
|---|---|---|
| Links quebrados no Pages | `href` hardcoded com `/` | Usar `BASE_URL` em todos os links |
| Build falha com erro de schema | Campo no frontmatter nao declarado em `content.config.ts` | Adicionar campo ao schema Zod |
| Deploy sobrescreve com site vazio | Workflow `static.yml` gerado pelo GitHub conflita com o nosso | Deletar `static.yml` do repositorio |
| Push falha por autenticacao | Terminal nao tem credenciais do GitHub Desktop | Usar `gh auth token` ou GitHub Desktop |
