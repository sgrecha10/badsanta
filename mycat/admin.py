from django.contrib import admin
from mycat.models import Catalog


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass
