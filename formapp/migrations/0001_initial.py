# Generated by Django 4.2.9 on 2024-03-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudenInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('branch', models.CharField(max_length=40)),
                ('rollno', models.IntegerField()),
            ],
        ),
    ]
