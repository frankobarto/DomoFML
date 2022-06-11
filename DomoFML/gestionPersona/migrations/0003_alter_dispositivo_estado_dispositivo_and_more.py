# Generated by Django 4.0.5 on 2022-06-11 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPersona', '0002_estado_dispositivo_parentesco_tipo_dispositivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='estado_dispositivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionPersona.estado_dispositivo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='tipo_dispositivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionPersona.tipo_dispositivo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='parentesco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionPersona.parentesco', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='tipo_propiedad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionPersona.tipo_propiedad', blank=True, null=True),
        ),
    ]
