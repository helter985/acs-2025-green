
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

### 2.3 Descripción de Módulos

| Módulo                            | Rol/es Aplicable/s       | Descripción                                                                                                                                       |
|----------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Ver lista de productos           | Encargado de ventas, Vendedor | Muestra el listado completo de productos importados desde archivos Excel. Incluye nombre, código e imagen, con precios actualizados.              |
| Buscar producto por nombre/código | Encargado de ventas, Vendedor | Permite localizar rápidamente productos usando nombre, código interno o código de barras. Ideal para escaneo o ingreso manual.                    |
| Ver imagen y precio de un producto | Encargado de ventas, Vendedor | Al visualizar un producto, se muestra su imagen y precio vigente. Útil para evitar errores por versiones desactualizadas.                         |
| Subir nueva lista de precios     | Encargado de ventas       | Permite cargar nuevos archivos Excel con precios actualizados de proveedores. Reemplaza la lista anterior.                                        |
| Actualizar imágenes de productos | Encargado de ventas       | Permite asignar imágenes manualmente a productos que no la traen. Las imágenes quedan asociadas al código único del producto.                     |
| Editar precios manualmente       | Encargado de ventas       | Posibilita modificar precios de productos puntualmente sin necesidad de recargar toda la lista desde cero.                                        |

---
