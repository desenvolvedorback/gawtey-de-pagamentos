from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import payment_controller, admin_controller

app = FastAPI(title="Gateway de Pagamento")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payment_controller.router, prefix="/api/payments", tags=["Payments"])
app.include_router(admin_controller.router, prefix="/api/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "Gateway de Pagamento Online - Sandbox"}
