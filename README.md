# Probabilidade B — Ambiente de Aprendizagem Interativo

Aplicação web para o ensino e estudo da disciplina **Probabilidade B** (Modelos Contínuos e Inferência), desenvolvida para a monitoria da disciplina IEE055.

O projeto cobre toda a ementa com tópicos teóricos interativos, um banco de exercícios resolvidos e um motor de revisão baseado em repetição espaçada.

---

## Funcionalidades

**Tópicos de Estudo**
Ementa completa da disciplina organizada em tópicos com suporte a equações matemáticas via KaTeX. Inclui variáveis aleatórias contínuas, função geradora de momentos, modelos contínuos, distribuição Normal, funções de variável aleatória e distribuições bivariadas.

**Banco de Exercícios**
Mais de 70 exercícios mapeados por tópico, dificuldade e origem (listas, provas, slides e livro). Cada exercício apresenta resolução passo a passo com revelação progressiva para estimular o esforço cognitivo antes de consultar a resposta.

**Revisão Diária**
Sistema de sugestão de conteúdo baseado na curva de esquecimento. O aplicativo indica quais tópicos revisar com base no histórico de autoavaliação do estudante.

**Visualizações Interativas**
Gráficos dinâmicos via Chart.js para explorar distribuições de probabilidade contínuas. O estudante pode ajustar parâmetros (média, desvio padrão, taxa) e observar o efeito sobre a densidade e a função de distribuição acumulada em tempo real.

---

## Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Framework | Astro 5 |
| Estilização | CSS Vanilla com design system em `global.css` |
| Renderização matemática | `remark-math` + `rehype-katex` |
| Gráficos | Chart.js |
| Conteúdo | Markdown + Astro Content Collections |
| Build | Vite (via Astro) |

---

## Estrutura do Repositório

```
APP_ENSINO_MONITORIA/
├── app/                        # Aplicação Astro
│   └── src/
│       ├── content/
│       │   ├── topicos/        # Teoria por tópico (Markdown)
│       │   ├── exercicios/     # Exercícios com resolução (Markdown)
│       │   └── revisao/        # Cheatsheets e resumos rápidos
│       ├── components/         # Componentes visuais e interativos
│       ├── layouts/            # Layout base da aplicação
│       └── pages/              # Rotas (início, tópicos, exercícios)
├── docs/                       # Documentação do projeto
│   └── guia-autoria.md         # Como adicionar conteúdo sem tocar em código
├── spec_kit/                   # Especificações e decisões de design
└── source/                     # Material-fonte original (HTMLs da disciplina)
```

---

## Como Rodar Localmente

Requisito: **Node.js v22 ou superior**.

```bash
# 1. Clone o repositório
git clone https://github.com/o-hugo/app_probabilidade_b_monitoria.git
cd APP_ENSINO_MONITORIA/app

# 2. Instale as dependências
npm install

# 3. Inicie o servidor de desenvolvimento
npm run dev
```

Acesse `http://localhost:4321` no navegador.

```bash
# Para gerar o build de produção
npm run build

# Para visualizar o build localmente antes de publicar
npm run preview
```

---

## Como Adicionar Conteúdo

Todo o conteúdo vive em arquivos Markdown dentro de `app/src/content/`. Não é necessário alterar código para adicionar tópicos ou exercícios.

Consulte o **[Guia de Autoria](docs/guia-autoria.md)** para instruções detalhadas sobre o formato dos arquivos, convenções de notação matemática e critérios de dificuldade.

### Exemplo rápido: novo exercício

```markdown
---
id: "lista02-q06-exp-ligacao"
titulo: "Duração Exponencial de Ligação"
topicos: ["exponencial", "funcao-sobrevivencia"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

A duração da ligação é $X \sim Exp(\lambda=1/10)$. Calcule...

## Passo 1: Identificar a distribuição

...
```

> O campo `solucao_verificada` deve permanecer `false` até que a resolução seja revisada. Exercícios não verificados exibem um aviso para o estudante.

---

## Deploy

O projeto é configurado para publicação estática via **GitHub Pages**. Qualquer push na branch `main` dispara o workflow de build e deploy automaticamente.

A aplicação publicada fica disponível em:
```
https://o-hugo.github.io/app_probabilidade_b_monitoria/
```

---

## Licença

O conteúdo matemático (exercícios e teoria) é baseado em material de domínio público originalmente disponibilizado pela UFSCar. O código-fonte da aplicação é de uso livre.
