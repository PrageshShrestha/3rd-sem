from django.core.management.base import BaseCommand
from b.models import (
    categories_subcategories,
    product_models,
    comments,
    category_saver,
    ratings,
    user_model,
    history,
    area_data,
    business_model,
    primary_subcategory,
    secondary_subcategory,
    last_category
    
)
import random
from datetime import datetime, timedelta
from django.utils import timezone
class Command(BaseCommand):
    help = 'Populate the database with demo data'

    def handle(self, *args, **kwargs):
        # Check if the database is already populated
        if user_model.objects.count() == 0 and business_model.objects.count()==0 and primary_subcategory.objects.count()==0:
            self.stdout.write(self.style.WARNING('Database already empty. Operation terminated...'))
            return
        def dropping():
            categories_subcategories.objects.all().delete()
            product_models.objects.all().delete()
            comments.objects.all().delete()
            category_saver.objects.all().delete()
            ratings.objects.all().delete()
            user_model.objects.all().delete()
            history.objects.all().delete()
            business_model.objects.all().delete()
            history.objects.all().delete()
            area_data.objects.all().delete()
            primary_subcategory.objects.all().delete()
            secondary_subcategory.objects.all().delete()
            last_category.objects.all().delete()
        dropping()    
        self.stdout.write(self.style.SUCCESS('Demo data thanosed successfully!'))