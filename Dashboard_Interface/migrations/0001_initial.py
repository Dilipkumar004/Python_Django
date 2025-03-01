# Generated by Django 5.1.6 on 2025-03-01 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=100)),
                ('database_name', models.CharField(max_length=100)),
                ('loaded_date', models.DateField()),
                ('table_count', models.IntegerField()),
            ],
        ),
    ]
