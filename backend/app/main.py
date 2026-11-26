from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(
    title = "ShopSphere API",
    description = "AI Ecommerce course — initial backend foundation",
    version = "0.2.0",
)

class Product(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    category: str
    in_stock: bool
    
PRODUCTS = [
    Product(id=1, name="Wireless Mouse", price=799.0, category="Electronics", in_stock=True),
    Product(id=2, name="Notebook", price=149.0, category="Stationery", in_stock=True),
    Product(id=3, name="USB-C Cable", price=399.0, category="Electronics", in_stock=False),
]

@app.get("/health", tags=["Health"])
def health_check() -> dict[str,str]:
    return {"status":"ok","message": "ShopSphere backend is running!"}

@app.get("/about", tags=["General"])
def about() -> dict[str, str]:
    return {"project": "ShopSphere", "api_version": app.version}

@app.get("/products",response_model=list[Product], tags=["Products"])
def list_products(
        category: str | None = None,
        in_stock: bool | None = None,
        limit:int = Query(default=10,ge=1,le=50)
    ) -> list[Product]:
    results = PRODUCTS
    if category is not None:
            results = [p for p in results if p.category.casefold() == category.casefold()]
    if in_stock is not None:
            results = [p for p in results if p.in_stock == in_stock] 
    return results[:limit]

@app.get("/products/{product_id}",tags=["Products"])
def get_product(product_id:int = Path(gt=0)) -> Product:
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404,detail = "Product not found")
