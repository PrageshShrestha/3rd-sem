# Generated by Django 4.0.6 on 2024-06-08 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_models',
            name='business_mdl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='b.business_model'),
        ),
    ]