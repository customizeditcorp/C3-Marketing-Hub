# TODO - C3 Marketing Hub

## 🔥 Esta Semana (Urgente)

### Módulo 1: Creativos para Ads - Fase Standalone

**Objetivo:** Resolver el cuello de botella de generación de imágenes para Meta Ads.

#### Tareas de Juan (Diseño)
- [ ] Crear cuenta Figma (gratis)
- [ ] Buscar templates Meta Ads en Figma Community
  - Buscar: "Meta Ads templates", "Facebook Instagram Ad templates"
  - Duplicar a su proyecto
- [ ] Instalar plugin Automator ($12/mes)
- [ ] Personalizar templates con identidad visual del primer cliente
  - Logo, colores, fuentes, estilo
  - Definir capas variables: headline, cta, background_image
- [ ] Documentar proceso para reutilizar con otros clientes

#### Tareas de Luis (Implementación)
- [ ] Agregar "Paso 2" a webapp de copys (generación de CSV)
  - Botón "Generar CSV para Imágenes"
  - Función que crea CSV con formato: headline, cta, background_image, logo_url
  - Descarga automática del archivo
  - Instrucciones para Juan
- [ ] Integrar generación de imagen base con Runway (opcional)
- [ ] Documentar flujo completo en GitHub

#### Tareas del Equipo
- [ ] Probar flujo completo con 1 cliente real
  - Luis: Genera copys (Paso 1)
  - Luis: Genera CSV (Paso 2)
  - Juan: Usa CSV en Figma + Automator
  - Juan: Exporta 18 imágenes a Google Drive
  - Carlos: Carga imágenes a Meta Business Suite
- [ ] Validar que funciona end-to-end
- [ ] Documentar problemas y ajustes necesarios

**Deadline:** Viernes de esta semana  
**Resultado esperado:** Cuello de botella resuelto, tiempo de Juan reducido de 4 horas a 9 minutos por campaña

---

## 📅 Próximo Mes (4 semanas)

### C3 Hub v1 - Sistema Centralizado

**Objetivo:** Crear interfaz unificada que integre onboarding y generación de creativos.

#### Semana 1: Arquitectura y Setup
- [ ] **Luis:** Crear proyecto C3 Hub en Lovable
- [ ] **Luis:** Diseñar estructura de base de datos (Supabase)
  - Tabla: clientes
  - Tabla: campanas
  - Tabla: copys
- [ ] **Luis:** Crear dashboard básico con selector de clientes y navegador de módulos

#### Semana 2: Módulo 0 - Onboarding
- [ ] **Luis:** Migrar 6 GPTs a Claude Skills
  - Skill 1: Brief Empresa
  - Skill 2: Buyer Persona
  - Skill 3: Oferta SEO Local
  - Skill 4: Oferta Ads
- [ ] **Luis:** Crear interfaz de onboarding en C3 Hub
  - Formulario para brief inicial
  - Flujo secuencial de los 4 Skills
  - Botones "Aprobar" y "Modificar" en cada paso
- [ ] **Luis:** Guardar resultados en Supabase (cliente_data.json)

#### Semana 3: Módulo 1 - Creativos Ads (Integrado)
- [ ] **Luis:** Migrar webapp de copys al C3 Hub
  - Copiar lógica de generación de copys
  - Adaptar para leer de Supabase
  - Integrar Paso 1 (copys) y Paso 2 (CSV)
- [ ] **Luis:** Conectar Módulo 1 con Módulo 0
  - Leer datos del cliente automáticamente
  - No requerir input manual de información
- [ ] **Juan:** Validar que templates de Figma funcionan con el nuevo flujo

#### Semana 4: Testing y Refinamiento
- [ ] **Equipo:** Probar flujo completo con 3 clientes reales
- [ ] **Equipo:** Recoger feedback y ajustar
- [ ] **Luis:** Documentar sistema completo
- [ ] **Luis:** Capacitar a Juan y Carlos en uso del C3 Hub

**Deadline:** 4 semanas desde inicio  
**Resultado esperado:** C3 Hub v1 operativo con Onboarding y Ads integrados

---

## 🔮 Futuro (Activar Cuando se Necesite)

### Módulo 2: Posts Sociales (Instagram, Facebook, TikTok)

**Tiempo estimado:** 1 semana

- [ ] **Juan:** Buscar templates para posts sociales en Figma Community
- [ ] **Juan:** Personalizar templates con identidad visual
- [ ] **Luis:** Crear nueva sección "Posts Sociales" en C3 Hub
- [ ] **Luis:** Adaptar generación de copys para formato de posts
- [ ] **Luis:** Generar CSV específico para posts
- [ ] **Equipo:** Probar con 1 cliente

**Formatos a cubrir:**
- Instagram Feed (1080x1080)
- Instagram Story (1080x1920)
- Instagram Reel (1080x1920)
- Facebook Post (1200x630)
- Facebook Story (1080x1920)
- TikTok (1080x1920)

---

### Módulo 3: Email Marketing

**Tiempo estimado:** 1 semana

- [ ] **Juan:** Buscar templates para email banners en Figma Community
- [ ] **Juan:** Personalizar templates
- [ ] **Luis:** Crear nueva sección "Email Marketing" en C3 Hub
- [ ] **Luis:** Adaptar generación de copys para emails
- [ ] **Luis:** Generar CSV específico para email
- [ ] **Equipo:** Probar con 1 cliente

**Formatos a cubrir:**
- Header de email (600x200)
- Banner principal (600x400)
- CTA button (variantes)

---

### Módulo 4: Google Business Profile (GBP)

**Tiempo estimado:** 1 semana

- [ ] **Juan:** Buscar templates para GBP posts en Figma Community
- [ ] **Juan:** Personalizar templates
- [ ] **Luis:** Crear nueva sección "GBP" en C3 Hub
- [ ] **Luis:** Adaptar generación de copys para GBP
- [ ] **Luis:** Generar CSV específico para GBP
- [ ] **Equipo:** Probar con 1 cliente

**Formatos a cubrir:**
- GBP Post (1200x900)
- GBP Offer (1200x900)
- GBP Event (1200x900)

---

### Fase 4: Automatización Total (Opcional)

**Solo si el paso manual de Juan se vuelve cuello de botella**

**Opción A: Migrar a Bannerbear API**
- [ ] **Juan:** Replicar templates de Figma en Bannerbear
- [ ] **Luis:** Reemplazar generación de CSV por llamadas a Bannerbear API
- [ ] **Luis:** C3 Hub genera imágenes directamente sin intervención de Juan
- [ ] **Luis:** Guardar en Google Drive automáticamente

**Costo:** $49/mes  
**Tiempo desarrollo:** 1 semana

**Opción B: Desarrollar Generador Custom con Fabric.js**
- [ ] **Luis:** Convertir templates de Figma a código (Fabric.js)
- [ ] **Luis:** Crear API interna de generación de imágenes
- [ ] **Luis:** C3 Hub llama a esta API
- [ ] **Luis:** Genera imágenes programáticamente

**Costo:** $0/mes  
**Tiempo desarrollo:** 2-3 semanas

---

## ✅ Completado

- [x] Arquitectura del sistema diseñada
- [x] Roadmap de implementación creado
- [x] Stack tecnológico definido y documentado
- [x] Análisis de IAs y optimización de costos
- [x] Análisis de stack audiovisual (Runway, ElevenLabs, etc.)
- [x] Guía práctica de qué IA usar para cada tarea
- [x] Repositorio GitHub creado y configurado
- [x] Documentación completa subida a GitHub
- [x] Integración de webapp de copys planificada

---

## 📊 Métricas de Éxito

### Fase 1 (Esta Semana)
- ✅ Tiempo de generación de imágenes: 4 horas → 9 minutos (96% reducción)
- ✅ Costo: $12/mes (Figma Automator)
- ✅ 1 cliente validado con flujo completo

### Fase 2 (Próximo Mes)
- ✅ Sistema centralizado operativo
- ✅ Onboarding automatizado (6 Skills)
- ✅ Datos estructurados y reutilizables
- ✅ 3 clientes usando C3 Hub

### Futuro
- ✅ Todos los canales cubiertos (Ads, Posts, Email, GBP)
- ✅ Escalabilidad: 100+ clientes sin contratar más personal
- ✅ ROI: 600-800% en ahorro de tiempo y costos

---

## 📝 Notas

- **Prioridad:** Resolver urgencia (Fase 1) antes de construir C3 Hub completo
- **Filosofía:** Modular y escalable, activar módulos según necesidad del cliente
- **Calidad:** Juan supervisa diseño base, automatización solo para variantes
- **Costos:** Empezar con $12/mes, escalar según necesidad

---

## 🔗 Enlaces Útiles

- **Repositorio:** https://github.com/customizeditcorp/C3-Marketing-Hub
- **Documentación completa:** Ver carpeta `/docs`
- **Webapp de copys (Manus):** [Link compartido]
- **Figma Community:** https://www.figma.com/community

---

**Última actualización:** 31 de octubre de 2025  
**Responsable:** Luis (con soporte de Manus AI)
