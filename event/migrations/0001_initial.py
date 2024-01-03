# Generated by Django 3.1.1 on 2024-01-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]