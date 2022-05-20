# Generated by Django 3.2.8 on 2022-05-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('cover', models.FileField(upload_to='product/cover/')),
                ('size', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('somoni', models.BooleanField()),
                ('ruble', models.BooleanField()),
                ('discription', models.TextField()),
            ],
        ),
    ]