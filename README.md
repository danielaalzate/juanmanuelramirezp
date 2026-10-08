# Juan Manuel Ramírez Pérez · Web

Sitio estático con Inicio, Biografía, Libros y Blog. Diseño editorial azul tinta con alternativa naranja. Nueve portadas originales representadas como libros mediante CSS; ocho enlaces a PDF originales.

## Ver y editar

La carpeta `dist` es el sitio listo para servir. Desde esta carpeta de proyecto: `python -m http.server 8769 --directory dist`. Abrir http://localhost:8769.

`build.py` genera el HTML desde los contenidos y datos recuperados de la web original. Ejecutar `python build.py` después de editarlo. El diseño está en `dist/styles.css` y las interacciones en `dist/site.js`.

## Biografía

La página `/biografia/` presenta un retrato editorial de gran formato con la misma integración sobre crema de Inicio: mezcla, máscara inferior y desvanecimiento de bordes. La apertura usa un titular serif grande, los datos del autor y una navegación por secciones. Formación y docencia se organizan en un capítulo asimétrico; cultura y vida pública, en una franja azul tinta que adopta el naranja al cambiar de tema.

El capítulo de escritura incluye tres libros construidos con las portadas originales de *Cuentos impertinentes*, *Huellas cifradas* y *Venezuela bajo el sol*, enlazados a sus fichas en el catálogo. Le siguen los vínculos académicos y una fotografía real del encuentro con Federico Diazgranados, con acceso al Blog. Se conserva la información biográfica recuperada de la fuente original. En móvil se apilan el retrato y los capítulos, se adapta la navegación y se mantiene la selección de tres libros.

## Color

El pie permite elegir Azul tinta o Naranja y recuerda la elección en el navegador. Para cambiar el color predeterminado de todo el sitio, editar `defaultTheme` en `dist/site-config.js`: `blue` u `orange`. Las variables de ambos temas están centralizadas en `dist/styles.css`. Los parámetros `?tema=blue` y `?tema=orange` permiten comparar colores.

## Video del estudio

El video suministrado por el usuario está instalado en `dist/assets/juan-manuel-escribiendo.mp4` y habilitado en `dist/site-config.js`. Se reproduce automáticamente, silenciado y en bucle; respeta la preferencia de movimiento reducido. La imagen ilustrativa original se conserva como respaldo. El video suministrado no se presenta como evidencia de una grabación auténtica.

La suscripción abre el formulario original. Su integración con un proveedor de correo queda pendiente de definir dicho proveedor. Sonetos no tiene un PDF enlazado en la fuente original.

## Encuentro en La Verbena Literaria

El Blog incluye una galería de tres fotografías del encuentro con Federico Diazgranados, con un adelanto en Inicio. Los datos facilitados por el usuario son: 22 de noviembre de 2023, La Verbena Literaria, Calle 121 # 12 - 15, Multicentro Usaquén, Bogotá. Las fotografías se convierten a WebP conservando los originales; cada imagen permite abrir la fotografía completa. No se añaden títulos de libros ni otros datos no confirmados.

## Lanzamiento de Cuentos impertinentes

El Blog incluye una galería de tres fotografías del lanzamiento de *Cuentos impertinentes*, con un adelanto en Inicio. Según los datos facilitados por el usuario, el encuentro tuvo lugar en el Museo de Arte Moderno Ramírez Villamizar, en Pamplona, Colombia, y la obra de la portada es de María Paula Alzate. Las imágenes WebP conservan las fotografías completas y sus enlaces permiten abrirlas a tamaño completo. No se añade una fecha del lanzamiento ni un año de edición, porque no se han facilitado ni confirmado.

## Contacto

El botón flotante de WhatsApp compartido se genera en `build.py` mediante `whatsapp()` y abre el chat del autor en `+573175379029` con el mensaje prellenado «Hola Juan Manuel me interesa tu trabajo, quisiera tener más información.»; el visitante debe enviarlo. Su CSS muestra un círculo verde de 62 px en escritorio y 56 px en móvil.

## Procedencia y comprobación

`sources` conserva el contenido recuperado y las URLs originales. Las carátulas reales están en `dist/assets/covers`, sin redibujar sus títulos. `.impeccable/review` contiene capturas de escritorio y móvil y los resultados de las comprobaciones de archivos y PDF.

Los años de edición están centralizados en `sources/edition-years.json`: siete están documentados, algunos mediante registros primarios contemporáneos de publicación. Los de *Cuentos impertinentes* y *Una ronda del tiempo* siguen sin confirmar y se muestran como «Año por confirmar».

`.openai/hosting.json` identifica el alojamiento privado de Sites. No contiene credenciales. La publicación se realiza mediante el flujo de Sites, conservando el sitio privado para revisión.

## Copia de seguridad en GitHub

Respaldo de la web publicada el 8 de octubre de 2026. Sitio: https://juan-manuel-ramirez-escritor.sotano.chatgpt.site/

- `dist/`: web lista para alojar, portadas, fotografías, fuentes y video.
- `resources/libros/`: ocho PDF originales disponibles; Sonetos no tiene PDF en la fuente original.
- `sources/`: contenido original y evidencia de los años de edición.
- `build.py`: genera las páginas. Ejecutar con Python 3 y servir `dist/` como raíz.
- `DESIGN.md` y `PRODUCT.md`: documentación del diseño y contenido.

Los PDF locales respaldan los recursos; la web conserva sus enlaces originales.
