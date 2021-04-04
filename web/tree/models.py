import mptt
from django.db import models


class Category(models.Model):
    title = models.CharField('Название', max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Родитель", related_name='child')

    def __unicode__(self):
        return self.title


mptt.register(Category,)
