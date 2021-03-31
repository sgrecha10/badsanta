from django.contrib import admin
from mycat.models import Catalog2


@admin.register(Catalog2)
class Catalog2Admin(admin.ModelAdmin):
    list_display = ('part', 'id0', 'pkey', 'id1', 'type', 'status', 'stype', 'numru', 'numen',
                    'snum', 'nameru', 'nameen', 'obl', 'ogl', 'comment', 'pub', 'html', 'gif',
                    'pages', 'date0', 'date1', 'date2', 'date3')

# @admin.register(Catalog)
# class CatalogAdmin(admin.ModelAdmin):
#     list_display = ('id0', 'id1', 'type', 'gtype', 'status', 'pages', 'num', 'snum',
#                     'namer', 'namee', 'obl', 'date0', 'date1', 'date2', 'date3', 'dates', 'rel', 'okp')
