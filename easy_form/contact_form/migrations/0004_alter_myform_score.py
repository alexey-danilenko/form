# Generated by Django 4.0.4 on 2022-05-05 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0003_myform_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myform',
            name='score',
            field=models.CharField(default=-1, max_length=200),
        ),
    ]