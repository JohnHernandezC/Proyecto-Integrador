# Generated by Django 4.0.1 on 2022-04-11 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicacionesApp', '0005_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
