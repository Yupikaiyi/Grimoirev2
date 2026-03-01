# Grimoire - Smart Document Management & Search

Grimoire es una plataforma avanzada de gestión y búsqueda de documentos que combina búsqueda tradicional por palabras clave con **IA Semántica** (Vectores) para encontrar información por contexto, no solo por coincidencia exacta.

## ✨ Características Principales

- **Búsqueda Híbrida**: Combina Elasticsearch (BM25) con búsqueda semántica (K-NN) usando `sentence-transformers`.
- **IA Semántica**: Encuentra documentos basándose en su significado, incluso si no contienen las palabras exactas de la consulta.
- **Gestión de Identidad**: Asocia cada archivo con un **Responsable** y un **Departamento** para una organización estructural clara.
- **Filtrado Dinámico**: Filtra por fecha, tamaño, etiquetas y extensiones de archivo que se adaptan automáticamente a tu base de datos.
- **Interfaz "Techno-Light"**: Diseño moderno, claro y responsivo con previsualización de documentos.
- **Chat con IA**: Consulta directa sobre el contenido de los documentos usando Gemini.

## 🛠️ Requisitos Técnico

### Software
- Python 3.10+
- **Elasticsearch 8.x** (corriendo en `http://localhost:9200`)
- SQLite 3

### Dependencias Principales
- `flask`: Framework web.
- `elasticsearch`: Cliente para el motor de búsqueda.
- `sentence-transformers`: Para la generación de embeddings vectoriales.
- `pymupdf`: Extracción de contenido de PDFs.

## 🚀 Instalación y Configuración

1. **Clona el repositorio e instala dependencias**:
```bash
pip install -r requirements.txt
```

2. **Asegúrate de que Elasticsearch esté activo**:
La aplicación intentará crear el índice `grimoire_files` automáticamente al arrancar.

3. **Inicia la aplicación**:
```bash
python app.py
```
La aplicación estará disponible en: [http://localhost:8080](http://localhost:8080)

## 📁 Estructura del Proyecto

```
Grimoire/
├── app.py              # Backend principal y API REST
├── search.py           # Lógica de búsqueda (ES + Modelos de IA)
├── grimoire.db         # Base de datos SQLite (Metadatos)
├── testfiles/          # Repositorio de documentos subidos
├── static/             # CSS moderno y recursos visuales
└── templates/          # Plantillas Jinja2 (Results, Index, etc)
```

## 🗺️ API Endpoints

- `GET /api/search?q=...` - Búsqueda híbrida con filtros.
- `GET /api/file-types` - Obtiene extensiones únicas existentes.
- `POST /api/files/<name>/identity` - Asigna responsable y departamento.
- `GET /api/identity-options` - Listado para filtros de la barra lateral.
