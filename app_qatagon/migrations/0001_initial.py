# Generated by Django 4.2.11 on 2024-04-05 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Hodisa')),
                ('date', models.DateField(verbose_name='Sana')),
                ('description', models.TextField(verbose_name='Tavsifi')),
                ('location', models.CharField(max_length=100, verbose_name='Hodisa sodir etilgan joyi')),
            ],
            options={
                'verbose_name': 'Hodisa',
                'verbose_name_plural': 'Hodisalar',
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='AffectedIndividual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ismi Sharifi')),
                ('data_of_birth', models.DateField(verbose_name='Tugulgan sanasi')),
                ('occupation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Kasbi')),
                ('description', models.TextField(verbose_name='Tavsifi')),
                ('person_image', models.ImageField(blank=True, null=True, upload_to='static/', verbose_name='Qatag`on qurboni surati')),
                ('event_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_qatagon.event')),
            ],
            options={
                'verbose_name': 'Qatag`on qurbonlari',
                'verbose_name_plural': 'Qatag`on qurbonlari',
                'db_table': 'people',
            },
        ),
    ]
