# Generated by Django 3.1.7 on 2021-03-07 09:50

from django.db import migrations


products = {
    'category 1': [
        {
            'title': 'product 1',
            'description': 'descr1',
            'price': 200,
            'image': 'загрузка_1.jpg'
        },
        {
            'title': 'product 2',
            'description': 'descr2',
            'price': 5000,

        }
    ]
}


def set_products(apps, scheme_editor):

    pass

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
    ]
