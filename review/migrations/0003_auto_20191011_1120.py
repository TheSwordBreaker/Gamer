# Generated by Django 2.2.3 on 2019-10-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20191011_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
