from ninja import ModelSchema
from . import models


class ProductIn(ModelSchema):
    class Config:
        model = models.Product
        model_fields = ["sku", "name"]


class ProductOut(ModelSchema):
    class Config:
        model = models.Product
        model_fields = ["sku", "name"]


class SupplierIn(ModelSchema):
    class Config:
        model = models.Supplier
        model_fields = ["name"]


class SupplierOut(ModelSchema):
    class Config:
        model = models.Supplier
        model_fields = ["id", "name"]
