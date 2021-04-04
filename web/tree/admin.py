from django.contrib import admin
from tree.models import Category
# from feincms.admin import editor


class CategoryAdmin(editor.TreeEditor):
    list_display = ('title',)


admin.site.register(Category, CategoryAdmin)
