<div align="center">

![Python](https://img.shields.io/badge/PYTHON-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FASTAPI-0.109.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Render](https://img.shields.io/badge/DEPLOY-RENDER-46E3B7?style=for-the-badge&logo=render&logoColor=black)
![Status](https://img.shields.io/badge/BUILD-PASSING-success?style=for-the-badge)

# REST API DEPLOYMENT POC
### Infraestructura como Servicio & Despliegue Continuo
</div>

---

## PROJECT OVERVIEW

Este repositorio contiene la implementación de referencia para una API de alto rendimiento utilizando **FastAPI**. El proyecto sirve como prueba de concepto (POC) para validar flujos de trabajo de integración continua (CI/CD) y despliegue en plataformas PaaS modernas.

El objetivo técnico es demostrar la capacidad de contenerización de aplicaciones Python asíncronas y su exposición pública segura mediante servicios gestionados.

---

## TECH STACK & ARCHITECTURE

La arquitectura ha sido seleccionada priorizando la latencia mínima y la escalabilidad horizontal.

| Componente | Tecnología | Justificación Técnica |
| :--- | :--- | :--- |
| **Runtime** | Python 3.10+ | Aprovechamiento de *Type Hints* avanzados y mejoras en gestión de memoria. |
| **Framework** | FastAPI | Valuado por su integración nativa con OpenAPI (Swagger) y velocidad de ejecución sobre Starlette. |
| **ASGI Server** | Uvicorn | Servidor de interfaz de puerta de enlace asíncrona estándar para producción. |
| **Cloud Provider** | Render | Plataforma PaaS seleccionada por su capacidad de *Zero Downtime Deploys* y soporte nativo HTTP/2. |

---

## REPOSITORY STRUCTURE

La estructura del proyecto sigue el estándar de *Flat Layout* para microservicios:

```text
/ (root)
├── main.py            # Entrypoint de la aplicación y definición de endpoints
├── requirements.txt   # Manifiesto de dependencias (Pinned versions)
├── .gitignore         # Reglas de exclusión para control de versiones
└── README.md          # Documentación técnica
