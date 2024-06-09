from django.db import models
from django.conf import settings 
from datetime import date ,datetime,time
import schedule
from django.utils import timezone
import json
# Create your models here.
class user_model(models.Model):
    name = models.CharField(max_length = 100,null=True)
    password = models.CharField(max_length = 200,null=True)
    email = models.CharField(max_length = 100)
    registered = models.BooleanField(default = 0,null=True)
    token = models.CharField(max_length = 100 , primary_key = True)
    ratings_count = models.IntegerField(null=True)
    views = models.IntegerField(null = True)
    comments_count = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    area_code = models.CharField(max_length = 20)
    frequency = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
class business_trackrecord(models.Model):
    name = models.CharField(max_length = 20)



    
class business_model(models.Model):
    name = models.CharField(max_length = 100)
    contacts = models.IntegerField(null=True)
    description = models.TextField()
    token = models.CharField(max_length = 100 , primary_key = True)
    #interaction = models.Foreignkey(interactions , on_delete = models.CASCADE)
    ratings_parameter = models.IntegerField(null=True)
    password = models.CharField(null=True , max_length = 100)
    category = models.CharField(max_length = 100)
    area_wise_views = models.TextField()#(area,views)
    reviews = models.IntegerField(null=True)
    avg_rating = models.IntegerField(null=True)
    img = models.ImageField(upload_to = "static/" , null = True , default = "static/images/business.jpg")
    today_views = models.IntegerField(null=True)
    monthly_views = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    mva = models.TextField()#most_viewed_area
    views_record = models.TextField()
    owner = models.CharField(max_length = 100)
    dob = models.DateField(default="2023-5-23")
    listed_items = models.TextField()
        
    def auto_update(self):
        now = datetime.now()
        hour = now.hour
        if hour == 0:
            self.monthly_views += self.today_views
            self.today_views = 0
        
            self.save()
    schedule.every().hour.do(auto_update)
    def auto_update_parameter(self):
        self.ratings_parameter = reviews * (avg_ratings/100)
    def set_list(self, area_wise_views):
        self.data = json.dumps(area_wise_views)  # Serialize the list to JSON

    def get_list(self):
        return json.loads(self.area_wise_views)
    def set_mva_list(self , data):  
        self.mva = json.dumps(data)
    def get_mva_list(self):
        return json.loads(mva)
class product_models(models.Model):
    product_name = models.CharField(max_length = 200)
    price = models.IntegerField(null=True)
    description = models.TextField()
    token = models.CharField(max_length = 100 , primary_key = True)
    views = models.IntegerField(null=True)
    business_mdl = models.ForeignKey(business_model , on_delete = models.CASCADE , null=True)
    likes = models.IntegerField(null=True)
    picture = models.ImageField(upload_to = "static/" , null = True , default ="static/images/product.jpg")
    price_range = models.CharField(null = True , max_length = 20)
    category = models.CharField(max_length = 200)
    sub_category = models.CharField(max_length = 200)
    weight = models.IntegerField(null=True)
    size = models.CharField(max_length = 100)
    negotiable = models.BooleanField()
    images = models.ImageField(upload_to = 'static/' , null = True , default="staic/images/product.jpg")
   # varients = models.Foreignkey()#list of productid
    #comments = models. list of comment id 
class ratings(models.Model):
    user = models.ForeignKey(user_model , on_delete = models.CASCADE)
    product_id = models.ForeignKey(product_models , on_delete = models.CASCADE)
    ratings = models.IntegerField(null=True)
    datetime = models.DateTimeField(default = timezone.now)
            
class category_saver(models.Model):
    category = models.CharField(max_length = 300)
    subcategory = models.TextField()
class update_business_models_at_midnight():
    now = datetime.now()
    # Check if it's 12 PM (noon)
    if now.time() == time(12, 0):
        # Call auto_update for all business models
        for model in business_model.objects.all():
            model.auto_update()
def current_time():
    return datetime.now().time()
    
class history(models.Model):
    user = models.ForeignKey(user_model , on_delete = models.CASCADE)
    business = models.ForeignKey(business_model , on_delete = models.CASCADE)
    category = models.CharField(max_length = 200)
    subcategory = models.CharField(max_length = 200)
    item_name = models.CharField(max_length = 200)
    product = models.ForeignKey(product_models , on_delete = models.CASCADE)
    time = models.TimeField(default=current_time)
    
class comments(models.Model):
    comment_token = models.CharField(max_length = 100)
    user = models.ForeignKey(user_model , on_delete = models.CASCADE)
    product_id = models.ForeignKey(product_models , on_delete = models.CASCADE)
    comment = models.TextField()
    business = models.ForeignKey(business_model , on_delete = models.CASCADE)   
    datetime = models.DateTimeField()    
'''class business_trackrecord(models.Model):
    product = models.ForeignKey(product_models , on_delete = models.CASCADE)
    business = models.ForeignKey(business_model , on_delete = models.CASCADE)
    user = models.ForeignKey(user_model , on_delete = models.CASCADE)'''
class area_data(models.Model):
    area_number = models.IntegerField(null=True)
    food  = models.TextField()
    def get_tokenized(self,data):
        var1 = json.dumps(data)
        for (token , views) in var1:
            var2 = chr(token)
            char_ext = ""
            for words  in var2:
                if words == "_":
                    break 
                char_ext+=words    
                
class categories_subcategories(models.Model):   
    category = models.CharField(max_length = 200)
    sub_category = models.TextField()
    def set_data(self , data):
        self.sub_category = jsons.dump(data)
    def get_data(self):
        return json.loads(sub_category)
class views_recorder(models.Model):
    user = models.ForeignKey(user_model , on_delete = models.CASCADE , primary_key = True)
    data_meta = models.TextField(null=True)
    def set_data(self , data_given):
        self.data_meta = json.dumps(data_given)
        
    def get_data(self):
        return json.loads(self.data_meta)
class primary_subcategory(models.Model):

    name = models.CharField(max_length = 20)
class secondary_subcategory(models.Model):
    ss_forekey = models.CharField(max_length = 200)
    sub_name = models.CharField(max_length = 200)
class last_category(models.Model):
    lc_forekey = models.CharField(max_length = 200)

    item_name = models.CharField(max_length = 200)
class bookmarked(models.Model):
    token = models.CharField(max_length = 200)
    user = models.ForeignKey(user_model , on_delete = models.CASCADE)
    product = models.CharField(max_length = 20)
    business = models.CharField(max_length = 20)