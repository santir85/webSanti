# Generated by Django 3.1.2 on 2021-07-06 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.DateField()),
                ('titulo', models.CharField(max_length=250)),
                ('precio', models.FloatField()),
                ('contenido', models.CharField(max_length=2000)),
                ('imagen', models.FileField(upload_to='imagenes/')),
                ('publicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='LeerMasTarde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicaciones', models.ManyToManyField(to='inicio.Articulo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasificacion_seccion', to='inicio.seccion'),
        ),
    ]
