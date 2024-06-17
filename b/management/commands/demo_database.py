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
            area_code = f"Area_{random.randint(1, 7)}",

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
            last_category.objects.create(lc_forekey="Pens", item_name="")
            last_category.objects.create(lc_forekey=secondary_obj_tshirts, item_name="Generic T-shirt 2")

            secondary_obj_dresses = secondary_subcategory.objects.create(ss_forekey=primary_obj_clothing, sub_name="Dresses")
            last_category.objects.create(lc_forekey=secondary_obj_dresses, item_name="Generic Dress 1")
            last_category.objects.create(lc_forekey=secondary_obj_dresses, item_name="Generic Dress 2")

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
            primary_obj_books = primary_subcategory.objects.create(name="Books")

            secondary_obj_fiction = secondary_subcategory.objects.create(ss_forekey=primary_obj_books, sub_name="Fiction")
            last_category.objects.create(lc_forekey=secondary_obj_fiction, item_name="Generic Fiction 1")
            last_category.objects.create(lc_forekey=secondary_obj_fiction, item_name="Generic Fiction 2")

            secondary_obj_nonfiction = secondary_subcategory.objects.create(ss_forekey=primary_obj_books, sub_name="Non-fiction")
            last_category.objects.create(lc_forekey=secondary_obj_nonfiction, item_name="Generic Non-fiction 1")
            last_category.objects.create(lc_forekey=secondary_obj_nonfiction, item_name="Generic Non-fiction 2")

            secondary_obj_biography = secondary_subcategory.objects.create(ss_forekey=primary_obj_books, sub_name="Biography")
            last_category.objects.create(lc_forekey=secondary_obj_biography, item_name="Generic Biography 1")
            last_category.objects.create(lc_forekey=secondary_obj_biography, item_name="Generic Biography 2")

            secondary_obj_scifi = secondary_subcategory.objects.create(ss_forekey=primary_obj_books, sub_name="Science Fiction")
            last_category.objects.create(lc_forekey=secondary_obj_scifi, item_name="Generic Sci-Fi 1")
            last_category.objects.create(lc_forekey=secondary_obj_scifi, item_name="Generic Sci-Fi 2")

            secondary_obj_mystery = secondary_subcategory.objects.create(ss_forekey=primary_obj_books, sub_name="Mystery")
            last_category.objects.create(lc_forekey=secondary_obj_mystery, item_name="Generic Mystery 1")
            last_category.objects.create(lc_forekey=secondary_obj_mystery, item_name="Generic Mystery 2")

   # Home Decor
            primary_obj_homedecor = primary_subcategory.objects.create(name="Home Decor")

            secondary_obj_furniture = secondary_subcategory.objects.create(ss_forekey=primary_obj_homedecor, sub_name="Furniture")
            last_category.objects.create(lc_forekey=secondary_obj_furniture, item_name="Generic Furniture 1")
            last_category.objects.create(lc_forekey=secondary_obj_furniture, item_name="Generic Furniture 2")

            secondary_obj_lighting = secondary_subcategory.objects.create(ss_forekey=primary_obj_homedecor, sub_name="Lighting")
            last_category.objects.create(lc_forekey=secondary_obj_lighting, item_name="Generic Lighting 1")
            last_category.objects.create(lc_forekey=secondary_obj_lighting, item_name="Generic Lighting 2")

            secondary_obj_wallart = secondary_subcategory.objects.create(ss_forekey=primary_obj_homedecor, sub_name="Wall Art")
            last_category.objects.create(lc_forekey=secondary_obj_wallart, item_name="Generic Wall Art 1")
            last_category.objects.create(lc_forekey=secondary_obj_wallart, item_name="Generic Wall Art 2")

            secondary_obj_rugs = secondary_subcategory.objects.create(ss_forekey=primary_obj_homedecor, sub_name="Rugs")
            last_category.objects.create(lc_forekey=secondary_obj_rugs, item_name="Generic Rug 1")
            last_category.objects.create(lc_forekey=secondary_obj_rugs, item_name="Generic Rug 2")

            secondary_obj_pillows = secondary_subcategory.objects.create(ss_forekey=primary_obj_homedecor, sub_name="Decorative Pillows")
            last_category.objects.create(lc_forekey=secondary_obj_pillows, item_name="Generic Pillow 1")
            last_category.objects.create(lc_forekey=secondary_obj_pillows, item_name="Generic Pillow 2")

   # Sports & Outdoors
            primary_obj_sportsoutdoors = primary_subcategory.objects.create(name="Sports & Outdoors")

            secondary_obj_fitnessequipment = secondary_subcategory.objects.create(ss_forekey=primary_obj_sportsoutdoors, sub_name="Fitness Equipment")
            last_category.objects.create(lc_forekey=secondary_obj_fitnessequipment, item_name="Generic Fitness 1")
            last_category.objects.create(lc_forekey=secondary_obj_fitnessequipment, item_name="Generic Fitness 2")

            secondary_obj_outdoorgear = secondary_subcategory.objects.create(ss_forekey=primary_obj_sportsoutdoors, sub_name="Outdoor Gear")
            last_category.objects.create(lc_forekey=secondary_obj_outdoorgear, item_name="Generic Outdoor 1")
            last_category.objects.create(lc_forekey=secondary_obj_outdoorgear, item_name="Generic Outdoor 2")

            secondary_obj_sportswear = secondary_subcategory.objects.create(ss_forekey=primary_obj_sportsoutdoors, sub_name="Sportswear")
            last_category.objects.create(lc_forekey=secondary_obj_sportswear, item_name="Generic Sportswear 1")
            last_category.objects.create(lc_forekey=secondary_obj_sportswear, item_name="Generic Sportswear 2")

            secondary_obj_campingsupplies = secondary_subcategory.objects.create(ss_forekey=primary_obj_sportsoutdoors, sub_name="Camping Supplies")
            last_category.objects.create(lc_forekey=secondary_obj_campingsupplies, item_name="Generic Camping 1")
            last_category.objects.create(lc_forekey=secondary_obj_campingsupplies, item_name="Generic Camping 2")

            secondary_obj_bikingaccessories = secondary_subcategory.objects.create(ss_forekey=primary_obj_sportsoutdoors, sub_name="Biking Accessories")
            last_category.objects.create(lc_forekey=secondary_obj_bikingaccessories, item_name="Generic Biking 1")
            last_category.objects.create(lc_forekey=secondary_obj_bikingaccessories, item_name="Generic Biking 2")

       
        
        

        def create_businesses():
            categories = ["Restaurant", "Clothing Store", "Bookstore", "Electronics Shop", "Fitness Center"]
            for _ in range(10):
                category = random.choice(categories)
                area_wise_views = [("area_"+str(random.randint(1,7)), random.randint(100,10000)) for _ in range(3)]
                business = business_model.objects.create(
                    name=f"{category} {_}",
                    contacts=random.randint(1000000000, 9999999999),
                    description=f"This is a {category} located at Area{_}",
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
            categories = ["Electronics", "Clothing", "Books", "Home Decor", "Sports & Outdoors"]
            subcategories = {
        "Electronics": ["Smartphones", "Laptops", "Tablets", "Headphones", "Cameras"],
        "Clothing": ["T-shirts", "Dresses", "Jeans", "Shoes", "Accessories"],
        "Books": ["Fiction", "Non-fiction", "Biography", "Science Fiction", "Mystery"],
        "Home Decor": ["Furniture", "Lighting", "Wall Art", "Rugs", "Decorative Pillows"],
        "Sports & Outdoors": ["Fitness Equipment", "Outdoor Gear", "Sportswear", "Camping Supplies", "Biking Accessories"]
    }       
            businesses = business_model.objects.get(token = "business0token")
            
            for _ in range(1,9):
                category = random.choice(categories)
                subcategory = random.choice(subcategories[category])
                price_range = ["very_high" , "high","medium" ,"affordable"]
                
                
                int2 = random.randint(0,3)
                product = product_models.objects.create(
                    product_name=f"{category} Product{_}",
            price=random.randint(1000, 1000000),
            description=f"This is a description for {category} product {_}",
            token=f"product{_}token",
            price_range = price_range[int2],
            views=random.randint(1, 500),
            likes=random.randint(1, 50),
            business_mdl = businesses,
            category=category,
            sub_category=subcategory,
            weight=random.randint(100, 5000),
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
