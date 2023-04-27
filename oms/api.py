from ninja import NinjaAPI

from . import schemas
from . import models

api = NinjaAPI()


# Products


@api.post("/products", response=schemas.ProductOut)
def create_product(request, payload: schemas.ProductIn):
    return models.Product.objects.create(**payload.dict())


@api.get("/products", response=list[schemas.ProductOut])
def list_products(request):
    return models.Product.objects.all()


# Suppliers


@api.post("/suppliers", response=schemas.SupplierOut)
def create_supplier(request, payload: schemas.SupplierIn):
    return models.Supplier.objects.create(**payload.dict())


@api.get("/suppliers", response=list[schemas.SupplierOut])
def list_suppliers(request):
    return models.Supplier.objects.all()

# Other endpoints...
