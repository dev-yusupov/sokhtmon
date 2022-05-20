# Generated by Django 3.2.8 on 2022-05-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('cover', models.FileField(upload_to='product/cover')),
                ('size', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
