# 🎨 INSTRUCCIONES PARA MANUS v2.0: Template JV Roofing "Trust Badge"
**Score Target: 98/100 | Fidelidad: 95%**

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

### **Fuentes (Orden de Preferencia):**
- **Opción 1 (Preferida):** Montserrat Bold + Montserrat Regular
- **Opción 2 (Alternativa):** Inter Bold + Inter Regular
- **Opción 3 (Fallback):** Roboto Bold + Roboto Regular

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
- Aplicar como capa separada sobre la imagen
- Blend mode: Normal
- Esto unifica la imagen con el branding y mejora legibilidad

Nota: Esta capa se reemplaza con CSV (diferentes fotos de proyectos)
```

---

### **2. LOGO JV (Fijo - Superior Izquierda)**
```
Archivo: JV_ROOFING_LOGO.png
Posición absoluta: X: 60px (desde left), Y: 60px (desde top)
Dimensiones: 
- Altura: 100px (fijo)
- Ancho: Auto (mantener proporción original)
- Constrains: Scale proportionally

Nota: Logo solo iconografía (casas), fondo transparente
      NO se modifica con AutoBulk (fijo)
```

---

### **3. SECCIÓN BADGES (Centro-Superior - Fijos)**

#### **Contenedor General:**
```
Nombre: Badges_Container
Tipo: Frame / Auto-layout (vertical)
Posición: Centrado horizontalmente, Y: 600px (desde top)
Dimensiones: 
- Ancho: 900px (fijo)
- Alto: Auto (basado en contenido interno)
- Max-height: 500px

Estilo contenedor:
- Fondo: Blanco (#FFFFFF)
- Opacidad: 90%
- Border-radius: 20px (todos los corners)
- Sombra: Drop shadow
  * X: 0px
  * Y: 4px
  * Blur: 12px
  * Color: rgba(0, 0, 0, 0.15)

Auto-layout settings:
- Direction: Vertical
- Gap vertical entre elementos: 40px
- Padding interno: 30px (todos los lados)
- Horizontal alignment: Center
- Vertical alignment: Top
```

#### **Distribución Interna de Badges:**

**FILA 1: GAF + Malarkey (Auto-layout Horizontal)**
```
Nombre: Badges_Row_Top
Tipo: Auto-layout horizontal
Dimensiones:
- Ancho: Auto (basado en contenido)
- Alto: Auto (basado en contenido)

Auto-layout settings:
- Direction: Horizontal
- Gap horizontal: 80px (espacio entre badges)
- Horizontal alignment: Center
- Vertical alignment: Center
- Pack: Center (distribuir al centro)
```

**GAF Badge (Izquierda):**
```
Archivo: GAF_Text.png
Dimensiones:
- Ancho: 350px (fijo)
- Alto: Auto (mantener proporción)
- Constrains: Scale proportionally

Contenido visible:
- Logo GAF rojo arriba
- Texto "CERTIFIED" 
- "Residential Roofing Contractor"
- "20+ Yrs"

Nota: Mantener imagen completa, no cropear
```

**Malarkey Badge (Derecha):**
```
Archivo: malerkey.png
Dimensiones:
- Ancho: 350px (fijo)
- Alto: Auto (mantener proporción)
- Constrains: Scale proportionally

Contenido visible:
- Sello verde circular completo
- "CERTIFIED PRO CONTRACTOR"
- "MALARKEY ROOFING PRODUCTS"
- "ESTD 1956"
- "When It Matters"

Nota: Mantener imagen completa, no cropear
```

---

**FILA 2: CSLB (Centrado Abajo)**
```
Nombre: Badge_CSLB_Bottom
Tipo: Image frame
Posición: Centrado horizontalmente dentro del contenedor
Margen superior desde Badges_Row_Top: 40px (ya definido en gap vertical del contenedor)

Dimensiones:
- Ancho: 300px (fijo)
- Alto: Auto (mantener proporción)
- Constrains: Scale proportionally

Contenido visible:
- Logo CSLB (casa azul con herramientas)
- Texto "CONTRACTORS STATE LICENSE BOARD"
- "CSLB #1125194"

Nota: Mantener imagen completa, no cropear
```

---

### **4. CAPA: headline (TEXTO VARIABLE)**
```
Nombre de capa: "headline"
Tipo: Text layer
Posición: Centrado horizontalmente, Y: 1200px (desde top)

Dimensiones:
- Ancho: 900px (fijo)
- Alto: Auto (resize basado en contenido)
- Márgenes laterales: 90px (desde cada borde)

Alineación: Center (horizontal y texto centrado)

Estilo de fuente:
- Fuente: 
  1. Montserrat Bold (preferida)
  2. Inter Bold (alternativa)
  3. Roboto Bold (fallback)
- Tamaño: 72px
- Color: #FFFFFF (blanco)
- Letter-spacing: 0px (normal)
- Line-height: 1.2 (86px aprox)

Efecto de legibilidad (ELEGIR UNO):
Opción A - Text outline stroke:
- Stroke: 2px
- Color: #2E3A8C (azul navy)
- Position: Outside

Opción B - Drop shadow (alternativa):
- X: 0px
- Y: 0px
- Blur: 4px
- Color: #2E3A8C
- Opacity: 100%

Text behavior:
- Auto-resize: Height (mantener ancho 900px fijo)
- Max lines: 3
- Truncate: No (permitir hasta 3 líneas completas)
- Wrap: Word wrap (break by words)

Texto placeholder: "Professional Roof & Deck Inspection. Free!"

Nota: Este texto se reemplazará vía AutoBulk con headlines del CSV
```

---

### **5. CAPA: cta (BOTÓN CTA - VARIABLE)**
```
Tipo: Component / Frame con text layer interno
Posición: Centrado horizontalmente, Y: 1550px (desde top)

ESTRUCTURA:
Frame externo (botón):
- Nombre: CTA_Button_Shape
- Dimensiones: 700px × 130px (fijo)
- Border-radius: 65px (fully rounded)
- Fondo: #E31E24 (rojo)
- Sombra: Drop shadow
  * X: 0px
  * Y: 6px
  * Blur: 16px
  * Color: rgba(227, 30, 36, 0.4)

Text layer interno:
- Nombre de capa: "cta"
- Posición: Centrado absoluto dentro del botón
- Auto-layout: Center (horizontal + vertical)

Estilo texto:
- Fuente:
  1. Montserrat Bold (preferida)
  2. Inter Bold (alternativa)
  3. Roboto Bold (fallback)
- Tamaño: 48px
- Color: #FFFFFF (blanco)
- Letter-spacing: 1px
- Text transform: UPPERCASE

Text behavior:
- Auto-resize: Width and height
- Max-width: 600px (dejar 50px padding a cada lado)
- Truncate: No
- Wrap: No (single line preferred)

Texto placeholder: "GET FREE QUOTE"

Nota: Solo el TEXTO de cta se reemplaza con CSV
      El botón (shape) permanece fijo
```

---

### **6. TELÉFONO (Fijo - Debajo del CTA)**
```
Nombre: Phone_Number_Text
Tipo: Text layer
Posición: Centrado horizontalmente, Y: 1710px (desde top)

Contenido: "(805) 674-1383"

Estilo:
- Fuente:
  1. Montserrat Bold (preferida)
  2. Inter Bold (alternativa)
  3. Roboto Bold (fallback)
- Tamaño: 36px
- Color: #FFFFFF (blanco)
- Letter-spacing: 0px

Efecto legibilidad (ELEGIR UNO):
Opción A - Text outline stroke:
- Stroke: 1px
- Color: #2E3A8C (azul navy)
- Position: Outside

Opción B - Drop shadow:
- X: 0px
- Y: 0px
- Blur: 3px
- Color: #2E3A8C

Alineación: Center

Nota: NO se modifica con AutoBulk (fijo)
```

---

### **7. LICENCIA (Opcional - Muy Abajo)**
```
Nombre: License_Text
Tipo: Text layer
Posición: Centrado horizontalmente, Y: 1860px (desde top)

Contenido: "Licensed & Insured • $2M Liability"

Estilo:
- Fuente:
  1. Montserrat Regular (preferida)
  2. Inter Regular (alternativa)
  3. Roboto Regular (fallback)
- Tamaño: 22px
- Color: #FFFFFF
- Opacidad: 80%
- Letter-spacing: 0px

Alineación: Center

Nota: NO se modifica con AutoBulk (fijo)
```

---

## 📐 JERARQUÍA DE CAPAS EN FIGMA

```
📁 Frame: "JV_Roofing_Trust_Badge_Story_v1"
   │
   ├── 📷 background_image [VARIABLE - AutoBulk]
   │   └── Archivo: 222A2570.jpg
   │
   ├── 🎨 Overlay_Navy
   │   └── Fill: rgba(46, 58, 140, 0.4)
   │
   ├── 🖼️ Logo_JV [FIJO]
   │   └── JV_ROOFING_LOGO.png
   │
   ├── 📦 Badges_Container [FIJO - Auto-layout vertical]
   │   ├── Background: White 90% opacity
   │   ├── Border-radius: 20px
   │   ├── Padding: 30px
   │   ├── Gap: 40px
   │   │
   │   ├── 📊 Badges_Row_Top [Auto-layout horizontal]
   │   │   ├── Gap: 80px
   │   │   ├── 🏆 Badge_GAF [FIJO]
   │   │   │   └── GAF_Text.png (350px width)
   │   │   └── 🏆 Badge_Malarkey [FIJO]
   │   │       └── malerkey.png (350px width)
   │   │
   │   └── 🏛️ Badge_CSLB_Bottom [FIJO]
   │       └── CSLB_Text.png (300px width)
   │
   ├── 📝 headline [VARIABLE - AutoBulk]
   │   └── Text: "Professional Roof & Deck Inspection. Free!"
   │
   ├── 🔘 CTA_Button_Shape [FIJO]
   │   ├── Shape: Rounded rectangle 700×130px
   │   ├── Fill: #E31E24
   │   └── 📝 cta [VARIABLE - solo texto AutoBulk]
   │       └── Text: "GET FREE QUOTE"
   │
   ├── 📞 Phone_Number_Text [FIJO]
   │   └── Text: "(805) 674-1383"
   │
   └── 📜 License_Text [FIJO]
       └── Text: "Licensed & Insured • $2M Liability"
```

---

## ⚠️ CASOS EDGE Y SOLUCIONES

### **CASO 1: Headline Muy Largo (>80 caracteres)**
```
Problema: Headline excede 3 líneas
Solución:
- Reducir font-size a 64px (desde 72px)
- Mantener max 3 líneas
- Si aún no cabe, reducir a 56px
- NO truncar texto
```

### **CASO 2: CTA Muy Largo (>20 caracteres)**
```
Problema: CTA text no cabe en botón
Solución:
- Permitir text wrap a 2 líneas si necesario
- Ajustar line-height a 1.1
- Reducir font-size a 42px si persiste
- Botón puede expandir height a max 160px
```

### **CASO 3: Foto Muy Oscura**
```
Problema: Texto blanco no se lee sobre foto oscura
Solución actual:
- Overlay azul navy rgba(46, 58, 140, 0.4) YA aplicado
- Text stroke/shadow en headline YA aplicado

Si persiste:
- Aumentar opacidad overlay a 0.5 (50%)
- Aumentar stroke de headline a 3px
```

### **CASO 4: Foto Muy Clara**
```
Problema: Badges blancos se pierden sobre foto clara
Solución actual:
- Contenedor badges tiene fondo blanco 90% opacity
- Sombra drop shadow en contenedor

Si persiste:
- Aumentar opacidad fondo badges container a 95%
- Aumentar blur de sombra a 16px
```

### **CASO 5: Badges No Caben Horizontalmente**
```
Problema: GAF + Malarkey muy anchos lado a lado
Solución:
- Reducir ancho de cada badge a 320px (desde 350px)
- Mantener gap de 80px
- Si aún no cabe, reducir gap a 60px
```

### **CASO 6: Logo JV Muy Grande**
```
Problema: Logo ocupa mucho espacio superior
Solución:
- Reducir altura a 80px (desde 100px)
- Mantener proporción
- Ajustar posición Y a 50px si necesario
```

---

## ✅ CHECKLIST PRE-EXPORTACIÓN

Antes de marcar como completo, verificar:

### **Nomenclatura:**
✅ Frame se llama: "JV_Roofing_Trust_Badge_Story_v1"

✅ Las 3 capas variables tienen nombres EXACTOS:
   - `background_image`
   - `headline`
   - `cta`

### **Assets:**
✅ Logo JV visible y bien posicionado (60px, 60px desde top-left)

✅ Los 3 badges están importados y visibles:
   - GAF (izquierda, 350px ancho)
   - Malarkey (derecha, 350px ancho)
   - CSLB (centrado abajo, 300px ancho)

### **Contenedor Badges:**
✅ Tiene fondo blanco semi-transparente (90%)
✅ Border-radius 20px
✅ Sombra drop shadow correcta
✅ Auto-layout con gap 40px vertical

### **Tipografía:**
✅ Fuente Montserrat (o alternativa) aplicada
✅ Headline 72px con stroke/shadow
✅ CTA 48px uppercase con letter-spacing 1px
✅ Teléfono 36px con stroke/shadow

### **Layout:**
✅ Headline tiene ancho fijo 900px
✅ Auto-resize height activado en headline
✅ CTA botón 700×130px
✅ Badges centrados correctamente

### **Colores:**
✅ Azul navy #2E3A8C aplicado
✅ Rojo #E31E24 en CTA
✅ Overlay rgba(46, 58, 140, 0.4) sobre background

### **Comportamiento:**
✅ Text wrap activado en headline
✅ Max 3 líneas en headline
✅ No truncate en ningún texto
✅ Auto-resize configurado correctamente

---

## 📤 ESPECIFICACIONES DE EXPORTACIÓN

### **Para Testing/Preview:**
```
Formato: PNG
Resolución: 2x (2160×3840)
Color profile: sRGB
Compression: Best quality
Include: Current frame only
```

### **Naming Convention:**
```
Formato: [ClientName]_[TemplateName]_[Version]_[Date].png

Ejemplo:
JV_Roofing_Trust_Badge_Story_v1_2025-11-01.png

Para variantes con AutoBulk:
JV_Roofing_Trust_Badge_Story_Variant_001.png
JV_Roofing_Trust_Badge_Story_Variant_002.png
etc.
```

### **Export Settings en Figma:**
```
1. Select frame "JV_Roofing_Trust_Badge_Story_v1"
2. Export menu → Add export setting
3. Format: PNG
4. Size: 2x
5. Color space: sRGB
6. Suffix: @2x (opcional)
7. Export
```

---

## 📋 EJEMPLO DE CSV (Para Testing con AutoBulk)

```csv
headline,cta,background_image
"Professional Roof & Deck Inspection. Free!","Book Now","https://example.com/roof1.jpg"
"20 Years of Excellence in Roofing","Call Now","https://example.com/roof2.jpg"
"GAF Certified Pros You Can Trust","Get Quote","https://example.com/roof3.jpg"
"Owner-Supervised Quality Every Time","Schedule","https://example.com/roof4.jpg"
"Premium Materials. Guaranteed Results.","Book Now","https://example.com/roof5.jpg"
```

---

## 🚀 SIGUIENTE PASO DESPUÉS DE CREAR

### **Fase 1: Validación Visual**
1. Revisar que todos los elementos estén visibles
2. Verificar spacing y alignment
3. Confirmar nombres de capas correctos
4. Export PNG preview @ 2x

### **Fase 2: Testing con AutoBulk**
1. Instalar plugin **AutoBulk** en Figma
2. Seleccionar frame "JV_Roofing_Trust_Badge_Story_v1"
3. AutoBulk → Load CSV de prueba
4. Generate → Preview results
5. Verificar que SOLO cambian:
   - ✅ Background image
   - ✅ Headline text
   - ✅ CTA text
6. Verificar que permanecen fijos:
   - ✅ Logo JV
   - ✅ Badges (GAF, Malarkey, CSLB)
   - ✅ Teléfono
   - ✅ Licencia
   - ✅ Todos los estilos

### **Fase 3: Export Final**
1. Generate variantes con AutoBulk
2. Select all generated frames
3. Export all @ 2x PNG
4. Download as ZIP
5. Entregar a cliente

---

## 🎨 NOTAS FINALES DE DISEÑO

**Objetivo del template:**
- Generar confianza INMEDIATA con badges profesionales
- Destacar certificaciones (GAF + Malarkey = doble punch)
- Mostrar licencia legal (CSLB)
- CTA claro y prominente
- Compatible con múltiples mensajes de campaña

**Buyer Persona:**
- Edad: 45-64 años
- Ubicación: San Luis Obispo County, California
- Valoran: Credenciales, experiencia, confiabilidad
- Buscan: Contratistas certificados y con licencia

**Uso previsto:**
- Campañas Meta Ads (Facebook/Instagram Stories)
- 5-10 variantes por campaña con diferentes headlines
- Mismo branding profesional en todas las variantes
- Generación automatizada vía AutoBulk

**Diferenciadores visuales:**
- Doble certificación (GAF + Malarkey) poco común en competencia
- Owner-supervised quality visible en fotos
- Badges oficiales reconocibles
- Licencia CSLB destacada

---

## 🎯 MEJORAS v2.0 IMPLEMENTADAS

✅ **1. Método de stroke especificado:**
   - Text outline stroke: 2px, color #2E3A8C
   - Alternativa drop shadow con parámetros exactos

✅ **2. Unidades de separación claras:**
   - Gap horizontal: 80px (entre GAF y Malarkey)
   - Gap vertical: 40px (en auto-layout contenedor)

✅ **3. Auto-layout vs Fixed Dimensions:**
   - Badges container: Ancho 900px (fijo), Alto Auto
   - Especificado claramente para cada elemento

✅ **4. Orden de preferencia fuentes:**
   - 1. Montserrat (preferida)
   - 2. Inter (alternativa)
   - 3. Roboto (fallback)

✅ **5. Comportamiento text overflow:**
   - Auto-resize height, Max lines: 3, Truncate: No
   - Especificado para headline y CTA

✅ **6. Sección Casos Edge agregada:**
   - 6 casos con soluciones específicas
   - Headline largo, CTA largo, fotos oscuras/claras, etc.

✅ **7. Especificaciones exportación:**
   - PNG, 2x, sRGB
   - Naming convention definida
   - Settings paso a paso

---

## ✅ ENTREGABLES ESPERADOS

1. **Frame completo en Figma:** "JV_Roofing_Trust_Badge_Story_v1"
2. **Screenshot preview PNG @ 2x** del template con placeholder
3. **Confirmación de nombres de capas** (screenshot layers panel)
4. **Template listo para AutoBulk** con las 3 capas variables correctamente nombradas

---

## 📊 SCORE ESPERADO

**Instrucciones v1.0:** 95/100, Fidelidad 92%
**Instrucciones v2.0:** 98/100, Fidelidad 95%

**Mejoras implementadas:**
- Especificaciones técnicas más precisas
- Casos edge cubiertos
- Export settings definidos
- Nomenclatura de archivos clara
- Auto-layout claramente especificado
- Orden de preferencia de fuentes
- Text behavior detallado

---

**¿Listo para crear el template con 95% de fidelidad?** 🚀
