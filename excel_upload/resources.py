from import_export import resources
from order_manager.models import Products


class ProductResources(resources.ModelResource):
    class Meta:
        model = Products
