from fastapi import FastAPI

app = FastAPI(
    title = "ShopSphere API",
    description = "AI Ecommerce course — initial backend foundation",
    version = "0.1.0",
)

@app.get("/health", tags=["Health"])
def health_check() -> dict[str,str]:
    return {"status":"ok","message": "ShopSphere backend is running!"}