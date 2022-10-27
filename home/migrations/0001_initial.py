# Generated by Django 4.1.2 on 2022-10-27 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Detalhes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nullable', models.BooleanField(default=True)),
                ('dataFundacao', models.DateTimeField(auto_now=True)),
                ('populacaoEstimada', models.IntegerField()),
                ('altitude', models.IntegerField()),
                ('idh', models.DecimalField(decimal_places=1, max_digits=10)),
                ('site', models.CharField(max_length=50)),
                ('detalhe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.cidade')),
            ],
        ),
    ]