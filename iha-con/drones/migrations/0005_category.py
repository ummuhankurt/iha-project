# Generated by Django 4.1.7 on 2023-02-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0004_alter_drone_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(max_length=100, null=True)),
            ],
        ),
    ]