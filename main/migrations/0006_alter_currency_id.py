# Generated by Django 3.2.8 on 2022-05-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_currency_current_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
