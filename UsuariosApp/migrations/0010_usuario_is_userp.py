# Generated by Django 4.0.1 on 2022-04-29 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsuariosApp', '0009_rename_usuario_admin_usuario_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_userp',
            field=models.BooleanField(default=False),
        ),
    ]
