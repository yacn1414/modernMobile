# Generated by Django 4.1 on 2022-08-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_remove_sabad_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabad',
            name='T',
            field=models.IntegerField(default=None, verbose_name='تعداد'),
            preserve_default=False,
        ),
    ]
