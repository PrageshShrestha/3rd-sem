from django.core.management.base import BaseCommand
import json

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
    business_trackrecord,
    primary_subcategory,
    secondary_subcategory,
    last_category,
    bookmarked,
    food_cate,
)
import random
from datetime import datetime, timedelta
from django.utils import timezone
class Command(BaseCommand):
    help = 'Populate the database with demo data'
    # Truncate to max_length of 200
       
    def handle(self, *args, **kwargs):
        # Check if the database is already populated
        if user_model.objects.count() > 0 and business_model.objects.count()>0:
            self.stdout.write(self.style.WARNING('Database already populated. Operation terminated...'))
            return

        # Generate and save demo data
        self.stdout.write('Populating the database with demo data...')
        categories = [
    ("Fruits", ("Apples", "Oranges", "Bananas", "Grapes", "Strawberries", "Watermelons", "Pineapples", "Mangoes", "Kiwis", "Peaches", "Plums", "Pears", "Cherries", "Blueberries", "Avocados")),
    ("Vegetables", ("Carrots", "Tomatoes", "Potatoes", "Lettuce", "Spinach", "Broccoli", "Bell Peppers", "Onions", "Cucumbers", "Cauliflower", "Zucchini", "Green Beans", "Mushrooms", "Kale", "Celery")),
    ("Meat and Poultry", ("Chicken Breasts", "Pork Chops", "Ground Beef", "Turkey Breast", "Lamb Chops", "Bacon", "Ham", "Sausages", "Veal", "Duck Breast", "Quail", "Rabbit", "Venison", "Cornish Hens")),
    ("Seafood", ("Salmon", "Shrimp", "Tuna", "Cod", "Crab", "Lobster", "Mussels", "Scallops", "Clams", "Oysters", "Squid", "Octopus", "Sardines", "Anchovies", "Haddock")),
    ("Dairy Products", ("Milk", "Cheese (Cheddar)", "Yogurt", "Butter", "Eggs", "Cream", "Cottage Cheese", "Sour Cream", "Cream Cheese", "Ricotta Cheese", "Mozzarella Cheese", "Parmesan Cheese", "Feta Cheese", "Swiss Cheese", "Gouda Cheese")),
    ("Grains and Cereals", ("Rice", "Bread (White)", "Pasta (Spaghetti)", "Oats", "Quinoa", "Barley", "Cornmeal", "Bulgur", "Farro", "Millet", "Couscous", "Buckwheat", "Polenta", "Rye", "Wheat Berries")),
    ("Bakery and Bread", ("Baguette", "Croissants", "Bagels", "Sourdough Bread", "Whole Wheat Bread", "Multigrain Bread", "Rye Bread", "Pita Bread", "English Muffins", "Focaccia Bread", "Ciabatta Bread", "Brioche", "Challah", "Pretzels", "Naan Bread")),
    ("Snacks and Sweets", ("Chocolate Bars", "Potato Chips", "Cookies (Chocolate Chip)", "Popcorn", "Ice Cream", "Candy (Gummy Bears)", "Pretzels (Salted)", "Nuts (Almonds)", "Trail Mix", "Granola Bars", "Brownies", "Cupcakes", "Donuts", "Marshmallows", "Fruit Snacks")),
    ("Beverages", ("Water", "Coffee", "Tea", "Soda (Cola)", "Juice (Orange)", "Sports Drinks", "Energy Drinks", "Milkshakes", "Smoothies", "Lemonade", "Iced Tea", "Hot Chocolate", "Coconut Water", "Kombucha", "Sparkling Water")),
    ("Condiments and Sauces", ("Ketchup", "Mustard", "Mayonnaise", "BBQ Sauce", "Soy Sauce", "Teriyaki Sauce", "Worcestershire Sauce", "Hot Sauce", "Ranch Dressing", "Caesar Dressing", "Balsamic Vinegar", "Olive Oil", "Honey", "Maple Syrup", "Salsa")),
    ("Fast Food", ("French Fries", "Pizza (Pepperoni)", "Hot Dogs", "Fried Chicken", "Tacos", "Burritos", "Fried Fish", "Onion Rings", "Milkshakes (Chocolate)", "Chicken Nuggets", "Breakfast Sandwiches", "Cheeseburgers", "Fried Shrimp", "Soft Drinks (Coke)")),
    ("Automotive Maintenance and Repair", ("General Maintenance", "Brake Systems", "Engine Repair and Tune-Up", "Transmission Services", "Electrical Systems", "Suspension and Steering", "HVAC Systems", "Exhaust Systems", "Diagnostic Services", "Body and Paint Repairs")),
    ("Baby Care", ("Infant Feeding and Nutrition", "Baby Gear and Equipment", "Baby Clothing and Apparel", "Diapering and Baby Hygiene", "Baby Health and Safety", "Baby Toys and Developmental Products", "Nursery Decor and Furniture", "Baby Bathing and Grooming", "Baby Travel and Outings", "Parenting Resources and Education")),
    ("Beauty and Personal Care", ("Skincare", "Haircare", "Cosmetics", "Personal Hygiene", "Men's Grooming", "Fragrances", "Natural and Organic Products", "Anti-Aging and Wellness", "Nail Care", "Beauty Tools and Accessories")),
    ("Men's Fashion", ("Casual Wear", "Formal Wear", "Business Casual Wear", "Athleisure Wear", "Outerwear", "Accessories", "Footwear", "Suits and Tailoring", "Streetwear", "Grooming and Personal Care")),
    ("Computers", ("Hardware Components", "Peripherals and Accessories", "Laptops and Notebooks", "Desktop Computers", "Tablets and Convertibles", "Servers and Workstations", "Networking Devices", "Storage Solutions", "Computer Software", "Gaming Hardware and Accessories")),
    ("Food", ("Fruits and Vegetables", "Meat and Poultry", "Seafood", "Dairy Products", "Grains and Cereals", "Snacks and Confectionery", "Beverages (Non-alcoholic)", "Alcoholic Beverages", "Frozen Foods", "Specialty and Gourmet Foods")),
    ("Stationery", ("Writing Instruments", "Notebooks and Journals", "Paper Products", "Planners and Organizers", "Desk Accessories", "Art Supplies", "Calendars and Appointment Books", "Filing and Storage Solutions", "School Supplies", "Crafting Materials"))
]


       

       
       
           


        def create_users():
            for _ in range(10):
                user = user_model.objects.create(
            name=f"User{_}",
            password="password123",  # Just an example password
            email=f"user{_}@example.com",
            registered=True,
            token=f"user_kjhub_{_}",
            ratings_count=random.randint(1, 100),
            views=random.randint(1, 1000),
            comments_count=random.randint(1, 50),
            latitude=random.randint(-90, 90),
            longitude=random.randint(-180, 180),
            area_code = f"Zone {random.randint(1, 7)}",

            frequency=random.randint(1, 10)
        )
       
        def create_categories_subcategories():
           
            # Electronics
           
   # Electronics
            primary_obj_electronics = primary_subcategory.objects.create(name="Games and Sports")

            secondary_obj_smartphones = secondary_subcategory.objects.create(ss_forekey="Games and Sports", sub_name="Indoor")
            last_category.objects.create(lc_forekey="Indoor", item_name="Futsal")
            last_category.objects.create(lc_forekey="Indoor", item_name="Fussball")
            last_category.objects.create(lc_forekey="Indoor", item_name="Carrom")
            last_category.objects.create(lc_forekey="Indoor", item_name="E-football")
            last_category.objects.create(lc_forekey="Indoor", item_name="Pool and snooker")
            last_category.objects.create(lc_forekey="Indoor", item_name="Voltaball")
            last_category.objects.create(lc_forekey="Indoor", item_name="Gym")
            last_category.objects.create(lc_forekey="Indoor", item_name="Zumba")
           

            secondary_obj_laptops = secondary_subcategory.objects.create(ss_forekey="Games and Sports", sub_name="Outdoor")
            last_category.objects.create(lc_forekey="Outdoor", item_name="KU football ground")
            last_category.objects.create(lc_forekey="Outdoor", item_name="Swimming")
            last_category.objects.create(lc_forekey="Outdoor", item_name="Badminton")
            last_category.objects.create(lc_forekey="Outdoor", item_name="Volleyball")




            primary_obj_clothing = primary_subcategory.objects.create(name="Stationary")

            secondary_obj_tshirts = secondary_subcategory.objects.create(ss_forekey="Stationary", sub_name="Pens")
            last_category.objects.create(lc_forekey="Pens", item_name="Ballpoint Pen")
            last_category.objects.create(lc_forekey="Pens", item_name="Gel pen")
            last_category.objects.create(lc_forekey="Pens", item_name="Fountain pen")
            last_category.objects.create(lc_forekey="Pens", item_name="Roller ball pen")
            last_category.objects.create(lc_forekey="Pens", item_name="Marker pen")
            last_category.objects.create(lc_forekey="Pens", item_name="Highlighters")

           

            secondary_obj_dresses = secondary_subcategory.objects.create(ss_forekey="Stationary", sub_name="Pencil")
            last_category.objects.create(lc_forekey="Pencil", item_name="Graphite Pencil")
            last_category.objects.create(lc_forekey="Pencil", item_name="Colored pencil")
            last_category.objects.create(lc_forekey="Pencil", item_name="mechanical pencil")
            last_category.objects.create(lc_forekey="Pencil", item_name="wooden pencil")
            secondary_obj_jeans = secondary_subcategory.objects.create(ss_forekey=primary_obj_clothing, sub_name="Jeans")
            last_category.objects.create(lc_forekey=secondary_obj_jeans, item_name="Generic Jeans 1")
            last_category.objects.create(lc_forekey=secondary_obj_jeans, item_name="Generic Jeans 2")

            secondary_obj_shoes = secondary_subcategory.objects.create(ss_forekey=primary_obj_clothing, sub_name="Shoes")
            last_category.objects.create(lc_forekey=secondary_obj_shoes, item_name="Generic Shoes 1")
            last_category.objects.create(lc_forekey=secondary_obj_shoes, item_name="Generic Shoes 2")

            secondary_obj_accessories = secondary_subcategory.objects.create(ss_forekey=primary_obj_clothing, sub_name="Accessories")
            last_category.objects.create(lc_forekey=secondary_obj_accessories, item_name="Generic Accessory 1")
            last_category.objects.create(lc_forekey=secondary_obj_accessories, item_name="Generic Accessory 2")

   # Books
            primary_obj_books = primary_subcategory.objects.create(name="Food")

            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Food", sub_name="Non-veg")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Food", sub_name="veg")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Food", sub_name="dairy products")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Food", sub_name="icecream")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Food", sub_name="bakery")
            last_category.objects.create(lc_forekey="Non-veg", item_name="Sausage")
            last_category.objects.create(lc_forekey="Non-veg", item_name="Chowmein")
            last_category.objects.create(lc_forekey="Non-veg", item_name="khajaset")
            last_category.objects.create(lc_forekey="Non-veg", item_name="Fried rice")
            last_category.objects.create(lc_forekey="Non-veg", item_name="Momo")
            last_category.objects.create(lc_forekey="Non-veg", item_name="Sekuwa")
            last_category.objects.create(lc_forekey="Non-veg", item_name="choila")
            last_category.objects.create(lc_forekey="veg", item_name="aalo")
            last_category.objects.create(lc_forekey="veg", item_name="chowmein")
            last_category.objects.create(lc_forekey="veg", item_name="momo")
            last_category.objects.create(lc_forekey="veg", item_name="sandwich")
            last_category.objects.create(lc_forekey="veg", item_name="appetizers")
            last_category.objects.create(lc_forekey="veg", item_name="drinks")
            last_category.objects.create(lc_forekey="veg", item_name="khana set")
            last_category.objects.create(lc_forekey="veg", item_name="roti")
            last_category.objects.create(lc_forekey="veg", item_name="soups")
            last_category.objects.create(lc_forekey="dairy products", item_name="milk")
            last_category.objects.create(lc_forekey="dairy products", item_name="cheese")
            last_category.objects.create(lc_forekey="dairy products", item_name="yogurt")
            last_category.objects.create(lc_forekey="dairy products", item_name="dahi")
            last_category.objects.create(lc_forekey="dairy products", item_name="butter")
            last_category.objects.create(lc_forekey="icecream", item_name="vanila")
            last_category.objects.create(lc_forekey="icecream", item_name="chocolate")
            last_category.objects.create(lc_forekey="icecream", item_name="strawberry")




            last_category.objects.create(lc_forekey="bakery", item_name="loaf bread")
            last_category.objects.create(lc_forekey="bakery", item_name="speciality bread")
            last_category.objects.create(lc_forekey="bakery", item_name="flat breads")
            last_category.objects.create(lc_forekey="bakery", item_name="choissants")
            last_category.objects.create(lc_forekey="bakery", item_name="darishes")
            last_category.objects.create(lc_forekey="bakery", item_name="muffins")
            last_category.objects.create(lc_forekey="bakery", item_name="layer cakes")
            last_category.objects.create(lc_forekey="bakery", item_name="cupcakes")
            last_category.objects.create(lc_forekey="bakery", item_name="cookies")

            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Dry cleaning service", sub_name="garment cleaning")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Dry cleaning service", sub_name="washing")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Dry cleaning service", sub_name="beddings and curtain cleaning")
       

            last_category.objects.create(lc_forekey="garment cleaning", item_name="suit")
            last_category.objects.create(lc_forekey="garment cleaning", item_name="blazer")
            last_category.objects.create(lc_forekey="garment cleaning", item_name="delicate")
            last_category.objects.create(lc_forekey="garment cleaning", item_name="silks")
            last_category.objects.create(lc_forekey="washing", item_name="shirt")
            last_category.objects.create(lc_forekey="washing", item_name="pant")
            last_category.objects.create(lc_forekey="washing", item_name="casual wear")
            last_category.objects.create(lc_forekey="washing", item_name="baby clothes")
            last_category.objects.create(lc_forekey="beddings and curtain cleaning", item_name="bedsheets")
            last_category.objects.create(lc_forekey="beddings and curtain cleaning", item_name="pillow")
            last_category.objects.create(lc_forekey="beddings and curtain cleaning", item_name="pillow sheets")
            last_category.objects.create(lc_forekey="beddings and curtain cleaning", item_name="curtain cleaning")

            primary_obj_books = primary_subcategory.objects.create(name="tailoring service")

            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="tailoring service", sub_name="custom tailoring")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="tailoring service", sub_name="tailoring adjustments")
       

            last_category.objects.create(lc_forekey="custom tailoring", item_name="custom dresses")
            last_category.objects.create(lc_forekey="custom tailoring", item_name="custom suits")
            last_category.objects.create(lc_forekey="tailoring adjustments", item_name="sleeves adjustment")
            last_category.objects.create(lc_forekey="tailoring adjustments", item_name="waist adjustment")
           
            primary_obj_books = primary_subcategory.objects.create(name="clothes treatment")

            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="clothes treatment", sub_name="fabric protection")
       

            last_category.objects.create(lc_forekey="fabric protection", item_name="stain guard")
            last_category.objects.create(lc_forekey="fabric protection", item_name="leather guard")
           
            primary_obj_books = primary_subcategory.objects.create(name="Eco-friendly services")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Eco-friendly services", sub_name="recycling programs")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="Eco-friendly services", sub_name="eco-friendly cleaning")
            last_category.objects.create(lc_forekey="recycling programs", item_name="hanger recycling")
            last_category.objects.create(lc_forekey="recycling programs", item_name="plastic bags")
            last_category.objects.create(lc_forekey="recycling programs", item_name="garment bags")
            last_category.objects.create(lc_forekey="eco-friendly cleaning", item_name="ecofriendly wet cleaning")
           

            primary_obj_books = primary_subcategory.objects.create(name="printing services")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="printing services", sub_name="black and white printing")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="printing services", sub_name="color printing")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="printing services", sub_name="binding services")
            last_category.objects.create(lc_forekey="binding services", item_name="thermal binding")
            last_category.objects.create(lc_forekey="binding services", item_name="wire binding")
            last_category.objects.create(lc_forekey="binding services", item_name="tape plastic binding")
            last_category.objects.create(lc_forekey="black and white printing", item_name="standard document")
            last_category.objects.create(lc_forekey="black and white printing", item_name="legal document")
            last_category.objects.create(lc_forekey="color printing", item_name="brochures")
            last_category.objects.create(lc_forekey="color printing", item_name="flyers")


            primary_obj_books = primary_subcategory.objects.create(name="photo servicing")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="photo servicing", sub_name="photo printing")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="photo servicing", sub_name="photo restoration")
            last_category.objects.create(lc_forekey="photo printing", item_name="standard photo prints")
            last_category.objects.create(lc_forekey="photo printing", item_name="enlargements/ phoster size prints")
            last_category.objects.create(lc_forekey="photo restoration", item_name="digital restoration")
           

            primary_obj_books = primary_subcategory.objects.create(name="hair salon and parlour")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="hair salon and parlour", sub_name="hair cuts")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="hair salon and parlour", sub_name="styling")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="hair salon and parlour", sub_name="coloring")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="hair salon and parlour", sub_name="hair treatments")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="hair salon and parlour", sub_name="shaving")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="hair salon and parlour", sub_name="facial hair removal")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="hair salon and parlour", sub_name="massage")
            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey="hair salon and parlour", sub_name="facials")
           

            last_category.objects.create(lc_forekey="hair cuts", item_name="man haircut")
            last_category.objects.create(lc_forekey="hair cuts", item_name="women's haircut")
            last_category.objects.create(lc_forekey="hair cuts", item_name="child")
            last_category.objects.create(lc_forekey="styling", item_name="blowdrying")
            last_category.objects.create(lc_forekey="styling", item_name="curling")
            last_category.objects.create(lc_forekey="styling", item_name="updos")
            last_category.objects.create(lc_forekey="styling", item_name="straighting")
            last_category.objects.create(lc_forekey="coloring", item_name="full color")
            last_category.objects.create(lc_forekey="coloring", item_name="root touchup")
            last_category.objects.create(lc_forekey="coloring", item_name="color correction")
            last_category.objects.create(lc_forekey="hair treatments", item_name="deep conditioning")
            last_category.objects.create(lc_forekey="hair treatments", item_name="scalp treatments")
            last_category.objects.create(lc_forekey="hair treatments", item_name="hair repair")
            last_category.objects.create(lc_forekey="hair treatments", item_name="keratin treatment")
            last_category.objects.create(lc_forekey="shaving", item_name="beard trimming")
            last_category.objects.create(lc_forekey="shaving", item_name="mustache trimming")
            last_category.objects.create(lc_forekey="shaving", item_name="hot towel shave")
            last_category.objects.create(lc_forekey="facial hair removal", item_name="waxing")
            last_category.objects.create(lc_forekey="facial hair removal", item_name="threading")
            last_category.objects.create(lc_forekey="massage", item_name="body massage")
            last_category.objects.create(lc_forekey="facials", item_name="basic facial")
            last_category.objects.create(lc_forekey="facials", item_name="advance facial")

            secondary_obj_dresses = secondary_subcategory.objects.create(ss_forekey="Stationary", sub_name="notebooks")
            last_category.objects.create(lc_forekey="notebooks", item_name="journals")
            last_category.objects.create(lc_forekey="notebooks", item_name="copies")
            last_category.objects.create(lc_forekey="notebooks", item_name="spiral notebooks")
            last_category.objects.create(lc_forekey="notebooks", item_name="legal pads")
            secondary_obj_dresses = secondary_subcategory.objects.create(ss_forekey="Stationary", sub_name="loosepapers")
            last_category.objects.create(lc_forekey="loosepapers", item_name="loose sheets")
            last_category.objects.create(lc_forekey="loosepapers", item_name="graphs")
            last_category.objects.create(lc_forekey="loosepapers", item_name="plain paper")
            last_category.objects.create(lc_forekey="loosepapers", item_name="A4 papers")
            last_category.objects.create(lc_forekey="loosepapers", item_name="drawing sheets")
            last_category.objects.create(lc_forekey="loosepapers", item_name="printer paper")
            secondary_obj_dresses = secondary_subcategory.objects.create(ss_forekey="Stationary", sub_name="sticky notes")
            last_category.objects.create(lc_forekey="sticky notes", item_name="super sticky notes")
            last_category.objects.create(lc_forekey="sticky notes", item_name="arrow pages")


            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="sausage" , name="buff sausage")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="sausage" , name="chicken sausage")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="chowmein" , name="buff chowmein")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="chowmein" , name="chicken chowmein")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="chowmein" , name="egg chowmein")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="khaja set" , name="buff")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="khaja set" , name="chicken")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="fried rice" , name="buff fried rice")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="fried rice" , name="chicken fried rice")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="momo" , name="buff momo")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="momo" , name="chicken momo")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="momo" , name="buff fried")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="momo" , name="chicken fried")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="momo" , name="steam buff")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="momo" , name="steam chicken")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="sekuwa" , name="buff sekuwa")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="sekuwa" , name="chicken sekuwa")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="sekuwa" , name="pork sekuwa")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="sekuwa" , name="chicken fried")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="sekuwa" , name="buff fried")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="choila" , name="buff choila")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="choila" , name="pork choila")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "Non-veg",item="choila" , name="chicken")







            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="aalu" , name="aalu stick")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="aalu" , name="alu fry tarkari")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="aalu" , name="jhol tarkari")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="chowmein" , name="veg chowmein")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="chowmein" , name="veg thukpa")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="momo" , name="veg momo")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="momo" , name="veg fry momo")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="sandwich" , name="khaja toast")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="sandwich" , name="salad sandwich")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="appetizers" , name="pakoda")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="appetizers" , name="samosa")
            create_db = food_cate.objects.create(category_first = "food" , sub_cate = "veg",item="soups" , name="mushroom soup")
           



        def create_businesses():
            category_db = primary_subcategory.objects.all()
            categories = []
            for i in category_db:
                if i.name not in categories:
                    categories.append(i.name)
            for _ in range(10):
                category = random.choice(categories)
                area_wise_views = [("area_"+str(random.randint(1,7)), random.randint(100,10000)) for _ in range(3)]
                business = business_model.objects.create(
                    name=f"{category} {_}",
                    contacts=random.randint(1000000000, 9999999999),
                    description=f"This is a {category} located at Zone{_}",
                    token=f"business{_}token",
            ratings_parameter=random.randint(1, 10),
            category=category,
            password = "password123",
            reviews=random.randint(10, 100),
            avg_rating=random.randint(1, 5),
            today_views=random.randint(50, 500),
            monthly_views=random.randint(500, 5000),
            latitude=random.randint(-90, 90),
            longitude=random.randint(-180, 180),
            area_wise_views=area_wise_views,
            mva=area_wise_views[2],  # Just an example, choose as needed
            views_record="",
            owner = "Saurav Bhujel",
           
            listed_items = (("Smartphones" ,("iPhone 13 Pro Max" ,  "Samsung Galaxy S21 Ultra" , "Google Pixel 6 Pro","OnePlus 9 Pro")))
        )
        def create_products():
            categories = primary_subcategory.objects.all()
    
            for _ in range(1, 900):
                category = random.choice(categories)
        
                if category.name == "Food":
                    continue
        
                businessesd = business_model.objects.filter(category=category.name)
                if not businessesd.exists():
                    continue
        
                businesses = random.choice(list(businessesd))
        
                sub_category = secondary_subcategory.objects.filter(ss_forekey=category.name)
                if not sub_category.exists():
                    continue
        
                sub_categories = random.choice(list(sub_category))
        
                product = product_models.objects.create(
            product_name=f"{category.name} Product{_}",
            price=random.randint(100, 1000),
            description=f"This is a description for {category.name} product {_}",
            token=f"product{_}token",
            price_range=random.choice(["very_high", "high", "medium", "affordable"]),
            views=random.randint(1, 500),
            likes=random.randint(1, 50),
            business_mdl=businesses,
            category=category.name,
            sub_category=sub_categories.sub_name,
            weight=random.randint(100, 5000),
            images="static/images/food.jpg",
            item_named=sub_categories.sub_name,
            size=f"{random.randint(5, 50)}x{random.randint(5, 50)}",
            negotiable=random.choice([True, False])
        )
        for _ in range(1,900):
            try:
                cates = random.choice(food_cate.objects.all())
                businessesd = business_model.objects.filter(category = cates.category_first)   
            except IndexError:
                cates = {
                "category_first":"Food" ,
"sub_cate":"veg",
"item":"momo",
"name":"veg_momo",
                
                }
                businessesd = business_model.objects.filter(category=cates['category_first'])

            int2 = random.randint(0,3)
            price_range = ["very_high" , "high","medium" ,"affordable"]
            
    
            try:
                businesses = random.choice(list(businessesd))
            except IndexError:
        # Handle the case where there are no businesses found
                continue 
            product = product_models.objects.create(
            product_name=f"{cates.category_first} Product{_}",
            price=random.randint(100, 1000),
            description=f"This is a description for {cates.category_first} product {_}",
            token=f"product{_}token",
            price_range = price_range[int2],
            views=random.randint(1, 500),
            likes=random.randint(1, 50),
            business_mdl = businesses,
            category=cates.category_first,
            sub_category=cates.sub_cate,
            weight=random.randint(100, 5000),
            images = "static/images/food.jpg",
            item_named = cates.item,
            size=f"{random.randint(5, 50)}x{random.randint(5, 50)}",
            negotiable=random.choice([True, False])
        )
        '''def create_categories_subcategories():
            categories = ["Electronics", "Clothing", "Books", "Home Decor", "Sports & Outdoors"]
            subcategories = {
        "Electronics": ["Smartphones", "Laptops", "Tablets", "Headphones", "Cameras"],
        "Clothing": ["T-shirts", "Dresses", "Jeans", "Shoes", "Accessories"],
        "Books": ["Fiction", "Non-fiction", "Biography", "Science Fiction", "Mystery"],
        "Home Decor": ["Furniture", "Lighting", "Wall Art", "Rugs", "Decorative Pillows"],
        "Sports & Outdoors": ["Fitness Equipment", "Outdoor Gear", "Sportswear", "Camping Supplies", "Biking Accessories"]
    }
   
            for category, sub_cats in subcategories.items():
                category_obj = categories_subcategories.objects.create(category=category, sub_category=sub_cats)

        '''

       
        def create_ratings():
            users = user_model.objects.all()
            products = product_models.objects.all()
            for _ in range(10):
                user = random.choice(users)
                product = random.choice(products)
                rating = random.randint(1, 5)
                ratings.objects.create(
            user=user,
            product_id=product,
            ratings=rating
        )

        def create_area_data():
            for _ in range(10):
                a = random.randint(1,7)
                area = area_data.objects.create(
            area_number = a,
            food = "None",
        )

       
        def create_history():
            users = user_model.objects.all()
            businesses = business_model.objects.all()
            primary_cats = primary_subcategory.objects.all()
            sec_cats = secondary_subcategory.objects.all()
            last_cats = last_category.objects.all()
            prod = product_models.objects.all()
           

            for _ in range(1, 1000):
                primary_cat = random.choice(primary_cats)
                sec_cat = random.choice(sec_cats)
                last_cat_instance = random.choice(last_cats)
                business_instance = random.choice(businesses)

        # Make sure that sec_cat and last_cat_instance are logically related to primary_cat and sec_cat respectively
               
                history_save = history.objects.create(
                user=random.choice(users),
                business=business_instance,
                category=primary_cat.name,
                subcategory=sec_cat.sub_name,
                item_name=last_cat_instance.item_name,
                product=random.choice(prod),
                    )
        def lcl(word):#letter_count_list
   
            counts = [0] * 26

   
            for letter in word:
       
                index = ord(letter.lower()) - ord('a')
       
                if 0 <= index < 26:
                    counts[index] += 1

            return counts    
        def bookmark_saver():
            products = product_models.objects.all()
            user = user_model.objects.all()
            for _ in range(100):
                bookmark_saver1 = bookmarked.objects.create(
                user = random.choice(user) ,
                product = random.choice(products)
           
           
                )
           
        def list_maker_func():
            result_list = []

            product_model = product_models.objects.all()
            business_modeled = business_model.objects.all()
            area_data_model = area_data.objects.all()
            primary_subcategory_m = primary_subcategory.objects.all()
            secondary_subcategory_m = secondary_subcategory.objects.all()
            last_category_m = last_category.objects.all()

            for i in product_model:
                smas = lcl(i.product_name)
                result_list.append((i.product_name, smas))

            for i in business_modeled:
                smas = lcl(i.name)
                result_list.append((i.name, smas))
            for i in primary_subcategory_m:
                smas = lcl(i.name)
                result_list.append((i.name, smas))

            for i in secondary_subcategory_m:
                smas = lcl(i.sub_name)
                result_list.append((i.sub_name, smas))

            for i in last_category_m:
                smas = lcl(i.item_name)
                result_list.append((i.item_name, smas))

            with open("list_maker.txt", "w") as file:
                json.dump(result_list, file, indent=4)
        def populate_database():
            create_categories_subcategories()
            create_users()
           
            create_businesses()
            create_products()
            create_ratings()
            
            create_history()
            bookmark_saver()
            create_area_data()
            list_maker_func()

       
# Call the populate_database function to populate the database with the generated data
        populate_database()
        self.stdout.write(self.style.SUCCESS('Demo data populated successfully!'))