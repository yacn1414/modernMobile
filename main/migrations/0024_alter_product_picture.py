# Generated by Django 4.1 on 2022-08-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_product_vip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='ProductImage/picture', verbose_name='عکس نمایشی'),
        ),
    ]
