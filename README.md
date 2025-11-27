<div align="center">

![Python](https://img.shields.io/badge/PYTHON-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FASTAPI-MODULAR-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Architecture](https://img.shields.io/badge/ARCH-MICROSERVICES-orange?style=for-the-badge&logo=serverless&logoColor=white)
![Render](https://img.shields.io/badge/DEPLOY-RENDER-46E3B7?style=for-the-badge&logo=render&logoColor=black)

# ENTERPRISE MICROSERVICES API
### Arquitectura Modular, Escalable y Despliegue Continuo
</div>

---

## 📋 PROJECT OVERVIEW

Este repositorio aloja una **API RESTful de grado empresarial** diseñada bajo el patrón de arquitectura de **Microservicios Modulares**. A diferencia de una aplicación monolítica tradicional, este sistema desacopla la lógica de negocio en dominios independientes (*Usuarios* y *Productos*), orquestados por un Gateway central.

El proyecto demuestra la implementación de prácticas avanzadas de ingeniería de software, incluyendo validación estricta de datos (Type Safety), gestión de dependencias moderna y despliegue automatizado en infraestructura PaaS.

---

##  ENGINEERING DECISIONS & UPDATES

Durante el ciclo de desarrollo (SDLC), se implementaron refactorizaciones críticas para garantizar la estabilidad y escalabilidad:

### 1. Arquitectura de Enrutamiento (`APIRouter`)
Se migró de un archivo `main.py` monolítico a una estructura distribuida utilizando `APIRouter`.
* **Beneficio:** Permite que equipos independientes trabajen en el módulo de `Users` sin romper el módulo de `Products`.
* **Implementación:** El `main.py` actúa únicamente como **Entrypoint/Gateway**, inyectando las rutas al iniciar la aplicación.

### 2. Migración a Pydantic V2
El sistema utiliza la última versión del motor de validación de datos **Pydantic**.
* **Actualización:** Se reemplazó el obsoleto `.dict()` por el moderno y eficiente serializador `.model_dump()`.
* **Validación:** Se integró `pydantic[email]` para asegurar la integridad de los datos de contacto a nivel de esquema.

### 3. Estabilidad del Runtime (Python 3.11)
Para evitar conflictos de compatibilidad detectados con versiones inestables (3.13+), se forzó el entorno de producción a **Python 3.11.9**. Esto asegura que todas las librerías asíncronas (`uvicorn`, `anyio`) funcionen sin errores de *ForwardRef*.

---

##  REPOSITORY STRUCTURE

La estructura sigue el estándar de "Flat Layout" optimizado para descubrimiento de paquetes en Python:

```text
/ (root)
├── main.py            # API Gateway & Entrypoint (Inicia Uvicorn)
├── requirements.txt   # Dependencias con versiones pineadas (Lockfile)
├── README.md          # Documentación técnica
└── routers/           # Paquete de Microservicios
    ├── __init__.py    # Inicializador del módulo
    ├── users.py       # Lógica de dominio: Gestión de Usuarios (CRUD)
    └── products.py    # Lógica de dominio: Catálogo de Productos

 # 1. Clonar repositorio
git clone [https://github.com/guaza69/Render1.1.git](https://github.com/guaza69/Render1.1.git)

# 2. Crear entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate  # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar servidor (Desde la raíz)
python -m uvicorn main:app --reload

¡Excelente! Viendo tu captura de pantalla, ahora tienes la estructura perfecta: el main.py está en la raíz (afuera) y los módulos dentro de routers. Eso es arquitectura de software real.Aquí tienes el README.md actualizado y profesional. He agregado secciones específicas que explican la Refactorización a Microservicios, la decisión de usar Pydantic V2, y la estrategia de enrutamiento.Copia y pega este código en tu archivo README.md:Markdown<div align="center">

![Python](https://img.shields.io/badge/PYTHON-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FASTAPI-MODULAR-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Architecture](https://img.shields.io/badge/ARCH-MICROSERVICES-orange?style=for-the-badge&logo=serverless&logoColor=white)
![Render](https://img.shields.io/badge/DEPLOY-RENDER-46E3B7?style=for-the-badge&logo=render&logoColor=black)

# ENTERPRISE MICROSERVICES API
### Arquitectura Modular, Escalable y Despliegue Continuo
</div>

---

## 📋 PROJECT OVERVIEW

Este repositorio aloja una **API RESTful de grado empresarial** diseñada bajo el patrón de arquitectura de **Microservicios Modulares**. A diferencia de una aplicación monolítica tradicional, este sistema desacopla la lógica de negocio en dominios independientes (*Usuarios* y *Productos*), orquestados por un Gateway central.

El proyecto demuestra la implementación de prácticas avanzadas de ingeniería de software, incluyendo validación estricta de datos (Type Safety), gestión de dependencias moderna y despliegue automatizado en infraestructura PaaS.

---

## 🛠️ ENGINEERING DECISIONS & UPDATES

Durante el ciclo de desarrollo (SDLC), se implementaron refactorizaciones críticas para garantizar la estabilidad y escalabilidad:

### 1. Arquitectura de Enrutamiento (`APIRouter`)
Se migró de un archivo `main.py` monolítico a una estructura distribuida utilizando `APIRouter`.
* **Beneficio:** Permite que equipos independientes trabajen en el módulo de `Users` sin romper el módulo de `Products`.
* **Implementación:** El `main.py` actúa únicamente como **Entrypoint/Gateway**, inyectando las rutas al iniciar la aplicación.

### 2. Migración a Pydantic V2
El sistema utiliza la última versión del motor de validación de datos **Pydantic**.
* **Actualización:** Se reemplazó el obsoleto `.dict()` por el moderno y eficiente serializador `.model_dump()`.
* **Validación:** Se integró `pydantic[email]` para asegurar la integridad de los datos de contacto a nivel de esquema.

### 3. Estabilidad del Runtime (Python 3.11)
Para evitar conflictos de compatibilidad detectados con versiones inestables (3.13+), se forzó el entorno de producción a **Python 3.11.9**. Esto asegura que todas las librerías asíncronas (`uvicorn`, `anyio`) funcionen sin errores de *ForwardRef*.

---

## 🏗️ REPOSITORY STRUCTURE

La estructura sigue el estándar de "Flat Layout" optimizado para descubrimiento de paquetes en Python:

```text
/ (root)
├── main.py            # API Gateway & Entrypoint (Inicia Uvicorn)
├── requirements.txt   # Dependencias con versiones pineadas (Lockfile)
├── README.md          # Documentación técnica
└── routers/           # Paquete de Microservicios
    ├── __init__.py    # Inicializador del módulo
    ├── users.py       # Lógica de dominio: Gestión de Usuarios (CRUD)
    └── products.py    # Lógica de dominio: Catálogo de Productos
🚀 DEPLOYMENT PIPELINEEl despliegue en Render está configurado para ser resiliente:Environment Check: Se valida la variable PYTHON_VERSION = 3.11.9.Dependency Resolution: Instalación limpia desde requirements.txt (FastAPI >= 0.110.0).Module Discovery: Ejecución de Uvicorn desde la raíz para asegurar que los imports de routers sean reconocidos correctamente.📡 API ENDPOINTSLa documentación interactiva (Swagger UI) está disponible en /docs. Los servicios están segregados por prefijos:ServicioMétodoEndpointDescripción TécnicaGatewayGET/Health Check del sistema global.UsersGET/users/Retorna lista de usuarios desde memoria.UsersPOST/users/Crea usuario con validación de Email y UUID autogenerado.ProductsGET/products/Consulta catálogo de productos (Read-Only).ProductsGET/products/{id}Búsqueda indexada por ID de producto.⚙️ LOCAL INSTALLATIONPara replicar el entorno de producción localmente:Bash# 1. Clonar repositorio
git clone [https://github.com/guaza69/Render1.1.git](https://github.com/guaza69/Render1.1.git)

# 2. Crear entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate  # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar servidor (Desde la raíz)
python -m uvicorn main:app --reload

<div align="center"><sub>Desarrollado por José Julián Guaza Botero | Backend Architecture</sub></div>
