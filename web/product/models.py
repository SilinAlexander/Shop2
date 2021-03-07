from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify


User = get_user_model()


class MinResolutionErrorException(Exception):

    pass


class MaxResolutionErrorException(Exception):

    pass


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:

    objects = LatestProductsManager()


class CategoryManager(models.Manager):

    CATEGORY_NAME_COUNT_NAME = {
        'Товар ': 'prod1__count',
    }

    def get_queryset(self):
        return super().get_queryset()


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


def validate_image(img):
    min_height, min_width = Product.MIN_RESOLUTION
    max_height, max_width = Product.MAX_RESOLUTION
    if img.height < min_height or img.width < min_width:
        raise MinResolutionErrorException('Разрешение изображения меньше минимального!')
    if img.height > max_height or img.width > max_width:
        raise MaxResolutionErrorException('Разрешение изображения больше максимального!')


class Product(models.Model):

    MIN_RESOLUTION = (40, 40)
    MAX_RESOLUTION = (800, 800)
    MAX_IMAGE_SIZE = 3145728

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='product_set')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True, allow_unicode=True)
    image = models.ImageField(verbose_name='Изображение', validators=(validate_image,))
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    objects = models.Manager()

    def __str__(self):
        return self.title

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return reverse_lazy('product_detail', kwargs={'slug': self.slug})

    def get_model_name(self):
        return self.__class__._meta.model_name

    def save(self, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(**kwargs)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)









