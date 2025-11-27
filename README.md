<div align="center">

![Python](https://img.shields.io/badge/PYTHON-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FASTAPI-MODULAR-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Architecture](https://img.shields.io/badge/ARCH-MICROSERVICES-orange?style=for-the-badge&logo=serverless&logoColor=white)
![Render](https://img.shields.io/badge/DEPLOY-RENDER-46E3B7?style=for-the-badge&logo=render&logoColor=black)
![License](https://img.shields.io/badge/LICENSE-MIT-green?style=for-the-badge)

# ENTERPRISE MICROSERVICES API
### Arquitectura Modular, Escalable y Despliegue Continuo (CI/CD)
</div>

---

## PROJECT OVERVIEW

Este repositorio aloja una implementación de referencia de una **API RESTful** diseñada bajo patrones de arquitectura de software modernos. A diferencia de las aplicaciones monolíticas tradicionales, este sistema implementa una **Arquitectura de Microservicios Modulares**, desacoplando la lógica de negocio en dominios independientes (*Usuarios* y *Productos*) orquestados por un API Gateway central.

**Objetivo del Proyecto:** Demostrar la capacidad de ingeniería para construir sistemas backend escalables, tipados estáticamente y desplegados automáticamente en infraestructura PaaS.

---

## SYSTEM ARCHITECTURE

El flujo de datos se gestiona a través de un Gateway centralizado que enruta las peticiones a los servicios correspondientes, manteniendo la separación de responsabilidades (SoC).

```mermaid
graph TD
    Client[Cliente / Frontend] -->|HTTP Request| Gateway[API Gateway main.py]
    
    subgraph Application_Layer
        Gateway -->|/users| UserRouter[Users Service]
        Gateway -->|/products| ProdRouter[Products Service]
    end
    
    subgraph Data_Layer
        UserRouter --> UserDB[(In-Memory Users DB)]
        ProdRouter --> ProdDB[(In-Memory Products DB)]
    end
    
    style Gateway fill:#f9f,stroke:#333,stroke-width:2px
    style UserRouter fill:#bbf,stroke:#333,stroke-width:2px
    style ProdRouter fill:#bbf,stroke:#333,stroke-width:2px
