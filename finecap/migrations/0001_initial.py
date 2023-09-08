# Generated by Django 4.2.5 on 2023-09-08 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=11)),
                ('categoria_empresa', models.DateField()),
                ('quitado', models.BooleanField()),
                ('stand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finecap.stands')),
            ],
        ),
    ]
