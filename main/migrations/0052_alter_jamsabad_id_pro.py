# Generated by Django 4.1 on 2022-08-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_alter_jamsabad_options_jamsabad_id_pro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jamsabad',
            name='id_pro',
            field=models.IntegerField(),
        ),
    ]
