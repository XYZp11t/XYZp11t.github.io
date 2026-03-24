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
    galeria: z.object({
      ruta: z.string(),
      titulo: z.string().optional(),
    }).optional(),
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
    nivel: z.enum(['licenciatura', 'maestria', 'doctorado']).optional(),
  }),
});

// Schema para el perfil de un investigador
const perfilInvestigadorSchema = z.object({
  cargo: z.string().default(''),
  areaEstudio: z.string().default(''),
  oficina: z.string().default(''),
  telefono: z.string().default(''),
  email: z.string().default(''),
});

// Schema base para un investigador
const investigadorSchema = z.object({
  nombre: z.string(),
  imagen: z.string().default(''),
  cv: z.string().default(''), // Ruta al archivo CV (ej: "/CVs/cv-nombre.pdf")
  perfil: perfilInvestigadorSchema.default({
    cargo: '',
    areaEstudio: '',
    oficina: '',
    telefono: '',
    email: '',
  }),
  esEncargado: z.boolean().default(false),
  orden: z.number().default(999),
});

// Schema para grupos de investigadores
const grupoInvestigadoresSchema = z.object({
  institucion: z.string(),
  siglas: z.string(),
  tipo: z.enum(['interno', 'externo']),
  orden: z.number().default(999),
});

const colaboradoresInternos = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/colaboradores/internos" }),
  schema: investigadorSchema,
});

// Schema para colaboradores externos (con grupo explícito)
const investigadorExternoSchema = investigadorSchema.extend({
  grupoSiglas: z.string(), // Siglas del grupo al que pertenece (ej: "IGUM", "IRYA")
});

const colaboradoresExternos = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/colaboradores/externos" }),
  schema: investigadorExternoSchema,
});

const gruposColaboradores = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/colaboradores/grupos" }),
  schema: grupoInvestigadoresSchema,
});

export const collections = { 
  divulgacion, 
  publicaciones, 
  colaboradoresInternos, 
  colaboradoresExternos,
  gruposColaboradores,
};
