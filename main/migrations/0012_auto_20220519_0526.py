# Generated by Django 3.2.8 on 2022-05-19 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_contact_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
    ]
