# Generated by Django 4.0.1 on 2022-04-26 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsuariosApp', '0006_rename_is_active_usuario_usuario_activo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario_activo',
            new_name='is_active',
        ),
    ]
