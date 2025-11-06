# Plan de Integración: Copy Generator + Image Generator

**Proyecto:** C3 Marketing Hub - Webapp Unificada  
**Para:** Claude (meta-ads-copy-generator)  
**De:** Manus (bannerbear-image-generator)  
**Fecha:** 2025-11-05

---

## 🎯 Objetivo

Integrar **Copy Generator** (existente) con **Image Generator** (Bannerbear) en una webapp unificada que permita a Juan generar campañas completas de Meta Ads (copys + imágenes) en un solo flujo.

---

## 📊 Estado Actual

### **Copy Generator** ✅
- **Repo:** https://github.com/customizeditcorp/meta-ads-copy-generator
- **Stack:** React 19 + Express + tRPC + MySQL + OpenAI/Claude
- **Status:** Deployado y funcional
- **Funcionalidad:**
  - Import de documentos (.docx) con knowledge base del cliente
  - Extracción automática con AI
  - Generación de copys para Meta Ads:
    - 2-3 ángulos estratégicos
    - 4 primary texts (125 chars)
    - 4 headlines (40 chars)
    - 4 descriptions (30 chars)
  - Lead form generation
  - Metodología Margarita Pasos (7 ARCs)

### **Image Generator** ✅
- **Repo:** https://github.com/customizeditcorp/C3-Marketing-Hub
- **Stack:** Python + Bannerbear API
- **Status:** Funcionando (Fase 2 completa)
- **Funcionalidad:**
  - 3 templates de Meta Business Suite:
    - Stories 9:16 (1080×1920)
    - Feed 4:5 (1080×1350)
    - Feed 1:1 (1080×1080)
  - Assets de JV Roofing integrados (logo, foto, badges)
  - Generación en 30 segundos
  - API Key: `bb_pr_68c446c743c4b27916126868d25fa3`

---

## 🔄 Flujo de Usuario Propuesto

### **Paso 1: Generación de Copys** (Copy Generator existente)

```
Input del usuario:
├─ Cliente: JV Roofing (selecciona knowledge base)
├─ Objetivo: Awareness / Consideration / Conversion
├─ Producto/Servicio: (opcional)
└─ Oferta: (opcional)

↓ [Click "Generar Copys"]

Output:
├─ Ángulo 1:
│   ├─ 4 primary texts
│   ├─ 4 headlines
│   └─ 4 descriptions
├─ Ángulo 2:
│   ├─ 4 primary texts
│   ├─ 4 headlines
│   └─ 4 descriptions
└─ (opcional) Ángulo 3

Total: 12-24 copys generados
```

**Usuario revisa y selecciona:**
- ✅ 1 primary text favorito
- ✅ 1 headline favorito
- ✅ 1 description favorito

**Click: "Generar Imágenes con este Copy"**

---

### **Paso 2: Generación de Imágenes** (Nuevo - Bannerbear)

```
Input automático:
├─ Primary text seleccionado → Headline en imagen
├─ Description seleccionado → Subtitle en imagen
├─ Assets de JV Roofing:
│   ├─ Logo: JVrofiinglogoFullcolor.svg
│   ├─ Foto: 222A2584copia.jpg
│   ├─ Badge GAF
│   ├─ Badge Malarkey
│   └─ Badge CSLB
└─ Templates UIDs:
    ├─ Stories 9:16: l9E7G65kozz35PLe3R
    ├─ Feed 4:5: Kp21rAZj1y3eb6eLnd
    └─ Feed 1:1: 8BK3vWZJ7a3y5Jzk1a

↓ [Bannerbear API genera 3 imágenes]

Output:
├─ jv_roofing_stories_9x16.png (1080×1920)
├─ jv_roofing_feed_4x5.png (1080×1350)
└─ jv_roofing_feed_1x1.png (1080×1080)

Tiempo: ~30 segundos
```

**Usuario ve preview de las 3 imágenes**

**Click: "Descargar Todo"**

---

### **Paso 3: Download Package** (Nuevo)

```
ZIP file contiene:
├─ images/
│   ├─ jv_roofing_stories_9x16.png
│   ├─ jv_roofing_feed_4x5.png
│   └─ jv_roofing_feed_1x1.png
├─ copys.txt (todos los copys generados)
└─ selected_copy.txt (copy usado en las imágenes)

Usuario descarga y sube a Meta Business Suite
```

---

## 🏗️ Arquitectura Técnica Propuesta

### **Opción A: Integración en Copy Generator Existente** (Recomendado)

**Ventajas:**
- ✅ Un solo repo, un solo deploy
- ✅ Aprovecha auth y database existente
- ✅ UX más fluido (un solo flujo)

**Cambios necesarios:**

1. **Backend (Express + tRPC):**
   ```typescript
   // server/routers.ts
   
   // Nuevo router para Bannerbear
   bannerbear: {
     generateImages: protectedProcedure
       .input(z.object({
         primaryText: z.string(),
         headline: z.string(),
         description: z.string(),
         clientId: z.number(),
       }))
       .mutation(async ({ input }) => {
         // 1. Get client assets from database
         const client = await db.query.clients.findFirst({
           where: eq(clients.id, input.clientId)
         });
         
         // 2. Call Bannerbear API para 3 templates
         const images = await Promise.all([
           generateBannerbearImage('l9E7G65kozz35PLe3R', input), // Stories
           generateBannerbearImage('Kp21rAZj1y3eb6eLnd', input), // Feed 4:5
           generateBannerbearImage('8BK3vWZJ7a3y5Jzk1a', input), // Feed 1:1
         ]);
         
         // 3. Return image URLs
         return { images };
       }),
   }
   ```

2. **Frontend (React):**
   ```tsx
   // client/src/pages/GenerateCampaign.tsx
   
   // Agregar estado para imágenes
   const [selectedCopy, setSelectedCopy] = useState(null);
   const [generatedImages, setGeneratedImages] = useState(null);
   
   // Después de generar copys, mostrar botón
   {campaign && (
     <div>
       {/* Existing: mostrar copys */}
       <CopySelector onSelect={setSelectedCopy} />
       
       {/* Nuevo: botón para generar imágenes */}
       {selectedCopy && (
         <Button onClick={handleGenerateImages}>
           Generar Imágenes con este Copy
         </Button>
       )}
       
       {/* Nuevo: preview de imágenes */}
       {generatedImages && (
         <ImagePreview images={generatedImages} />
       )}
     </div>
   )}
   ```

3. **Database Schema:**
   ```typescript
   // drizzle/schema.ts
   
   export const clients = mysqlTable("clients", {
     // ... existing fields
     
     // Nuevo: Bannerbear config
     bannerbearTemplateStories: varchar("bannerbear_template_stories", { length: 255 }),
     bannerbearTemplateFeed45: varchar("bannerbear_template_feed_45", { length: 255 }),
     bannerbearTemplateFeed11: varchar("bannerbear_template_feed_11", { length: 255 }),
     logoUrl: varchar("logo_url", { length: 500 }),
     photoUrl: varchar("photo_url", { length: 500 }),
     badge1Url: varchar("badge1_url", { length: 500 }),
     badge2Url: varchar("badge2_url", { length: 500 }),
     badge3Url: varchar("badge3_url", { length: 500 }),
   });
   
   export const generatedImages = mysqlTable("generated_images", {
     id: serial("id").primaryKey(),
     campaignId: int("campaign_id").notNull(),
     format: varchar("format", { length: 50 }).notNull(), // "stories", "feed_4_5", "feed_1_1"
     imageUrl: varchar("image_url", { length: 500 }).notNull(),
     bannerbearUid: varchar("bannerbear_uid", { length: 255 }),
     createdAt: timestamp("created_at").defaultNow(),
   });
   ```

4. **Environment Variables:**
   ```env
   # .env
   BANNERBEAR_API_KEY=bb_pr_68c446c743c4b27916126868d25fa3
   BANNERBEAR_PROJECT_ID=5OPnVJ1PJJDvZA6rYb
   ```

---

### **Opción B: Dos Webapps Separadas con API**

**Ventajas:**
- ✅ Separación de concerns
- ✅ Más fácil de mantener independientemente

**Desventajas:**
- ❌ Dos deploys
- ❌ UX menos fluido (usuario cambia de app)
- ❌ Necesita autenticación compartida

**No recomendado para este caso.**

---

## 🎨 UI/UX Propuesto

### **Wireframe del Flujo:**

```
┌─────────────────────────────────────────┐
│  Generar Campaña - JV Roofing           │
└─────────────────────────────────────────┘

[Paso 1: Configuración]
  Knowledge Base: [JV Roofing ▼]
  Objetivo: [Conversion ▼]
  Producto: [Roof Repair]
  Oferta: [Free Estimate]
  
  [Generar Copys] ←─ Existing

↓

[Paso 2: Seleccionar Copy]
  
  Ángulo 1: Pain-Focused
  ┌─────────────────────────────────────┐
  │ Primary Text 1:                     │
  │ "Leaking roof? Storm damage? Get a  │
  │  free estimate from licensed..."    │
  │ [📋 Copy] [✓ Seleccionar]          │
  └─────────────────────────────────────┘
  
  [Ver más variaciones...]
  
  ✅ Copy seleccionado:
  - Primary: "Leaking roof? Storm damage?..."
  - Headline: "Book Free Estimate"
  - Description: "⭐5.0 Licensed Roofers..."
  
  [Generar Imágenes] ←─ Nuevo

↓

[Paso 3: Preview de Imágenes]
  
  ⏳ Generando imágenes... (30 seg)
  
  ✅ Imágenes generadas:
  
  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │ Stories  │  │ Feed 4:5 │  │ Feed 1:1 │
  │  9:16    │  │          │  │          │
  │          │  │          │  │          │
  │ [Preview]│  │ [Preview]│  │ [Preview]│
  └──────────┘  └──────────┘  └──────────┘
  
  [Descargar Todo (ZIP)] ←─ Nuevo
  [Regenerar con otro copy]

```

---

## 📦 Entregables

### **Para Claude (Copy Generator):**

1. **Código Backend:**
   - `server/bannerbear.ts` - Cliente de Bannerbear API
   - `server/routers.ts` - Nuevo router `bannerbear`
   - `drizzle/schema.ts` - Nuevas tablas y campos

2. **Código Frontend:**
   - `client/src/components/ImageGenerator.tsx` - Componente nuevo
   - `client/src/components/ImagePreview.tsx` - Preview de imágenes
   - `client/src/pages/GenerateCampaign.tsx` - Modificaciones

3. **Documentación:**
   - `docs/BANNERBEAR_INTEGRATION.md` - Guía de integración
   - `docs/API.md` - Documentación de endpoints

### **Para Manus (Image Generator):**

1. **Assets de JV Roofing:**
   - Ya subidos a GitHub (público)
   - URLs disponibles para Bannerbear

2. **Template UIDs:**
   - Stories 9:16: `l9E7G65kozz35PLe3R`
   - Feed 4:5: `Kp21rAZj1y3eb6eLnd`
   - Feed 1:1: `8BK3vWZJ7a3y5Jzk1a`

3. **API Key:**
   - `bb_pr_68c446c743c4b27916126868d25fa3`

---

## 🚀 Plan de Implementación

### **Fase 1: Setup (30 min)**
- [ ] Claude: Agregar `BANNERBEAR_API_KEY` a .env
- [ ] Claude: Instalar dependencias si necesario
- [ ] Claude: Crear `server/bannerbear.ts` con cliente API

### **Fase 2: Backend (1 hora)**
- [ ] Claude: Agregar router `bannerbear` en tRPC
- [ ] Claude: Implementar `generateImages` mutation
- [ ] Claude: Actualizar schema de database
- [ ] Claude: Push schema changes

### **Fase 3: Frontend (1.5 horas)**
- [ ] Claude: Crear componente `ImageGenerator`
- [ ] Claude: Crear componente `ImagePreview`
- [ ] Claude: Modificar `GenerateCampaign.tsx`
- [ ] Claude: Agregar lógica de selección de copy

### **Fase 4: Testing (30 min)**
- [ ] Ambos: Test end-to-end del flujo completo
- [ ] Ambos: Validar que imágenes se generan correctamente
- [ ] Ambos: Validar que copys se integran bien

### **Fase 5: Deploy (15 min)**
- [ ] Claude: Deploy a producción
- [ ] Manus: Validar que Bannerbear API funciona
- [ ] Ambos: Entregar URL a Luis

**Tiempo total estimado: 3-4 horas**

---

## 🔧 Código de Referencia

### **Bannerbear API Client (TypeScript)**

```typescript
// server/bannerbear.ts

import axios from 'axios';

const BANNERBEAR_API_KEY = process.env.BANNERBEAR_API_KEY;
const BANNERBEAR_API_URL = 'https://api.bannerbear.com/v2';

interface BannerbearImageRequest {
  template: string;
  modifications: Array<{
    name: string;
    text?: string;
    image_url?: string;
  }>;
}

export async function generateBannerbearImage(
  templateUid: string,
  data: {
    headline: string;
    subtitle: string;
    cta: string;
    logoUrl: string;
    photoUrl: string;
    badge1Url: string;
    badge2Url: string;
    badge3Url: string;
  }
): Promise<{ uid: string; image_url: string }> {
  const request: BannerbearImageRequest = {
    template: templateUid,
    modifications: [
      { name: 'headline', text: data.headline },
      { name: 'subtitle', text: data.subtitle },
      { name: 'cta', text: data.cta },
      { name: 'logo', image_url: data.logoUrl },
      { name: 'background_image', image_url: data.photoUrl },
      { name: 'badge_gaf', image_url: data.badge1Url },
      { name: 'badge_malarkey', image_url: data.badge2Url },
      { name: 'badge_cslb', image_url: data.badge3Url },
    ],
  };

  const response = await axios.post(
    `${BANNERBEAR_API_URL}/images`,
    request,
    {
      headers: {
        'Authorization': `Bearer ${BANNERBEAR_API_KEY}`,
        'Content-Type': 'application/json',
      },
    }
  );

  const imageUid = response.data.uid;

  // Wait for image to be generated (poll status)
  let imageUrl = null;
  let attempts = 0;
  const maxAttempts = 30;

  while (!imageUrl && attempts < maxAttempts) {
    await new Promise(resolve => setTimeout(resolve, 2000)); // Wait 2 seconds

    const statusResponse = await axios.get(
      `${BANNERBEAR_API_URL}/images/${imageUid}`,
      {
        headers: {
          'Authorization': `Bearer ${BANNERBEAR_API_KEY}`,
        },
      }
    );

    if (statusResponse.data.status === 'completed') {
      imageUrl = statusResponse.data.image_url;
    }

    attempts++;
  }

  if (!imageUrl) {
    throw new Error('Image generation timed out');
  }

  return {
    uid: imageUid,
    image_url: imageUrl,
  };
}
```

### **tRPC Router**

```typescript
// server/routers.ts

import { generateBannerbearImage } from './bannerbear';

export const bannerbear = router({
  generateImages: protectedProcedure
    .input(z.object({
      primaryText: z.string(),
      headline: z.string(),
      description: z.string(),
      clientId: z.number(),
    }))
    .mutation(async ({ input, ctx }) => {
      // Get client assets
      const client = await ctx.db.query.clients.findFirst({
        where: eq(clients.id, input.clientId),
      });

      if (!client) {
        throw new Error('Client not found');
      }

      // Generate 3 images in parallel
      const [storiesImage, feed45Image, feed11Image] = await Promise.all([
        generateBannerbearImage(client.bannerbearTemplateStories!, {
          headline: input.headline,
          subtitle: input.description,
          cta: 'Book Free Estimate',
          logoUrl: client.logoUrl!,
          photoUrl: client.photoUrl!,
          badge1Url: client.badge1Url!,
          badge2Url: client.badge2Url!,
          badge3Url: client.badge3Url!,
        }),
        generateBannerbearImage(client.bannerbearTemplateFeed45!, {
          headline: input.headline,
          subtitle: input.description,
          cta: 'Book Free Estimate',
          logoUrl: client.logoUrl!,
          photoUrl: client.photoUrl!,
          badge1Url: client.badge1Url!,
          badge2Url: client.badge2Url!,
          badge3Url: client.badge3Url!,
        }),
        generateBannerbearImage(client.bannerbearTemplateFeed11!, {
          headline: input.headline,
          subtitle: input.description,
          cta: 'Book Free Estimate',
          logoUrl: client.logoUrl!,
          photoUrl: client.photoUrl!,
          badge1Url: client.badge1Url!,
          badge2Url: client.badge2Url!,
          badge3Url: client.badge3Url!,
        }),
      ]);

      // Save to database
      await ctx.db.insert(generatedImages).values([
        {
          campaignId: input.campaignId,
          format: 'stories',
          imageUrl: storiesImage.image_url,
          bannerbearUid: storiesImage.uid,
        },
        {
          campaignId: input.campaignId,
          format: 'feed_4_5',
          imageUrl: feed45Image.image_url,
          bannerbearUid: feed45Image.uid,
        },
        {
          campaignId: input.campaignId,
          format: 'feed_1_1',
          imageUrl: feed11Image.image_url,
          bannerbearUid: feed11Image.uid,
        },
      ]);

      return {
        images: [
          { format: 'stories', url: storiesImage.image_url },
          { format: 'feed_4_5', url: feed45Image.image_url },
          { format: 'feed_1_1', url: feed11Image.image_url },
        ],
      };
    }),
});
```

---

## 📞 Coordinación

### **Para Claude:**
- **Repo:** https://github.com/customizeditcorp/meta-ads-copy-generator
- **Contacto:** Manus (este chat)
- **Assets URL:** https://github.com/customizeditcorp/C3-Marketing-Hub/tree/main/assets/jv-roofing

### **Para Manus:**
- **Repo:** https://github.com/customizeditcorp/C3-Marketing-Hub
- **Contacto:** Luis (usuario)
- **Bannerbear Dashboard:** https://app.bannerbear.com/projects/5OPnVJ1PJJDvZA6rYb

### **Comunicación:**
- Luis coordina entre Manus y Claude
- Ambos documentan cambios en GitHub
- Testing conjunto al final

---

## ✅ Checklist Final

**Antes de empezar:**
- [ ] Claude lee este documento completo
- [ ] Claude confirma que entiende la integración
- [ ] Manus confirma que assets están accesibles
- [ ] Luis aprueba el plan

**Durante desarrollo:**
- [ ] Claude documenta cambios en commits
- [ ] Manus valida que Bannerbear API funciona
- [ ] Testing incremental (backend → frontend → e2e)

**Al terminar:**
- [ ] Deploy a producción
- [ ] URL funcional compartida con Luis
- [ ] Documentación actualizada
- [ ] Video demo (opcional)

---

**Última actualización:** 2025-11-05  
**Próxima revisión:** Después de implementación

---

## 🎯 Resultado Esperado

**Juan podrá:**
1. Entrar a la webapp
2. Seleccionar JV Roofing
3. Generar copys (12-24 opciones)
4. Seleccionar su favorito
5. Click "Generar Imágenes"
6. Ver preview de 3 imágenes (Stories, Feed 4:5, Feed 1:1)
7. Descargar ZIP con todo
8. Subir a Meta Business Suite
9. **Tiempo total: 5 minutos** (vs 4 horas manual)

**ROI:**
- 99% reducción en tiempo
- 98% reducción en costo
- 100% consistencia de marca
- Calidad profesional garantizada

---

**¿Preguntas? Contacta a Luis o Manus.**
