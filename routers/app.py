from fastapi import FastAPI
from routers import users, products # Importamos los microservicios

app = FastAPI(
    title="Enterprise Microservices API",
    description="Arquitectura modular integrando servicios de Usuarios y Productos",
    version="2.0.0"
)

# Inyectamos los microservicios (Routing)
app.include_router(users.router)
app.include_router(products.router)

@app.get("/")
def health_check():
    return {"status": "Gateway Online", "services": ["Users", "Products"]}