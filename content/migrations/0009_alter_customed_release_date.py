# Generated by Django 4.2.5 on 2023-09-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_alter_customed_description_alter_customed_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customed',
            name='release_date',
            field=models.IntegerField(verbose_name='Año de estreno'),
        ),
    ]
