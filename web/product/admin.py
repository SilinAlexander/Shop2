from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField, ModelForm, ValidationError
from PIL import Image
from django.utils.safestring import mark_safe


class ProdAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red; font-size:14px;">Минимальный размер загружаемого изображения {}x{} !</span>
            """.format(
                *Product.MIN_RESOLUTION
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3МВ!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального!')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Разрешение изображения больше максимального!')
        return image


@admin.register(Product)
class ProdAdmin(admin.ModelAdmin):

    form = ProdAdminForm
    fields = ('category', 'title', 'image', 'description', 'price')
    list_display = ('title', 'category', 'price', 'slug')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # if db_field.name == 'category':
        #     return ModelChoiceField(Category.objects.filter(slug='prod1s'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):

        return super(ProdAdmin, self).get_queryset(request).select_related('category')


admin.site.register(Category)
admin.site.register(Customer)

