


###### para correr el servidor ejecutar comando: "uvicorn main:app --reload" ######
## una vez activado ir a la url "http://127.0.0.1:8000/docs" para ver servicios de API



## Actividad 1 - Test Plan

### Revisión y Aprobación del Documento

Las siguientes especificaciones de requerimientos de software han sido aceptadas y aprobadas por las personas a continuación:

| Nombre             | Título | Fecha        |
|--------------------|--------|--------------|
| Aldana Moreno      |        |              |
| Ulises Festín      |        |              |
| Pablo Balastegui   |        |              |
| Emanuel Gallo      |        |              |

---

## 1. Introducción

La empresa cliente es una distribuidora de artículos de limpieza que comercializa sus productos tanto en su local físico como a través de vendedores que se movilizan en vehículos con mercadería. El principal problema que enfrentan actualmente es la dificultad para consultar precios actualizados, ya que los listados se reciben en distintos formatos y los vendedores muchas veces utilizan versiones antiguas, lo que genera errores en la venta. Por esto, se requiere una aplicación sencilla que les permita a los vendedores consultar rápidamente el precio vigente de los productos desde sus celulares, visualizando nombre, precio, imagen y código. La actualización de precios será gestionada desde casa central por el encargado de ventas, quien se encargará de normalizar la información proveniente de diferentes proveedores.

### 1.1 Propósito

El propósito de este documento es especificar los requerimientos del sistema "Lista de Precios", una aplicación móvil para vendedores de una distribuidora de artículos de limpieza. Su principal función es permitir la consulta rápida y precisa de los precios actualizados de productos mediante dispositivos móviles.

### 1.2 Alcance de las pruebas (Scope)

**Se probará (In Scope):**
- **Funcionalidad**: Carga de lista, búsqueda de productos, visualización de información (nombre, precio, imagen, código).
- **Usabilidad**: Interfaz simple, accesible sin necesidad de capacitación.
- **Compatibilidad**: Android e iOS.
- **UI (Interfaz de Usuario)**: Diseño amigable e intuitivo.

**Fuera de alcance (Out of Scope):**
- **Seguridad**: No se manejarán datos sensibles.
- **Performance**: No se realizarán pruebas de estrés.
- **Hardware**: No hay interacción con hardware específico.

### 1.3 Definiciones

- **Vendedor**: Usuario de la app móvil que consulta precios.
- **Encargado de ventas**: Usuario con acceso al sistema para actualizar listas y subir imágenes.
- **Producto**: Artículo de limpieza con nombre, precio, imagen y código (de barras o interno).
- **Lista de precios**: Archivo Excel que contiene información de productos, enviado por los proveedores.


## 2. Requerimientos

### 2.1 Descripción de Roles

- **Vendedor**: Solo tiene acceso a la consulta de productos desde la app móvil.
- **Encargado de ventas**: Administra el sistema desde una interfaz web o backend, cargando y actualizando listas de precios e imágenes de productos.

### 2.2 Funcionalidades por Rol

| Funcionalidad                        | Vendedor | Encargado de ventas  |
|--------------------------------------|----------|----------------------|
| Ver lista de productos               | ✅       | ✅                  |
| Buscar producto por nombre/código    | ✅       | ✅                  |
| Ver imagen y precio de un producto   | ✅       | ✅                  |
| Subir nueva lista de precios         | ❌       | ✅                  |
| Actualizar imágenes de productos     | ❌       | ✅                  |
| Editar precios manualmente           | ❌       | ✅                  |

### Descripción de Módulos

| Módulo                            | Rol/es Aplicable/s       | Descripción                                                                                                                                       |
|----------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Ver lista de productos           | Encargado de ventas, Vendedor | Muestra el listado completo de productos importados desde archivos Excel. Incluye nombre, código e imagen, con precios actualizados.              |
| Buscar producto por nombre/código | Encargado de ventas, Vendedor | Permite localizar rápidamente productos usando nombre, código interno o código de barras. Ideal para escaneo o ingreso manual.                    |
| Ver imagen y precio de un producto | Encargado de ventas, Vendedor | Al visualizar un producto, se muestra su imagen y precio vigente. Útil para evitar errores por versiones desactualizadas.                         |
| Subir nueva lista de precios     | Encargado de ventas       | Permite cargar nuevos archivos Excel con precios actualizados de proveedores. Reemplaza la lista anterior.                                        |
| Actualizar imágenes de productos | Encargado de ventas       | Permite asignar imágenes manualmente a productos que no la traen. Las imágenes quedan asociadas al código único del producto.                     |
| Editar precios manualmente       | Encargado de ventas       | Posibilita modificar precios de productos puntualmente sin necesidad de recargar toda la lista desde cero.                                        |

## Actividad 2 - User Stories / Test Cases

### 2.3 - User Stories - Lista de Precios

---

### 📦 Módulo: Ver lista de productos

#### HU01 - Visualizar productos como vendedor
**Como** vendedor,  
**quiero** ver la lista completa de productos disponibles,  
**para** consultar fácilmente qué artículos hay y cuál es su precio actualizado.

#### HU02 - Visualizar productos como encargado de ventas
**Como** encargado de ventas,  
**quiero** acceder a todo el listado de productos,  
**para** poder revisar o validar la información que se sube desde los archivos Excel.

---

### 🔍 Módulo: Buscar producto por nombre/código

#### HU03 - Buscar productos como vendedor
**Como** vendedor,  
**quiero** buscar productos por nombre o código,  
**para** encontrarlos más rápido cuando estoy atendiendo a un cliente o en ruta.

#### HU04 - Buscar productos como encargado de ventas
**Como** encargado de ventas,  
**quiero** encontrar un producto fácilmente usando el nombre o código,  
**para** editar o verificar su información rápidamente.

---

### 🖼️ Módulo: Ver imagen y precio de un producto

#### HU05 - Ver detalle de producto como vendedor
**Como** vendedor,  
**quiero** ver la imagen y el precio de cada producto,  
**para** asegurarme de ofrecer el producto correcto al cliente.

#### HU06 - Ver detalle de producto como encargado de ventas
**Como** encargado de ventas,  
**quiero** ver la imagen y precio actual de un producto,  
**para** verificar su presentación y editar su contenido si es necesario.

---

### 📁 Módulo: Subir nueva lista de precios

#### HU07 - Subir lista de precios como encargado de ventas
**Como** encargado de ventas,  
**quiero** subir un nuevo archivo Excel con precios,  
**para** actualizar de forma masiva el catálogo del sistema con la lista más reciente.

---

### 🖼️ Módulo: Actualizar imágenes de productos

#### HU08 - Cargar imágenes como encargado de ventas
**Como** encargado de ventas,  
**quiero** subir imágenes de los productos manualmente,  
**para** completar la información visual en caso de que no venga incluida en la lista.

---

### ✏️ Módulo: Editar precios manualmente

#### HU09 - Modificar precios como encargado de ventas
**Como** encargado de ventas,  
**quiero** editar el precio de un producto desde el sistema,  
**para** corregir valores sin necesidad de subir toda una lista nueva.

### 2.4 - Test Cases

A continuación se describen los casos de prueba asociados a las historias de usuario del sistema "Lista de Precios":

---

### 📦 Módulo: Ver lista de productos

#### TC01 - Ver productos como vendedor
- **Precondición:** Usuario con rol "Vendedor" autenticado.
- **Entrada:** Acceso al módulo "Lista de productos".
- **Resultado esperado:** Se muestra la lista completa de productos con nombre, código y precio.

#### TC02 - Ver productos como encargado de ventas
- **Precondición:** Usuario con rol "Encargado de ventas" autenticado.
- **Entrada:** Acceso al módulo "Lista de productos".
- **Resultado esperado:** Se visualiza el listado completo de productos importados.

---

### 🔍 Módulo: Buscar producto por nombre/código

#### TC03 - Buscar por nombre como vendedor
- **Precondición:** Usuario con rol "Vendedor" autenticado, lista visible.
- **Entrada:** Ingreso de nombre parcial o completo del producto.
- **Resultado esperado:** Se muestran los productos coincidentes.

#### TC04 - Buscar por código como vendedor
- **Entrada:** Ingreso de código exacto o parcial.
- **Resultado esperado:** El producto correspondiente aparece en la lista.

#### TC05 - Buscar por nombre o código como encargado de ventas
- **Precondición:** Usuario con rol "Encargado de ventas".
- **Entrada:** Búsqueda por nombre/código.
- **Resultado esperado:** Se filtra correctamente el listado de productos.

---

### 🖼️ Módulo: Ver imagen y precio de un producto

#### TC06 - Visualizar imagen y precio como vendedor
- **Precondición:** Usuario autenticado como "Vendedor".
- **Entrada:** Selección de un producto de la lista.
- **Resultado esperado:** Se muestra la imagen del producto y su precio actualizado.

#### TC07 - Visualizar imagen y precio como encargado de ventas
- **Precondición:** Usuario autenticado como "Encargado de ventas".
- **Entrada:** Selección de un producto.
- **Resultado esperado:** Se muestra imagen y precio, disponibles para verificación.

---

### 📁 Módulo: Subir nueva lista de precios

#### TC08 - Subir archivo válido
- **Precondición:** Usuario con rol "Encargado de ventas" autenticado.
- **Entrada:** Carga de archivo Excel con formato correcto.
- **Resultado esperado:** Se actualiza correctamente la lista de productos.

#### TC09 - Subir archivo con errores
- **Entrada:** Carga de archivo con campos faltantes o formato inválido.
- **Resultado esperado:** El sistema muestra un mensaje de error y no actualiza la lista.

---

### 🖼️ Módulo: Actualizar imágenes de productos

#### TC10 - Cargar imagen a producto existente
- **Precondición:** Producto cargado sin imagen previa.
- **Entrada:** Selección del producto y carga de imagen (JPG/PNG).
- **Resultado esperado:** La imagen se guarda correctamente y se asocia al producto.

#### TC11 - Cargar imagen con formato no soportado
- **Entrada:** Archivo en formato no válido (por ejemplo, PDF).
- **Resultado esperado:** El sistema rechaza el archivo y muestra mensaje de error.

---

### ✏️ Módulo: Editar precios manualmente

#### TC12 - Modificar precio correctamente
- **Precondición:** Usuario autenticado como "Encargado de ventas".
- **Entrada:** Selección de producto y nuevo precio válido.
- **Resultado esperado:** El precio se actualiza y se guarda correctamente.

#### TC13 - Ingreso de precio inválido
- **Entrada:** Precio en formato incorrecto (texto, negativo, vacío).
- **Resultado esperado:** El sistema no permite guardar y muestra error de validación.

---

## 3. Especificaciones

### 3.1 Arquitectura

![image](https://github.com/user-attachments/assets/3b817a23-f869-4181-bf78-c52b45ec8a48)


---

### 📄 3.2 - Definición de API

El contrato de la API fue definido utilizando el estándar **OpenAPI 3.0.3**.  
Incluye los endpoints disponibles para el rol de **vendedor**, con filtrado por nombre, manejo de errores y estructura de respuesta.

🔗 [Ver contrato OpenAPI](./contract-api.yaml)


---

## 🧪 4. Cómo ejecutar la API localmente

1. Asegurate de tener Python 3.9 o superior instalado.

2. Abrí la terminal en la carpeta del proyecto y creá un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # En Windows
   # source venv/bin/activate   # En Linux o macOS
   ```

3. Instalá las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutá la API con Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

5. Accedé desde tu navegador a:

   - Swagger: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

Esto levantará un servidor local con los endpoints definidos en main.py y podrás probarlos visualmente.