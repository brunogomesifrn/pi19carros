# Generated by Django 2.2.7 on 2019-11-26 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_cor'),
    ]

    operations = [
        migrations.AddField(
            model_name='carros_comprar',
            name='cor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cor'),
        ),
        migrations.AddField(
            model_name='carros_diarios',
            name='cor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cor'),
        ),
    ]
