# Generated by Django 4.0.6 on 2024-06-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_models',
            name='ratings_prod',
            field=models.IntegerField(default=5, null=True),
        ),
    ]
