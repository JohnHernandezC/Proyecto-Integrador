# Generated by Django 4.0.1 on 2022-04-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacionesApp', '0009_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.URLField(verbose_name='Imagen de Perfil'),
        ),
    ]