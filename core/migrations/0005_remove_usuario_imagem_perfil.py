# Generated by Django 2.2.6 on 2019-10-30 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191030_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='imagem_perfil',
        ),
    ]