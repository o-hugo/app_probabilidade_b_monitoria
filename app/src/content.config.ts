import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const topicos = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/topicos" }),
  schema: z.object({
    id: z.string(),
    titulo: z.string(),
    ordem: z.number(),
    ementa_ref: z.string(),
    tags: z.array(z.string()).default([]),
    visualizador: z.string().optional(),
  }),
});

const exercicios = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/exercicios" }),
  schema: z.object({
    id: z.string(),
    titulo: z.string(),
    topicos: z.array(z.string()),
    dificuldade: z.enum(['baixa', 'media', 'alta']),
    origem: z.enum(['lista', 'lista-02', 'prova-3', 'slide', 'slides', 'livro', 'aula']),
    metodo: z.string().optional(),
    resposta_final: z.string().optional(),
    solucao_verificada: z.boolean().default(false),
  }),
});

const revisao = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/revisao" }),
  schema: z.object({
    id: z.string(),
    titulo: z.string(),
    topicos: z.array(z.string()),
    ordem: z.number().optional(),
  }),
});

export const collections = {
  topicos,
  exercicios,
  revisao,
};
