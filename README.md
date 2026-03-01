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

2. **Configura las variables de entorno**:
Crea un archivo llamado `.env` en la raíz del proyecto y añade tu clave de API de Gemini:
```env
GEMINI_API_KEY=tu_clave_api_aqui
```
*(Este paso es necesario para que el Chat con IA funcione correctamente).*

3. **Descarga e instalación de Elasticsearch (Windows)**:
Puedes descargar Elasticsearch ejecutando uno de los siguientes comandos en tu terminal:

```powershell
powershell -Command "Invoke-WebRequest -Uri 'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.12.0-windows-x86_64.zip' -OutFile 'elasticsearch.zip'"

# Alternativa usando curl:
curl.exe -L -o elasticsearch.zip https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.12.0-windows-x86_64.zip
```
Extrae el contenido del `.zip` de Elasticsearch.

## 🏃 Ejecución del Proyecto

Para arrancar Grimoire correctamente, necesitas tener tanto Elasticsearch como la aplicación Flask corriendo al mismo tiempo.

1. **Inicia Elasticsearch**:
Abre una terminal, navega a la carpeta donde extrajiste Elasticsearch y ejecuta:
```bash
bin\elasticsearch.bat
```
*(Nota: Mantén esta terminal abierta. La aplicación intentará crear el índice `grimoire_files` automáticamente al conectarse).*

2. **Inicia la aplicación principal**:
Abre una *nueva* terminal, asegúrate de estar en el directorio del proyecto `Grimoire` y ejecuta:
```bash
python app.py
```

3. **Accede a la plataforma**:
Abre tu navegador web y visita: [http://localhost:8080](http://localhost:8080)

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
