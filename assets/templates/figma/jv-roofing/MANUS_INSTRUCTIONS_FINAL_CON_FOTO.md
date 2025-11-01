# 🎨 INSTRUCCIONES FINALES PARA MANUS: Template JV Roofing "Trust Badge"

## CONTEXTO
Crear template Meta Ads Story (1080x1920) para JV Roofing Inc. compatible con AutoBulk.

---

## 📦 ARCHIVOS A USAR

### **Logos y Badges:**
1. **JV_ROOFING_LOGO.png** - Logo principal (solo iconografía, sin texto)
2. **GAF_Text.png** - Badge GAF Certified 20+ Yrs
3. **malerkey.png** - Badge Malarkey Certified Pro Contractor
4. **CSLB_Text.png** - Badge CSLB #1125194

### **Foto Placeholder:**
5. **222A2570.jpg** - Foto de trabajador con camisa naranja (background placeholder)
   - Esta es una foto REAL de trabajo de JV Roofing
   - Usar como ejemplo visual en el template
   - Será reemplazada con diferentes fotos vía CSV en AutoBulk

**Todos los archivos están disponibles y listos para importar.**

---

## 🎨 ESPECIFICACIONES DEL DISEÑO

### **Formato:**
- Dimensiones: 1080x1920 px (Instagram/Facebook Story)
- Orientación: Vertical

### **Paleta de Colores:**
- Azul Navy: #2E3A8C
- Rojo Acento: #E31E24
- Blanco: #FFFFFF
- Overlay oscuro para backgrounds: rgba(46, 58, 140, 0.4)

### **Fuentes:**
- Headlines: Montserrat Bold o Inter Bold
- Cuerpo: Montserrat Regular o Inter Regular
- Alternativa: Roboto

---

## 🏗️ ESTRUCTURA DEL TEMPLATE (Top to Bottom)

### **1. CAPA: background_image (FONDO COMPLETO)**
```
Nombre de capa: "background_image"
Tipo: Image placeholder rectangle
Dimensiones: 1080x1920 (full bleed)

IMPORTANTE - USAR ESTA FOTO COMO PLACEHOLDER:
- Archivo: 222A2570.jpg (trabajador con camisa naranja instalando tejas)
- Esta es una foto REAL de trabajo de JV Roofing
- Muestra profesionalismo y "owner-supervised quality"

Efecto sobre la foto:
- Overlay azul navy: rgba(46, 58, 140, 0.4) 
- Esto unifica la imagen con el branding
- Mejora legibilidad de texto blanco

Nota: Esta capa se reemplaza con CSV (diferentes fotos de proyectos)
```

---

### **2. LOGO JV (Fijo - Superior Izquierda)**
```
Archivo: JV_ROOFING_LOGO.png
Posición: X: 60px, Y: 60px desde top-left
Altura: ~100px (ajustar proporcionalmente)
Nota: Logo solo iconografía (casas), fondo transparente
      NO se modifica con AutoBulk (fijo)
```

---

### **3. SECCIÓN BADGES (Centro-Superior - Fijos)**

#### **Contenedor General:**
```
Posición: Centrado horizontalmente, Y: 600px desde top
Dimensiones contenedor: 900x500 px
Fondo: Blanco con 90% opacidad
Border-radius: 20px
Sombra: 0px 4px 12px rgba(0,0,0,0.15)
Padding interno: 30px
```

#### **Distribución Interna de Badges:**

**FILA 1: GAF + Malarkey (Lado a lado)**
```
┌─────────────────────────────────┐
│                                 │
│  ┌──────────┐    ┌──────────┐  │
│  │   GAF    │    │ Malarkey │  │
│  │  Badge   │    │  Badge   │  │
│  │          │    │          │  │
│  └──────────┘    └──────────┘  │
│                                 │
└─────────────────────────────────┘
```

**GAF Badge (Izquierda):**
- Archivo: GAF_Text.png
- Ancho: ~350px (mantener proporción)
- Posición: Izquierda del contenedor (margin: 20px)
- Mantener logo completo visible:
  * Logo GAF rojo
  * "CERTIFIED"
  * "Residential Roofing Contractor"
  * "20+ Yrs"

**Malarkey Badge (Derecha):**
- Archivo: malerkey.png
- Ancho: ~350px (mantener proporción)
- Posición: Derecha del contenedor (margin: 20px)
- Mantener logo completo visible:
  * Sello verde circular
  * "CERTIFIED PRO CONTRACTOR"
  * "MALARKEY ROOFING PRODUCTS"
  * "ESTD 1956"
  * "When It Matters"

**Separación:** 80px entre GAF y Malarkey

---

**FILA 2: CSLB (Centrado abajo)**
```
┌─────────────────────────────────┐
│          [GAF] [Malarkey]       │
│                                 │
│        ┌──────────────┐         │
│        │     CSLB     │         │
│        │   #1125194   │         │
│        └──────────────┘         │
└─────────────────────────────────┘
```

**CSLB Badge:**
- Archivo: CSLB_Text.png
- Ancho: ~300px (mantener proporción)
- Posición: Centrado horizontalmente
- Margen superior desde badges: 40px
- Mantener logo completo visible:
  * Logo CSLB (casa con herramientas)
  * "CONTRACTORS STATE LICENSE BOARD"
  * "CSLB #1125194"

---

### **4. CAPA: headline (TEXTO VARIABLE)**
```
Nombre de capa: "headline"
Tipo: Text layer
Posición: Centrado horizontalmente, Y: 1200px desde top
Ancho máximo: 900px (márgenes 90px)
Alineación: Centrado

Estilo:
- Fuente: Montserrat Bold / Inter Bold
- Tamaño: 72px
- Color: #FFFFFF (blanco)
- Stroke: 2px azul navy #2E3A8C (para legibilidad sobre foto)
- Interlineado: 1.2
- Máximo 2-3 líneas
- Text overflow: Auto-resize

Texto placeholder: "Professional Roof & Deck Inspection. Free!"

Nota: Se reemplaza con CSV (headlines de webapp)
```

---

### **5. CAPA: cta (BOTÓN CTA - VARIABLE)**
```
Nombre de capa: "cta"
Tipo: Text in button component
Posición: Centrado horizontalmente, Y: 1550px desde top
Dimensiones botón: 700x130 px

Estilo botón:
- Rectángulo redondeado (radius: 65px - fully rounded)
- Fondo: #E31E24 (rojo)
- Sombra: 0px 6px 16px rgba(227, 30, 36, 0.4)

Estilo texto:
- Fuente: Montserrat Bold / Inter Bold
- Tamaño: 48px
- Color: #FFFFFF (blanco)
- Centrado vertical y horizontal
- Letter-spacing: 1px
- Texto placeholder: "GET FREE QUOTE"

Nota: Solo el TEXTO se reemplaza con CSV
```

---

### **6. TELÉFONO (Fijo - Debajo del CTA)**
```
Posición: Centrado horizontalmente, Y: 1710px desde top
Contenido: "(805) 674-1383"
Estilo:
- Fuente: Montserrat Bold / Inter Bold
- Tamaño: 36px
- Color: #FFFFFF (blanco)
- Stroke: 1px azul navy (para legibilidad)
- Centrado

Nota: NO se modifica con AutoBulk (fijo)
```

---

### **7. LICENCIA (Opcional - Muy Abajo)**
```
Posición: Centrado horizontalmente, Y: 1860px desde top
Contenido: "Licensed & Insured • $2M Liability"
Estilo:
- Fuente: Montserrat Regular / Inter Regular
- Tamaño: 22px
- Color: #FFFFFF con 80% opacidad
- Centrado

Nota: NO se modifica con AutoBulk (fijo)
```

---

## 📐 JERARQUÍA DE CAPAS EN FIGMA

```
📁 Frame: "JV_Roofing_Trust_Badge_Story_v1"
   │
   ├── 📷 background_image [VARIABLE - AutoBulk]
   │
   ├── 🎨 Overlay_Navy (40% opacity)
   │
   ├── 🖼️ Logo_JV [FIJO]
   │
   ├── 📦 Badges_Container [FIJO]
   │   ├── Background_White (90% opacity, rounded)
   │   ├── 🏆 Badge_GAF [FIJO]
   │   ├── 🏆 Badge_Malarkey [FIJO]
   │   └── 🏛️ Badge_CSLB [FIJO]
   │
   ├── 📝 headline [VARIABLE - AutoBulk]
   │
   ├── 🔘 CTA_Button_Shape [FIJO]
   │   └── 📝 cta [VARIABLE - solo texto AutoBulk]
   │
   ├── 📞 Phone_Number [FIJO]
   │
   └── 📜 License_Text [FIJO]
```

---

## ✅ CHECKLIST PRE-EXPORTACIÓN

Antes de marcar como completo, verificar:

✅ Frame se llama: "JV_Roofing_Trust_Badge_Story_v1"

✅ Las 3 capas variables tienen nombres EXACTOS:
   - `background_image`
   - `headline`
   - `cta`

✅ Logo JV visible y bien posicionado (arriba izquierda)

✅ Los 3 badges están importados y visibles:
   - GAF (izquierda)
   - Malarkey (derecha)
   - CSLB (centrado abajo)

✅ Contenedor de badges tiene fondo blanco semi-transparente

✅ Badges son legibles y mantienen proporciones

✅ Headline tiene stroke para legibilidad sobre foto

✅ Botón CTA es prominente (rojo brillante)

✅ Teléfono es visible

✅ Paleta de colores JV aplicada (azul #2E3A8C, rojo #E31E24)

✅ Fuentes Montserrat o Inter aplicadas

✅ Todo está alineado y centrado correctamente

---

## 🎯 DETALLES IMPORTANTES

### **Badges Container:**
- El contenedor blanco semi-transparente es CRÍTICO
- Sin él, los badges se pierden sobre fotos oscuras
- Border-radius suave (20px) para look moderno
- Sombra sutil para profundidad

### **GAF + Malarkey Lado a Lado:**
- Doble certificación = doble impacto
- GAF = Instaladores certificados
- Malarkey = Productos premium certificados
- Ambos reconocibles en la industria

### **CSLB Centrado:**
- Licencia legal es must-have
- Centrado abajo para balance visual
- Número visible (#1125194)

### **Headline con Stroke:**
- Stroke azul navy garantiza legibilidad
- Funciona sobre fotos claras Y oscuras
- 72px es óptimo para móvil

---

## 📋 EJEMPLO DE CSV (Para Testing)

```csv
headline,cta,background_image
"Professional Roof & Deck Inspection. Free!","Book Now","https://example.com/roof1.jpg"
"20 Years of Excellence in Roofing","Call Now","https://example.com/roof2.jpg"
"GAF Certified Pros You Can Trust","Get Quote","https://example.com/roof3.jpg"
```

---

## 🚀 SIGUIENTE PASO DESPUÉS DE CREAR

1. Instalar plugin **AutoBulk** en Figma
2. Seleccionar frame "JV_Roofing_Trust_Badge_Story_v1"
3. AutoBulk → Load CSV de prueba
4. Generar variantes
5. Verificar que:
   - Background image cambia ✅
   - Headline cambia ✅
   - CTA text cambia ✅
   - Todo lo demás permanece fijo ✅

---

## 🎨 NOTAS FINALES DE DISEÑO

**Objetivo del template:**
- Generar confianza INMEDIATA
- Destacar certificaciones profesionales (GAF + Malarkey)
- Mostrar licencia legal (CSLB)
- CTA claro y prominente
- Compatible con múltiples mensajes

**Buyer Persona:**
- 45-64 años
- Propietarios San Luis Obispo County
- Valoran credenciales y experiencia
- Buscan contratistas confiables

**Uso previsto:**
- Campañas Meta Ads (Facebook/Instagram Stories)
- 5-10 variantes por campaña
- Diferentes headlines según ángulo
- Mismo branding profesional

---

## ✅ ENTREGABLES ESPERADOS

1. Frame completo en Figma
2. Screenshot preview del template
3. Confirmación de nombres de capas correctos
4. Template listo para AutoBulk

---

**¿Listo para crear el template?**

Todos los archivos están disponibles:
- JV_ROOFING_LOGO.png ✅
- GAF_Text.png ✅
- malerkey.png ✅
- CSLB_Text.png ✅

**Adelante con la creación!** 🚀
