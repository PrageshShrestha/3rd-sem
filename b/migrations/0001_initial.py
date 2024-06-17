# Generated by Django 4.0.6 on 2024-06-09 07:54

import b.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_number', models.IntegerField(null=True)),
                ('food', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='business_model',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('contacts', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('token', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ratings_parameter', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('area_wise_views', models.TextField()),
                ('reviews', models.IntegerField(null=True)),
                ('avg_rating', models.IntegerField(null=True)),
                ('img', models.ImageField(default='static/images/business.jpg', null=True, upload_to='static/')),
                ('today_views', models.IntegerField(null=True)),
                ('monthly_views', models.IntegerField(null=True)),
                ('latitude', models.IntegerField(null=True)),
                ('longitude', models.IntegerField(null=True)),
                ('mva', models.TextField()),
                ('views_record', models.TextField()),
                ('owner', models.CharField(max_length=100)),
                ('dob', models.DateField(default='2023-5-23')),
                ('listed_items', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='business_trackrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='categories_subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('sub_category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='category_saver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=300)),
                ('subcategory', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='last_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lc_forekey', models.CharField(max_length=200)),
                ('item_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='primary_subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='product_models',
            fields=[
                ('product_name', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('token', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('views', models.IntegerField(null=True)),
                ('likes', models.IntegerField(null=True)),
                ('picture', models.ImageField(default='static/images/product.jpg', null=True, upload_to='static/')),
                ('price_range', models.CharField(max_length=20, null=True)),
                ('category', models.CharField(max_length=200)),
                ('sub_category', models.CharField(max_length=200)),
                ('weight', models.IntegerField(null=True)),
                ('size', models.CharField(max_length=100)),
                ('negotiable', models.BooleanField()),
                ('images', models.ImageField(default='staic/images/product.jpg', null=True, upload_to='static/')),
                ('business_mdl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='b.business_model')),
            ],
        ),
        migrations.CreateModel(
            name='secondary_subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ss_forekey', models.CharField(max_length=200)),
                ('sub_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user_model',
            fields=[
                ('name', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=100)),
                ('registered', models.BooleanField(default=0, null=True)),
                ('token', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ratings_count', models.IntegerField(null=True)),
                ('views', models.IntegerField(null=True)),
                ('comments_count', models.IntegerField(null=True)),
                ('latitude', models.IntegerField(null=True)),
                ('area_code', models.CharField(max_length=20)),
                ('frequency', models.IntegerField(null=True)),
                ('longitude', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='views_recorder',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='b.user_model')),
                ('data_meta', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField(null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.product_models')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('subcategory', models.CharField(max_length=200)),
                ('item_name', models.CharField(max_length=200)),
                ('time', models.TimeField(default=b.models.current_time)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.business_model')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.product_models')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_token', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.business_model')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.product_models')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='bookmarked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.product_models')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.user_model')),
            ],
        ),
    ]
