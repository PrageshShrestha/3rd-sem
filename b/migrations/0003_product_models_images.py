# Generated by Django 4.0.6 on 2024-06-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0002_alter_product_models_business_mdl'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_models',
            name='images',
            field=models.ImageField(default='staic/images/product.jpg', null=True, upload_to='static/'),
        ),
    ]
