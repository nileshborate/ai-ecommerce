from fastapi import FastAPI, Path, HTTPException, Query, Response, status
from pydantic import BaseModel, Field, model_validator

app = FastAPI(
    title = "ShopSphere API",
    description = "AI Ecommerce course — initial backend foundation",
    version = "0.3.0",
)

class ProductCreate(BaseModel):
      sku: str = Field(min_length=3, max_length=30, pattern=r"^[A-Z0-9-]+$")
      name: str = Field(min_length=1)
      price: float = Field(gt=0)
      category: str = Field(min_length=1)
      in_stock: bool

class Product(ProductCreate):
    id: int = Field(gt=0)
    
class ProductPatch(BaseModel):
      sku: str | None = Field(default=None, min_length=3, max_length=30,pattern=r"^[A-Z0-9-]+$")
      name: str | None = Field(default=None, min_length=1)
      price: float | None = Field(default=None, gt=0)
      category: str | None = Field(default=None, min_length=1)
      in_stock: bool | None = None

      @model_validator(mode="after")
      def nonempty_nonnull_patch(self):
          if not self.model_fields_set:
              raise ValueError("Send at least one field to update")
          for field_name in self.model_fields_set:
              if getattr(self, field_name) is None:
                  raise ValueError(f"{field_name} cannot be null")
          return self

INITIAL_PRODUCTS = [
      Product(id=1, sku="MOUSE-001", name="Wireless Mouse", price=799.0,category="Electronics", in_stock=True),
      Product(id=2, sku="NOTE-001", name="Notebook", price=149.0,category="Stationery", in_stock=True),
      Product(id=3, sku="CABLE-001", name="USB-C Cable", price=399.0,category="Electronics", in_stock=False),
  ]

PRODUCTS = [p.model_copy(deep=True) for p in INITIAL_PRODUCTS]

#helper functions
def find_product(product_id: int) -> Product:
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

def check_unique_sku(sku: str, *, except_id: int | None = None) -> None:
    if any(p.sku == sku and p.id != except_id for p in PRODUCTS):
        raise HTTPException(status_code=409, detail="SKU already exists")
    
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

#POST Method - To add record
@app.post("/products", response_model=Product,status_code=status.HTTP_201_CREATED, tags=["Products"])
def create_product(payload: ProductCreate) -> Product:
    check_unique_sku(payload.sku)
    new_id = max((p.id for p in PRODUCTS), default=0) + 1
    product = Product(id=new_id, **payload.model_dump())
    PRODUCTS.append(product)
    return product

#PUT - to update entire object
@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
def replace_product(payload: ProductCreate,
    product_id: int = Path(gt=0)) -> Product:
    previous = find_product(product_id)
    check_unique_sku(payload.sku, except_id=product_id)
    updated = Product(id=product_id, **payload.model_dump())
    PRODUCTS[PRODUCTS.index(previous)] = updated
    return updated

#PATCH - Partial update
@app.patch("/products/{product_id}", response_model=Product, tags=["Products"])
def patch_product(payload: ProductPatch,
                    product_id: int = Path(gt=0)) -> Product:
    previous = find_product(product_id)
    changes = payload.model_dump(exclude_unset=True)
    if "sku" in changes:
        check_unique_sku(changes["sku"], except_id=product_id)
    updated = Product.model_validate({**previous.model_dump(), **changes})
    PRODUCTS[PRODUCTS.index(previous)] = updated
    return updated

#DELETE - to remove object
@app.delete("/products/{product_id}",status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
def delete_product(product_id: int = Path(gt=0)) -> Response:
    previous = find_product(product_id)
    PRODUCTS.remove(previous)
    return Response(status_code=status.HTTP_204_NO_CONTENT)