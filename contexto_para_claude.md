# Contexto del Proyecto C3 Marketing Hub - Para Claude

## Quién Soy

Soy Luis, co-fundador de C3 Marketing, una agencia de marketing digital incipiente. Somos 3 personas:
- **Juan:** Diseñador gráfico profesional (branding e identidad visual)
- **Carlos:** Especialista en Google Ads y Meta Ads
- **Yo (Luis):** Ventas, implementación, AI, automatización

## Qué Hacemos

Ofrecemos servicios de marketing digital para negocios locales (principalmente roofing y servicios). Nuestros servicios incluyen:
- Google Ads y Meta Ads
- SEO local y Google Business Profile
- Creación de identidad visual
- Email marketing corporativo
- Websites y landing pages (usando Lovable y GHL)

## Nuestro Stack Tecnológico Actual

- **CRM:** GoHighLevel (GHL) con subcuentas por cliente
- **Onboarding:** 6 GPTs orquestados que generan: brief empresa, buyer persona, oferta SEO local, oferta ads
- **Copys:** Webapp en Manus AI que genera textos para Meta Ads
- **Websites:** Lovable para desarrollo rápido
- **Workflows:** GHL con automatizaciones

## El Problema Que Estamos Resolviendo

**Cuello de botella:** Juan tarda 4 horas generando manualmente 18 variantes de imágenes para cada campaña de Meta Ads (diferentes formatos: Stories, Feed, Reels, etc.).

**Solución:** Automatizar la generación de imágenes usando Figma + plugin AutoBulk + CSV.

## Lo Que Ya Hicimos Hoy (con Manus AI)

1. ✅ Diseñamos arquitectura completa del sistema C3 Marketing Hub
2. ✅ Creamos roadmap de implementación
3. ✅ Definimos stack tecnológico y costos
4. ✅ Configuramos repositorio GitHub: https://github.com/customizeditcorp/C3-Marketing-Hub
5. ✅ Creamos TODO.md con todas las tareas
6. ✅ Analizamos opciones de IAs (Claude, DeepSeek, Grok, etc.)
7. ✅ Setup de Figma:
   - Cuenta FREE creada
   - Template "Reeeads Ad Templates Library for Meta" duplicado
   - Plugin AutoBulk instalado

## Dónde Estoy Ahora

**Tengo abierto en Figma:**
- El template "Reeeads Ad templates library" (duplicado)
- Plugin AutoBulk instalado y listo para usar
- Necesito personalizar un template con mi branding

## Lo Que Necesito Que Me Ayudes

**Objetivo:** Personalizar un template de Figma para que pueda usarlo con AutoBulk y generar múltiples variantes automáticamente.

**Pasos específicos:**
1. Elegir un template apropiado del Reeeads (simple, con imagen de fondo + headline + CTA)
2. Duplicarlo para trabajar en una copia
3. Personalizar:
   - Logo (o ajustar el existente)
   - Colores de marca (para roofing: azules oscuros, grises, naranjas)
   - Fuentes profesionales (Montserrat, Inter, Roboto)
4. **IMPORTANTE:** Renombrar capas para que AutoBulk funcione:
   - Imagen de fondo → "background_image"
   - Texto del headline → "headline"
   - Texto del CTA → "cta"
5. Guardar y verificar que está listo

**Después de esto:**
- Crearé un CSV con datos de prueba
- Usaré AutoBulk para generar variantes
- Validaré que funciona
- Enseñaré el proceso a Juan

## Información Técnica Importante

### **Cómo Funciona AutoBulk:**
1. Seleccionas un frame "master" (template personalizado)
2. Subes un archivo CSV con columnas que coincidan con nombres de capas
3. AutoBulk genera copias del frame, reemplazando contenido según el CSV
4. Exportas todas las variantes

### **Formato del CSV:**
```csv
headline,cta,background_image
"¿Tu techo necesita reparación?","Cotiza Gratis","https://ejemplo.com/imagen.jpg"
"Techos de calidad garantizada","Llama Ahora","https://ejemplo.com/imagen2.jpg"
```

### **Nombres de Capas Críticos:**
- **background_image:** La capa de imagen de fondo
- **headline:** El texto principal del ad
- **cta:** El texto del botón o call-to-action

Estos nombres DEBEN coincidir exactamente con las columnas del CSV.

## Mi Nivel de Experiencia

- **Figma:** Principiante (primera vez usándolo hoy)
- **Diseño:** Básico (no soy diseñador)
- **Desarrollo:** Intermedio-avanzado (manejo APIs, código, automatización)
- **AI:** Avanzado (uso múltiples IAs, orquestación, prompts)

## Estilo de Comunicación Que Prefiero

- Paso a paso, claro y directo
- Sin explicaciones largas innecesarias
- Dime exactamente dónde hacer click
- Si necesitas ver algo, pídeme screenshot
- Pregúntame qué veo en cada paso para validar

## Contexto del Negocio (Para Diseño)

**Industria:** Roofing (techos, reparación de techos)
**Audiencia:** Dueños de casas, propietarios de negocios locales
**Tono:** Profesional, confiable, accesible
**Colores recomendados:** 
- Primario: Azul oscuro (#1E3A8A) o Gris (#374151)
- Secundario: Naranja (#F97316) o Rojo (#DC2626)
- CTA: Color brillante que contraste

**Fuentes recomendadas:** Montserrat, Inter, Roboto, Open Sans

## Proyecto Completo (Para Contexto)

Este es solo el **Paso 1** de un proyecto más grande:

**Fase 1 (Esta semana - URGENTE):**
- Resolver cuello de botella de imágenes con Figma + AutoBulk

**Fase 2 (Próximo mes):**
- Desarrollar C3 Marketing Hub (interfaz centralizada)
- Integrar onboarding con Claude Skills
- Automatizar generación de copys + imágenes + landing pages

**Fase 3 (Futuro):**
- Módulos para Posts Sociales, Email Marketing, GBP
- Automatización total del workflow

## Repositorio GitHub

Todo está documentado en: https://github.com/customizeditcorp/C3-Marketing-Hub

Incluye:
- Arquitectura completa
- Roadmap detallado
- TODO.md con todas las tareas
- Análisis de IAs y costos
- Stack tecnológico

## Cómo Ayudarme Mejor

1. **Guíame paso a paso** en Figma
2. **Pregúntame qué veo** antes de avanzar
3. **Pídeme screenshots** si necesitas verificar algo
4. **Sé específico** con los clicks (ej: "Click en el panel izquierdo donde dice...")
5. **Valida cada paso** antes de continuar

## Mi Objetivo Inmediato

**Hoy:** Personalizar 1 template en Figma y probarlo con AutoBulk
**Esta semana:** Enseñar el proceso a Juan y escalar a los 18 formatos de Meta
**Próxima semana:** Integrar con mi webapp de copys para automatizar el CSV

## Pregunta Inicial Para Ti (Claude)

Estoy listo para empezar. ¿Puedes guiarme paso a paso para personalizar mi primer template en Figma?

Tengo el archivo "Reeeads Ad templates library" abierto. ¿Qué debo hacer primero?

---

**Nota:** Este contexto fue preparado por Manus AI para facilitar la transición a Claude para tareas específicas de diseño en Figma.
