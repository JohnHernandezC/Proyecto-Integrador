# Generated by Django 4.0.1 on 2022-05-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentariosApp', '0002_rename_inmuebles_comentarios_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='publicacion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
