import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const divulgacion = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/divulgacion" }),
  schema: z.object({
    titulo: z.string(),
    descripcion: z.string(),
    autor: z.string(),
    fecha: z.date(),
    imagen: z.string().optional(),
    etiquetas: z.array(z.string()).default([]),
    destacado: z.boolean().default(false),
  }),
});

const publicaciones = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/publicaciones" }),
  schema: z.object({
    titulo: z.string(),
    autores: z.array(z.string()),
    revista: z.string().optional(),
    anio: z.number(),
    doi: z.string().optional(),
    resumen: z.string(),
    tipo: z.enum(['articulo', 'tesis']),
    categoria: z.enum(['produccion', 'previa']).optional(),
    enlace: z.string().optional(),
    institucion: z.string().optional(),
    director: z.string().optional(),
    directorInstitucion: z.string().optional(),
  }),
});

export const collections = { divulgacion, publicaciones };
