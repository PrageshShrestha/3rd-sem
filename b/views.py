# Django imports
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session
from django import template
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
# External library imports
import ast
import pandas as pd
import numpy as np
import random
import string
import re
import json
import ssl
import smtplib
from email.message import EmailMessage
from math import sqrt
from datetime import date, timedelta
import schedule

# Local Django model imports
from .models import (
    categories_subcategories,
    product_models,
    comments,
    category_saver,
    ratings,
    user_model,
    history,
    business_model,
    primary_subcategory,
    views_recorder,
    secondary_subcategory,
    last_category,
    bookmarked,
)

# Project-specific settings import
from a import settings

# Ensure consistent spacing

def requested(request):
    r = request.POST
    return r 
def searcher(request,query_string):
    def category_finder(query_string):
        query_string = query_string.split()
        processed_array = []
        for i in query_string:
            j = i.lower()
            processed_array.append(j)
        
        return processed_array 
    
    def lcl(word):#letter_count_list
    # Initialize a list of 26 zeros, one for each letter of the alphabet
        counts = [0] * 26

    # Iterate over each letter in the word
        for letter in word:
        # Convert the letter to lowercase and calculate its index in the alphabet (0-indexed)
            index = ord(letter.lower()) - ord('a')
        # Increment the count for that letter
            if 0 <= index < 26:
                counts[index] += 1

        return counts
    def sma(list1, list2):
    # Convert lists to NumPy arrays
    
        arr1 = np.array(list1)
        arr2 = np.array(list2)
    
    # Calculate the squared difference between corresponding elements
        squared_diff = (arr1 - arr2) ** 2
    
    # Calculate the mean of the squared differences
        mse = np.mean(squared_diff)
    
        return mse
    def list_content_maker():
        with open('list_maker.txt', 'r') as file:
            file_content = file.read()
        try:
            data_list = ast.literal_eval(file_content)
        except (ValueError, SyntaxError):
            print("Error: The file content is not a valid Python list.")
            data_list = []
        return data_list
        
    def jethalal(word):
        worded = lcl(word)
        smas = []
        list_content = list_content_maker()
        for i in list_content:
            sma_cal = sma(worded , i[1])
            smas.append((sma_cal , i[0]))
        sorted_list = sorted(smas, key=lambda x: x[0], reverse=False)    
        most_milne = sorted_list[0]
        if most_milne[1][3:] == word[3:]:
            return most_milne 
        else:
            return_list = [1 , "none"]
            return return_list
    def baga(words):
        most_milne_token = []
        vector_to_find = []
        for i in words:
            one_word_removed = i[:-1]
            two_word_removed = i[:-2]
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            most_milne_one = []
            for word in alphabet:
            
                word3 = i + word 
            
                smas_calc = jethalal(word3)
                most_milne_one.append(smas_calc)
            sorted_one = sorted(most_milne_one , key = lambda x:x[0] , reverse = False)
            most_mil = sorted_one[0]
            actual_thing = jethalal(i)
            owr_milne = jethalal(one_word_removed)
            twr_milne = jethalal(two_word_removed)
            appended = [most_mil , actual_thing , owr_milne , twr_milne]
            sorted_two = sorted(appended , key = lambda x:x[0] , reverse = False)
            if sorted_two[0][0]<0.04:
                most_milne_token.append((sorted_two[0][1] , i))
            sorted_two = []    
        print(most_milne_token)
        return most_milne_token 
    
    words = category_finder(query_string)   
    listed = baga(words)  
    categories = []
    category = primary_subcategory.objects.all()
    for i in category:
        subcat = item_name_giver(request , i.name)
        categories.append((str(i.name) , subcat))
    #categories = [(("Junk food") , ["momo" , "chowmein" , "pizza"])]
    sorted_cat = []
    for i in listed:
        searching_word = i[0]
        for cat , mouse in categories:
            for j in mouse:
                if str(j)== str(searching_word):
                    sorted_cat.append(cat)
                    break
        #print(f"the word is {searching_word} ,actual word is {i[1]} and sorted is {sorted_cat[0]}")
        #the word is momo , actual word is chowmei and sorted is Junk Food.
    return sorted_cat 

#searcher(query_string)
def test(request):




    context = {
    "content":'hello world',
    "success":'success',
    
    
    }
    return render(request , "test.html" , context)
def signup(request):
    r = request.POST
    
    if request.method == "POST":
        r = request.POST
        password = r.get("password")
        name = r.get("username")
        email = r.get("email")
        if not user_model.objects.filter(email = email).exists():
            if email=="admin" and password == admin_pass:
                admined = user_model(email = "admin" , username = "admin" , password = admin_pass)
                admined.save()
                request.session["user_number"] = "admin"
                data = {
                "already":"admin",
                }
                return JsonResponse(data , safe = False)
            else:
                total = [email , name , password]
                request.session["total"] = total
                extravar = "none"
                data = {
                "already":"true_otp",
                
                }
                extra_var = "none"
                Email(request , email , extra_var)
                return JsonResponse(data  , safe = False)
        else:
            data = {
            "already":"true",
            
            }
            return JsonResponse(data , safe = False)
    
    return render(request , "signup.html")
   
    
def Email(request , receiver,extra_var):
    
    email_sender = 'binormus007@gmail.com'
    email_password = "gzmljziqphfqnflw"
    email_receiver = str(receiver)
    if extra_var =='hello':
        em = EmailMessage()
        em ['From'] = email_sender
        em['To'] = email_receiver
        number = random.randint(4567 , 9999)
        em['Subject'] = "OTP for Account Security - Action Required"

        body = f"Hello User,\n\nYou have requested to change your Email or Phone number to ours. If you did not initiate this change, please treat this email with report to Google or to our team in given Email below .\n\nTo ensure your account's security, we have sent you a One-Time Password (OTP). Please use the following OTP to verify your request:\n\nOTP: {number}\n\nIf you did not make this request or believe it's an unauthorized action, please contact our support team immediately or report this issue at binormus007@gmail.com.\n\nThank you for your attention to this matter.\n\nBest Regards,\nSBGS"

        request.session['number'] = number
        em.set_content(body)
        context= ssl.create_default_context()
        
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com' , 465 , context = context) as smtp:
                smtp.login(email_sender , email_password)
        
                smtp.sendmail(email_sender , email_receiver , em.as_string())
            
        except:
            print("none")
        
           
    else:
        number = random.randint(4567, 9999)

# Store the OTP in the user's session (assuming request is defined)
        request.session['number'] = number

# Create the email message
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = "Sign-Up Authentication - One-Time Password (OTP)"
        body = f"Hello User,\n{number} is your One-Time Password (OTP).\n\nIf you did not initiate this process, please treat this email with report to Google or to our team in Same Email.Please use this OTP to authenticate your sign-up process.Please don't share your OTP with anyone for security purposes.\n\nIf you didn't request this OTP, you can safely ignore this email.\n\nBest Regards,\n\nSBGS."

# Construct the email body using HTML format
        em.set_content(body)

# Send the email using SSL
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com' , 465 , context = context) as smtp:
                smtp.login(email_sender , email_password)
        
                smtp.sendmail(email_sender , email_receiver , em.as_string())
        except:
            print("none")       
        
          
def otp(request , email_receiver):
    password = 0
    email=0
    ps = 0
    em = 0
    if "new_password" in request.session:
        password = request.session["new_password"]
        ps = 1
    if "new_email" in request.session:
        email = request.session["new_email"]
        em = 1
    context = {
    "email":email_receiver , 
    "otp":request.session["number"],
    "password_received":password,
    "email_received":email,
    "ps":ps,
    "em":em,
    }
    return render(request , "otp.html" , context)        
           
            
def restricted_page(request):
    return render(request , "restricted_page.html")
def actual(request):
    total = request.session['total']
    
    if "number" in request.session:
        number = request.session['number']
        r = request.POST
        user_Id = "user"+"_kjhub_"+str(random.randint(10000,999000))
        if not user_model.objects.filter(token = user_Id).exists():
            to_save = user_model(email = total[0] , name = total[1] , password = total[2] , token = user_Id)
            to_save.save()
            request.session["user_number"] = user_Id
            data = {
           'yes':'True',
            }
            return redirect("homepage")
        else:
            actual(request , otp)
    else:
        return error_display(request)
    
    
def user_page(request):
    businesses_searched = []
    category_searched= []
    sub_category_searched = []
    item_name_searched = []
    time_searched = []
    if "user_number" in request.session:
        user = user_model.objects.get(token = request.session["user_number"])
        entered_businesses = sites_visited(request)
        total_visited = len(entered_businesses)
        views , ms = msi(request)
        cat_array = category_seperator(request)
        to_send_cat = cat_array[:3]
        ttv = 0
        
        for i in to_send_cat:
            ttv+=i[1]
        ttvr = views-ttv    
        to_send_cat.append(("others" , ttvr))
        x_values_pie , y_values_pie = [] , []
        
        for cat , views in to_send_cat:
            
            x_values_pie.append(cat)
            y_values_pie.append(views)
        history_data = history.objects.filter(user = user)
        history_searched = history.objects.filter(user=user).order_by("-time")
        #for business 
        comments_p = comments.objects.filter(user = user).order_by("-datetime")
        ratings_p = ratings.objects.filter(user = user).order_by("-datetime")
        for i in history_data:
            businesses_searched.append(i.business.name)
            category_searched.append(i.category)
            sub_category_searched.append(i.subcategory)
            item_name_searched.append(i.item_name)
            time_value = i.time.hour 
            time_searched.append(time_value)
        views_get = [(1,0)]    
        try:
            
            views_recorded = views_recorder.objects.get(user = user)
            views_get = views_recorded.get_data()
        except:
            views_get = [(1,0)]  
            to_save = views_recorder(user = user)
            to_save.save()
            data5 = views_recorder.objects.get(user = user)
            save_data = [(1,100)]
            data5.set_data(save_data)
        trending = product_models.objects.all().order_by("-views")
        
        context = {
        "user":user,
        "cat_graph":to_send_cat,
        "tv":total_visited,
        "views":abs(views),
        #"x_values_pie":x_values_pie,
        "x_values_pie":["hello","hi","how","are"],
        "y_values_pie":y_values_pie,
        "ms":ms,
        "history_searched":history_searched[:5],
        "tn":trending[:5],
        "bs":businesses_searched,
        "cs":category_searched,
        "scs":sub_category_searched,
        "ins":item_name_searched,
        "ts":time_searched,
        "comments":comments_p,
        "rating":ratings_p , 
        "views_get":views_get,
        }
        return render(request,"user_page.html" , context)
    else:
        return restricted_page(request)
    
def thousands_to_k(value):
    try:
        value = int(value)
        if value >= 1000:
            return str(round(value / 1000, 1)) + 'k'
        else:
            return str(value)
    except (ValueError, TypeError):
        return value

def homepage(request):
    category_db = primary_subcategory.objects.all()
    category = []
    category_count = 0
    season = [("Fans/AC","Sunscreen","Hydration water bottle","Picnics","Swimming","Sunglasses","Umbrella"),("woolensweater","Thermocoats","Gloves","Heater","Chiya/coffee","Lipbalm/moisturing cream"),("Umbrella" , "Raincoat" , "Dry Rack","Portable powerbank","Water proof outwears" , "Plastic holder")]
    seasons = season[1]
    best_rated=product_models.objects.all().order_by("-ratings_prod")[:4]
    most_viewed_products = product_models.objects.all().order_by("-views")[:4]
    ppr = product_models.objects.filter(category = "Games and Sports")
    food_db = product_models.objects.filter(category = "food").order_by("-views")
    if "business_token" in request.session:
        request.session["b/u"] = 1
    for i in category_db:
        category.append(i.name)
        category_count +=1
    request.session["category_count"] = category_count
    request.session["category"] = category
    if "user_number" not in request.session:
        
        if "b/u" in request.session:
            business = business_model.objects.get(token = request.session["business_token"])
            context = {
        "logged":1,
        "bu":1,
        "business":business,
        "seasons":seasons,
        "best_rated":best_rated,
        "mvp":most_viewed_products,
        "ppr":ppr,
        
        }
            return render(request , "homepage2.html" , context)
        else:
            context = {
        "logged":0,
        "seasons":seasons,
        "best_rated":best_rated,
        "mvp":most_viewed_products,
        "ppr":ppr,
        
        }
            return render(request, "homepage2.html",context)
    else:
        user = user_model.objects.get(token = request.session['user_number'])
        datas2 = product_models.objects.all()  
        request.session["latitude"] , request.session["longitude"] = user.latitude , user.longitude 
        if views_recorder.objects.all().count()==0:
            to_save = views_recorder.objects.create(user = user)
            meta_data = [("Electronics",(("high",100),("affordable",200)))]
            to_save.set_data(meta_data)
            to_save.save()


        context = {
            "logged":1,
            'user': request.session['user_number'],
            'people':user,
            'data2':datas2,
            "seasons":seasons,
            "best_rated":best_rated,
            "ppr":ppr,
        "mvp":most_viewed_products,
        }
        return render(request , 'homepage2.html' , context)
def maps(request , mode):#loggged and located = 2 , logged = 1 ,unlogged = 0
    if "user_number" in request.session:
        context = {
        "logged":1,
        "mode":int(mode),
        "user":user_model.objects.get(token = request.session["user_number"]),
        }
    else:
        context = {
        "logged":0,
        "mode":int(mode),
        "user":"none0",
        
        }
    return render(request , "maps.html" , context)

def search_results(request,query_string):
    sorted_cat = searcher(request,query_string)
    return sorted_cat
def auto_update():
        now = datetime.now()
        hour = now.hour
        if hour == 0:
            for model in business_model.objects.all():
                model.monthly_views += model.today_views
                model.today_views = 0
                model.save()
schedule.every().hour.do(auto_update)


    
def bookmark(request):
    r = request.POST
    user = request.session.get('user_number') 
    product = r.get("product") 
    i = r.get("i")
    j = int(i)
    real_product = products.objects.get(product_Id = product)
    user_get = people.objects.get(user_number = user)
    if not bookmarks.objects.filter(user = user_get , product = real_product).exists():

        if j == 0:
            user_get.book += 1 
      
            uses = bookmarks( user = user_get , user_number = user , product = real_product)
            user_get.save()  
            uses.save() 
        else:   
            user_get.book -= 1 
      
            uses = bookmarks.objects.get(user = user_get , product = real_product)
            user_get.save()
            uses.delete() 
    else:
        bookmarks.objects.filter(user = user_get , product = real_product).delete()
    
    return JsonResponse({'response':"done",} , safe = False)   
def binary_search(array_given , number):
    len1 = len(array_given)
    front , back = 0,len1-1
    while front<= back:
        mid = (front+back)//2 
        term = array_given[mid]
        if term == number:
            return 1 
        elif term<number:
            front = mid +1
        else:
            back = mid-1
    return -1
def adminpanel(request):
    return render(request , "adminpanel.html" , context)
    
def revisited(business_id , user_id , product_id):
    data1 = business_trackrecord.objects.filter(business = business_id)
    array1 = []
    for i in data1:
        array1.append(int(i[:-5]))
    array1.sort()
    num = user_id[:-5]
    inp = binary_search(array1 , num)
    if inp==1:
        print("found")
    else:
        tosave = business_trackrecord(product = product_id , business = business_id , user = user_id)
        tosave.save()
def euclidean_distance(x_cor , y_cor , x ,y):
    distance = sqrt((int(x_cor) - x)**2 + (int(y_cor) -y)**2)
    return distance 
def closest_business(request):
    db_busy = business_model.objects.all()
    options = []
    category = []
    for i in db_busy:
        x_cor = i.latitude 
        y_cor = i.longitude
        x = request.session["latitude"]
        y = request.session["longitude"]
        distance = euclidean_distance(x_cor , y_cor , x,y)
        options.append((i.token , distance , i.category))
    sorted_options = sorted(options , key = lambda x:x[1] , reverse = False)    
    options = []
    for j in sorted_options:
        if j[2] not in category:
            category.append(j[2])
    for k in category:
        real_options = []
        count = 0
        for l in sorted_options:
            if count <= 10:# change this count to give that no of outputs for each cateogry
                if k == l[2]:
                    count +=1
                    real_options.append((l[0] , l[1]))
            else:
                break
        options.append((k , real_options))
        real_options = []
    return options
def show_me_best(request):
    options = closest_business(request) 
    category = []
    business = []
    for i in options:
        if i[0] not in category:
            category.append(i[0])
    for k in category:
        cat = []
        for j in options:
            if j[0]==k:
               
                
                #for (token,distance) in j[1]:
                for l in  j[1]:   
                    token = l[0]
                    db = business_model.objects.get(token = token)
                    ratings = db.avg_rating
                    cat.append((token , ratings))
        cat_sorted = sorted(cat , key = lambda x:x[1] , reverse = False)            
        business.append((k , cat_sorted))
        cat_sorted = []
    return options   
def set_mva(request):
    category = request.session["category"]
    for i in category:
        business_db = business_model.objects.get(category = category)
        for j in business_db:
            lad = j.get_list()#listed_area_data 
            sorted_lad = sorted(lad , key = lambda x:x[1] , reverse = True)
            j.set_mva_list = sorted_lad[:2]#area,views
            j.save()    
def area_filler(request):
    category = request.session["category"]

    table_made = area_data()
    areas = [1,2,3,4,5,6,7]
    for i in category:
        business_db = business_model.objects.get(category = category)
        false_list = []
        for j in business_db:
            mva_listed = j.get_mva_list()
            token = j.token
            for k in mva_listed:
                false_list.append((token , k[0],k[1]))#token , area , views
        for j in areas:
            second_false = []
            for k in false_list:
                if j == k[1]:
                    second_false.append((token , k[2]))#token , views
            sorted_sf = sorted(second_false , key = lambda x:x[1] , reverse = True)
            to_save = area_data.objects.get(area = j)
            to_save.get_tokenized(sorted_sf[:2])
            to_save.save()
                    
def sites_visited(request):
    data1 = history.objects.filter(user = request.session["user_number"])
    businesses = []
    for i in data1:
        if i.business not in businesses:
            businesses.append(i.business)
    return businesses      
def msi(request):
    if "user_number" in request.session:
        views = history.objects.filter(user = request.session["user_number"]).count()
        data2 = history.objects.filter(user = request.session["user_number"])
        searched_items = []
        for i in data2:
            found = False
            for index, (item, views) in enumerate(searched_items):
                if i.item_name == item:
                    searched_items[index] = (item, views + 1)
                    found = True
                    break
            if not found:
                searched_items.append((i.item_name, 1))

        sorted_si = sorted(searched_items, key=lambda x: x[1], reverse=True)
        return views , sorted_si[:2]
    else:
        return 0 , [("None" , 0)]
def category_seperator(request):
    data1 = history.objects.filter(user = request.session["user_number"])
    count_array = []
    count = 0
    category = request.session["category"]
    
    for i in category:
        for j in data1:
            if j.category == i:
                count+=1
        count_array.append((i,count))
        count = 0
    corr_ca = sorted(count_array , key = lambda x:x[1] , reverse = True)
    return corr_ca    
def views_adder(request , business , *args):
    
    business_token = business 
    product_token = args
    if user_number in request.session:
        user_id = request.session["user_number"]
        if product_token:
            product_data = product_models.objects.get(token = product_token)
            product_data.views+=1
            
            hist = history(user = user_id , business = business_token , category = product_data.category , subcategory = product_data.subcategory , item_name = product_data.product_name , product = product_token)
            hist.save()
            product_data.save()
        user_data = user_model.objects.get(token = user_id)
        try:
        # Try to get the existing record
            data1 = views_recorder.objects.get(user=user_id)
        except ViewsRecorder.DoesNotExist:
        
            data1 = views_recorder(user_id=user_id)
            data1.set_data([(1, 1)])
            data1.save()
        else:
        # If it exists, update the data
            some_data = data1.get_data()
            if some_data:
                some_data[-1][1] += 1  
            else:
                some_data = [(1, 1)] 
        
        area_got = user_data.area_code
        business_data = business_model.objects.get(token = business_token)
        data2 = business_data.get_list()#(area,views)
        data3 = []
        for (area,views) in data2:
            if area == area_got:
                views+=1
            data3.append((area,views))
        business_data.set_list(data3)
        business_data.today_views +=1
        business_data.monthly_views+=1
        business_data.save()
        user_data.views+=1
        user_data.save()
    else:
        business_data = business_model.objects.get(token = business_token)
        business_data.today_views +=1
        business_data.monthly_views+=1
        business_data.save()
        if product_token:
            product_data = product_models.objects.get(token = product_token)
            product_data.views+=1
            hist = history(user = user_id , business = business_token , category = product_data.category , subcategory = product_data.subcategory , item_name = product_data.product_name , product = product_token)
            hist.save()      
            product_data.save()    
        else:   
            hist = history(user = "not_logged" , business = business_token , category = "none" , subcategory = "none" , item_name = "none" , product = "none")
            hist.save()

            

def space_remover(cat):
    result = ""
    capitalize_next = False
    
    for char in cat:
        if char == " ":
            capitalize_next = True
        else:
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char
    return result
def top_picks(request, id):
    dat_cat_name = {}
    dat_cat_name[0] = "All"
    data_cat = []  # Initialize data_cat outside the loop
    
    if "user_number" in request.session:
        user_data = user_model.objects.get(token=request.session["user_number"])
        category_count = request.session["category_count"]
        
        if user_data.latitude == 0 or user_data.longitude == 0:
            not_added_address = 1
        else:
            not_added_address = 0
            businesses = show_me_best(request)
            
            for cat, arr in businesses:
                dat_cat_name[category_count + 1] = space_remover(cat)
                cate = space_remover(cat)
                
                if id == cate or id == "All":
                    for tok, rat in arr:
                        data_cat += business_model.objects.filter(token=tok)
                    category_count += 1  
                else:
                    category_count += 1  
                    
        context = {
            "user": user_data,
            "current": id,
            "address": not_added_address, 
            "dat_cat_name": dat_cat_name,
            "data_cat": data_cat,
            "count": category_count,
        }
        
        return render(request, "top_picks.html", context)
    else:
        return error_display(request)

def error_display(request):
 
    return render(request , "restricted_page.html")
def address_adder(request , mode):

    
        
    context = {
        "mode":mode,
        "user":user_model.objects.get(token = request.session["user_number"]),
        }
    
    return render(request,"maps.html" , context)
def address_adder_views(request):
    if request.method == "POST":
        user = user_model.objects.get(token = request.session["user_number"])
        r = request.POST 
        lat = r.get("lat")
        longi = r.get("longi")
        zone = r.get("zone")
        user.latitude = lat 
        user.longitude = longi 
        user.area_code = zone 
        user.save()
        data = {
        "done":1,
        }
        return JsonResponse(data , safe = False)
def login(request):
    r = request.POST 
    if request.method == "POST":
        
        username = r.get("username")
        password = r.get("password")
        if user_model.objects.filter(name = username , password = password).exists():
            g = user_model.objects.get(name = username , password = password)
            request.session["user_number"] = g.token
            
            return homepage(request)
        elif business_model.objects.filter(token = username , password = password):
            
            request.session["business_token"] = username
            request.session["bu"] = 1
            return business_page(request,username)
    return render(request , "login.html")        
def business_page(request,token):
    
    if "business_token" in request.session:
        token = request.session["business_token"]
        prod_busi = business_model.objects.get(token = token)
        products = product_models.objects.filter(business_mdl = prod_busi)
        cmts = comments.objects.filter(business = prod_busi)
        leng = len(products)
        leng_cmts = len(cmts)
        context = {
        "business":business_model.objects.get(token = token),
        "b":1,
        "products":products,
        "l":leng,
        "cl":leng_cmts,
        }
        return render(request,"business_page.html",context)
    elif business_model.objects.filter(token=token):
        prod_busi = business_model.objects.get(token = token)
        products = product_models.objects.filter(business_mdl = prod_busi)
        leng = len(products)
        cmts = comments.objects.filter(business = prod_busi)
        leng_cmts = len(cmts)
        context = {
        "cl":leng_cmts,
        "business":business_model.objects.get(token = token),
        "products":products,
        "l":leng,
        }
        return render(request,"business_page.html",context)
    else:
        return error_display(request)
def add_real_product(request):
    r = request.POST
    if request.method == "POST":
        cate = r.get("category")
        sub_cate = r.get("sub_cate")
        show = r.get("show")
        category = primary_subcategory.objects.get(name = cate)
        if secondary_subcategory.objects.filter(ss_forekey = category.name).exists() or sub_cate == "none":
            show = 0
        else:
            show = 1
        if show==0:
            sub_cate1_json = []
            category = primary_subcategory.objects.get(name = cate)
            sub_cate1 = secondary_subcategory.objects.filter(ss_forekey=category.name)
            print(f"subcate is {sub_cate1}")
             
            for i in sub_cate1:
                sub_cate1_json.append(i.sub_name)
    
    # Construct the response data
            data = {
            "category":category.name,
        "sub_cate": sub_cate1_json,
        "show": 1,
        
            }   
            return JsonResponse(data , safe = False)
        else:
            item_names_ser = []
            category = primary_subcategory.objects.get(name = cate)
            print(f"cate is {category}")
            item_names = last_category.objects.filter(lc_forekey = category.name)
            for i in item_names:
                item_names_ser.append(i.item_name)
            
            sub = "ola"
            print(item_names_ser)
            data = {
            "item_names":item_names_ser,
            "show":0,
            "sub_cate":sub,
            }
            return JsonResponse(data , safe = False)
            
    else:
        return error_display(request)
def add_product(request , token):
    r = request.POST
    business = business_model.objects.get(token = token)
    category1 = []
    for i in primary_subcategory.objects.all():
        category1.append(i)
    
    context = {
    "business":business,
    "category1":category1,
    }
    
    
    return render(request,"add_product.html" , context)
def category_saver(request):
    r = request.POST
    done = 0
    if request.method == "POST":
        category = r.get("category_name")
        subcategory = r.get("sub_category")
        item_name = r.get("item_name")
        token = r.get("token")
        obj1 = primary_subcategory(name = category)
        obj1.save()
        obj1 = primary_subcategory.objects.get(name = category)
        if subcategory != "none":
            obj2 = secondary_subcategory(ss_forekey = obj1 , sub_name = subcategory)
            obj2.save()
            obj2 = secondary_subcategory.objects.get(sub_name = subcategory)
            
            obj3 = last_category(lc_forekey = subcategory , item_name = item_name)
            obj3.save()
        else:
            obj3 = last_category(lc_forekey = category , item_name = item_name)
            obj3.save()
        done = 1    
    context = {
    "done":done,
    
    }
    return render(request , "category_saver.html" , category)

def item_name_giver(request , name):
    db1 = primary_subcategory.objects.get(name = name)
    return_array = []
    if secondary_subcategory.objects.filter(ss_forekey = db1).exists():
        db2 = secondary_subcategory.objects.filter(ss_forekey = db1)
        for i in db2:
            db3 = last_category.objects.get(lc_forekey = i.sub_name)
            
            return_array.append(db3.item_name)
    else:
        db3 = last_category.objects.filter(lc_forekey = name)
        for k in db3:
        
            return_array.append(k.item_name)
    return return_array    
            
def history_page(request):
    if "user_number" in request.session:
        user = request.session["user_number"]
        history_pages = history.objects.filter(user = user)
        user_id = user_model.objects.get(token = user)
        context = {
        "user":user,
        "user_id":user_id,
        "histories":history_pages,
        
        }
        return render(request,"Myhistory.html" , context)
    else:
        return error_display(request)
def remove_bookmark(request , id):
    if "user_number" in request.session:
        id = request.POST.get("id")
        product_id = product_models.objects.get(token = id)
        user = user_model.objects.get(token = request.session["user_number"])
        get_book = bookmarked.objects.filter(product = product_id , user = user).delete()
        return homepage(request)
    else:
        return error_display(request)
def add_bookmark(request , id):
    if "user_number" in request.session:
        id = request.POST.get("id")
        product_id = product_models.objects.get(token = id)
        user = user_model.objects.get(token = request.session["user_number"])
        get_book = bookmarked.objects.create(product = product_id , user = user)
    else:
        return error_display(request)
def bookmarks(request):
    if "user_number" in request.session:
        user = request.session["user_number"]
        bookmarks = bookmarked.objects.filter(user = user)
        context = {
        "bookmarked":bookmarks,
        "logged":1,
        "user":user,
        }
        return render(request,"mybookmarks.html" , context)
    else:
        return error_display(request)
def logout(request):
    request.session.flush()
    return redirect("homepage")
def most_active(request , area):
    most_activated = user_model.objects.all().order_by("views")
    most_activated_actual = most_activated[:10]
    area_wise = []
    if area!=0:
        area_code = "zone_" + area
        area_wise_re = user_model.objects.filter(area_code = area_code).order_by("views")
        area_wise = area_wise_re[:5]
    return most_activated_actual , area_wise 
def highest_ranker(query):
    returner = []
    if query=="very_high":
        returner = ["very_high" , "high"]
    elif query=="high":
        returner =["high" , "medium"]
    elif query=="medium":
        returner =["medium" , "affordable"] 
    elif query=="affordable":
        returner =["medium" , "affordable"] 
    return returner  
def recommendations(request , category):
    if "user_number" in request.session:
        user = user_model.objects.get(token = request.session["user_number"])
        if category != "All":    
            cate = primary_subcategory.objects.all()
        
            data4 = recommended_ones(request,category)
            context = {
            "data4":data4,
            "user":user,
            "cate":cate,
            "category":category,
            }
            return render(request, "recommendations.html",context)
        else:
            cate = primary_subcategory.objects.all()
        
            
            category = "All"
            data4 = recommended_ones(request,category)
            context = {
        "data4":data4,
        "cate":cate,
        "user":user,
        "category":category,
            }
            return render(request, "recommendations.html",context)
    else:
        return error_display(request)
def recommended_ones(request , category):
    try:
        user_id = user_model.objects.get(token = request.session["user_number"])
        user_meta = views_recorder.objects.get(user = user_id)
    except:
        return error_display(request)
    #meta_data = user_meta.get_data()
    meta_data = [["Electronics", [["high", 100], ["affordable", 200]]]]
    if category == "All":
        categories = []
        for i in meta_data:
            highest = ["low" , 0]
            for (price , views) in i[1]:
                if views >= highest[1]:
                    highest = [price , views]
                else:
                    continue
            highest_giver = highest_ranker(highest[0])
            int1 = random.randint(0,1)
            categories.append((i[0] , highest_giver[int1]))
        print(categories)
        data4 = []              
                    
        for _ in range(7):
            int2 = random.randint(0, len(categories) - 1)
            category_name, price_range = categories[int2]
    
    
            filtered_data = product_models.objects.filter(
                category=category_name, 
                price_range=price_range,
                
            )
    
    
            data4.extend(list(filtered_data))    
            #print(data4)
        data4 = product_models.objects.all()    
        return data4 
    else:
        print(category)
        for i in meta_data:
            if i[0]==category:
                print("here")
                data4  = []
                for (price ,views) in i[1]:
                    filtered_data = product_models.objects.filter(category = category)
                    data4.extend(list(filtered_data))
                return data4 
            else:
                data4  = []
                for (price ,views) in i[1]:
                    filtered_data = product_models.objects.filter(category = category)
                    data4.extend(list(filtered_data))
                return data4 
def searchbar(request):
    data = "empty"
    list_made = word_list_giver(request)
   
    business_id = []
    product_id = []
    if "user_number" in request.session:
        user = user_model.objects.get(token = request.session["user_number"])
        logged = 1
    elif "business_token" in request.session:
        user = business_model.objects.get(token = request.session["business_token"])
        logged =1
    else:
        logged = 0
        user = ""
    if request.method == "POST":
        r = request.POST
        query_set = r.get("query_string")
        
        data = string_taker(query_set , list_made)
        print(f"data is {data}")
        #business_id ,  product_id = sentence_seperator(data , list_made)
        for i in data:
            business_ids =  business_tracker(i)
            business_id.append(business_ids)
            product_ids = prod_tracker(i)
            product_id.append(product_ids)
        #data = search_results(request,query_set) 
        #data = temporary_search_results(query_set)
        print(f"business_ids is {business_id}")
        print(f"product_id is {product_id}")
        business_idu=[]
        product_idu = []
        for j in business_id:
            try:
                businessed = business_model.objects.get(token=j)
                busi_prod = product_models.objects.filter(business_mdl = businessed).count()
                
                listed_busid = [businessed.token , businessed.name , businessed.avg_rating , businessed.img.url ,businessed.category , businessed.dob,busi_prod]
                if not any(businessed.token == listed_busi[0] for listed_busi in business_id):
                    business_idu.append(listed_busid)
            except business_model.DoesNotExist:
                pass
        for k in product_id:
            try:
                producted = product_models.objects.get(token = k)
                listed_prod = [producted.token , producted.product_name , producted.views , producted.picture.url , producted.category , producted.ratings_prod , producted.price , producted.business_mdl.name]
                if not any(producted.token == product[0] for product in product_id):
                    product_idu.append(listed_prod)
            except product_models.DoesNotExist:
                pass
        data1 = {
            "prod":product_idu, 
            "busi":business_idu,

            }
        print(product_id)    
        return JsonResponse(data1,safe = False)
        
        
    context = {
    "user":user , 
    "logged":logged,
        "data":data,
        "list":list_made,
        }
    return render(request , "searchbar.html",context)
                
def word_list_giver(request):
    list_made = []
    product_model = product_models.objects.all()
    business_modeled = business_model.objects.all()
    primary_subcategory_m = primary_subcategory.objects.all()
    secondary_subcategory_m = secondary_subcategory.objects.all()
    last_category_m = last_category.objects.all()
    for i in product_model:
        product_na = i.product_name 
        product_n = product_na.split()
        length_of = len(product_n)
        for j in range(length_of):
            list_made.append(product_n[j])
    for i in business_modeled:
        product_na = i.name 
        product_n = product_na.split()
        length_of = len(product_n)
        for j in range(length_of):
            list_made.append(product_n[j])  
    for i in primary_subcategory_m:
        product_na = i.name 
        product_n = product_na.split()
        length_of = len(product_n)
        for j in range(length_of):
            list_made.append(product_n[j])    
    for i in secondary_subcategory_m:
        product_na = i.sub_name
        product_n = product_na.split()
        length_of = len(product_n)
        for j in range(length_of):
            list_made.append(product_n[j])
    for i in last_category_m:
        product_na = i.item_name
        product_n = product_na.split()
        length_of = len(product_n)
        for j in range(length_of):
            list_made.append(product_n[j])   
                
    return list_made       
def most_milne_2(word , word_list):
    word_length = len(word)
    word = word.lower()
    total =0
    data1 = []
    for i in word_list:
        i = i.lower()
        for j in range(word_length):
            if 0 <= j-1 < len(i) and 0 <= j-1 < len(word):
                if i[j-1]==word[j-1]:
                    total +=1
        percentage = int((total/word_length)*100)
        data1.append((i , percentage))
        if percentage == 100:
            break 
        percentage = 0
        total = 0 
    sorted_list = sorted(data1, key=lambda x: x[1], reverse=True) 
    

    return sorted_list[0]     
            
def string_taker(query_string , list_made):
    words = []
    if " " not in query_string:
        words.append(query_string)
    else:    
        words = query_string.split()
      
    word = []
    sentence = []
    for i in words:
        length_i = len(i)   
        word = most_milne_2(i , list_made)
        sentence.append(word)
           
    real_sentence = [] 
    for (word , value) in sentence:
        real_sentence.append(word)
    return real_sentence    
def sentence_to_tracker(sentence, list_maker):
    lds = len(sentence)
    print("lds is")
    print(lds)
    print(sentence)
    
   
    lm_len = len(list_maker)
    try:
        n = int(lm_len/lds) + 1  
    except ZeroDivisionError:
        n = int(lm_len/3)+1
    gotit = 0
    for j in range(lm_len - lds + 1):
        start_idx = j
        end_idx = start_idx + lds
        if list_maker[start_idx:end_idx] == sentence:
            gotit = 1
            break  
    
    return gotit
'''def sentence_seperator(sentence , list_maker):
    business_token = []
    product_token = []
    leng = len(sentence)
    
    if leng >4:
        for i in range(1,4):
            iterations = leng-i
            for j in range(0,iterations):
                stri = sentence[j:i+j-1]
                gotit = sentence_to_tracker(stri, list_maker)
               
                if gotit == 1:
                    joined = " ".join(stri)
                    try:
                        busi = business_model.objects.get(name = joined)
                        business_token.append(busi.token)
                    except business_model.DoesNotExist:
                        try:
                            prod = product_models.objects.get(product_name = joined)
                            product_token.append(prod.token)
                        except product_models.DoesNotExist:
                            pass
                    pass
    else:
        for i in range(0,leng):
            joined = ""
            stri = []
            if i==0:
                
                for j in range(0,leng):
                    stri = sentence[j]
            else:        
               
                iterations = leng-i
                for j in range(0,iterations):
                    stri = sentence[j:i+j-1]
            gotit = sentence_to_tracker(stri, list_maker)
           
            
            if gotit == 1:
                joined = " ".join(stri)
               
                
                try:
                    busi = business_model.objects.get(name = joined)
                    business_token.append(busi.token)
                except business_model.DoesNotExist:
                    try:
                        prod = product_models.objects.get(product_name = joined)
                        product_token.append(prod.token)
                    except product_models.DoesNotExist:
                        pass
                    pass
                    
    return business_token , product_token       '''     
def business_tracker(word):
    names = business_model.objects.values_list("name" , flat = True)
    business_var  = ""
    
    for j in names:
       
        
        
        j = j.lower()
       
        if word in j:
            
            try:
                businessed = business_model.objects.get(name = j)
                business_var = businessed.token
            except business_model.DoesNotExist:    
                pass
            pass    
    return business_var         
def prod_tracker(word):
    names = product_models.objects.values_list("product_name" , flat = True)
    business_var = ""
    for j in names:
        j = j.lower()
        
        if word in j:
            
            try:
                businessed = product_models.objects.get(product_name = j)
                business_var = businessed.token
            except business_model.DoesNotExist:    
                pass
            pass
    return business_var        
def ci(request):
    user = user_model.objects.get(token = request.session["user_number"])
    if request.method=="POST":
        r = request.POST
        password = r.get("password")
        name = r.get("username")
        email = r.get("email")
        real_email = user.email 
        real_password = user.password 
        real_name = user.name
        if name!=real_name and password == real_password:
            print(12)
            user.name = name
            user.save()
            return JsonResponse({"redirect":1} , safe = False)
        elif email!=real_email and password == real_password:
            print(13)
            request.session["new_email"] = email 
            number = random.randint(4567 , 9999)
            request.session["number"] = number 
            extra_var = "none"
            Email(request , email , extra_var)
            return JsonResponse({"email":email} , safe = False)
            
        elif password != real_password:
            print(23)
            request.session["new_password"] = password 
            number = random.randint(4567 , 9999)
            request.session["number"] = number 
            extra_var = "none"
            Email(request , email , extra_var)
            return JsonResponse({"email":email} , safe = False)
        else:
            return JsonResponse({"redirect":1} , safe = False)
    else:
        return homepage(request)
def change_info(request):
    if "user_number" in request.session:
        user = user_model.objects.get(token = request.session["user_number"])
        context = {
        "user":user,
        
        
        }
        return render(request , "change_info.html" ,context)
    else:
        return error_display(request)    
def change_email_password(request):
    user = user_model.objects.get(token = request.session["user_number"])
    
    if "new_email" in request.session:
        user.email = request.session["new_email"]
        request.session.pop("new_email" , None)
        user.save()
        return user_page(request)
    elif "new_password" in request.session:
        user.password = request.session["new_password"]
        user.save()
        request.session.pop("new_password" , None)
        return user_page(request)
    else:
        return error_display(request)
        
def product_list(request):
    if "business_token" in request.session:
        business_got = business_model.objects.get(token = request.session["business_token"])
        products = product_models.objects.filter(business_mdl = business_got)
        context = {
        "prods":products,
        "business":business_got,
        
        
        }
        return render(request, "product_list.html" ,context)
    else:
        return error_display(request)
        
        
def comments_page(request):
    if "business_token" in request.session:
        business_got = business_model.objects.get(token=request.session["business_token"])
        products = product_models.objects.filter(business_mdl=business_got)
        
        cmts = []
        rated = []
        
        for product in products:
            rate = ratings.objects.filter(product_id=product)
            for i in rate:
                rated.append((product.product_name , (i.user.name ,i.ratings)) )
            cmted = comments.objects.filter(product_id=product)
            for i in cmted:
                cmts.append((product.product_name , (i.user.name , i.comment)))

        context = {
            "cmts": cmts,
            "rated": rated,
        }
        return render(request, "comments.html" ,context)
    else:
        error_display(request)
def promo_discount(request):
    return render(request, "promo.html" ,context = {})    
def variant_finder(id):
    product = product_models.objects.get(token = id)
    category,sub_category = product.category , product.sub_category
    producted = product_models.objects.filter(category = category , sub_category = sub_category).order_by("-views")
    return producted[:2]
def rpf(id):
    product = product_models.objects.get(token = id)
    category,sub_category = product.category , product.sub_category 
    products = product_models.objects.filter(category = category)
    return products[:6]
def product_page(request, id):
    if product_models.objects.filter(token = id).exists():
        
        prod = product_models.objects.get(token = id)
        variants = variant_finder(id)
        cmted = -1
        prod.views +=1
        comment = comments.objects.filter(product_id = prod)
        related_product_finders = rpf(id)
        if "user_number" in request.session:
            user = user_model.objects.get(token = request.session["user_number"])
            
            cmted = 0
            try:
                if comments.objects.filter(user = user , product_id = prod):
                    cmted = 0
            except comments.DoesNotExist:
                cmted = 1
            
        
            
            
            context = {
                "user":user , 
                "rpf":related_product_finders,
                "variants":variants,
                "prod":prod,
                "logged":1,
                "comments":comment,
                "cmted":cmted,
                
                }
        else:
            context = {
            
            "cmted":cmted,
            "comments":comment,
            "logged":0,
            "rpf":related_product_finders,
                "variants":variants,
            "prod":prod,
            
            
            }
        return render(request , "product.html" , context)
    else:
        return error_display(request)
def edit_busi_prod(request, id):
    return homepage(request)
def delete_busi_prod(request , id):
    if "business_token" in request.session:
        busine = product_models.objects.get(token = id)
        busine.delete()
        token = request.session["business_token"]
        return business_page(request,token)
      
    else:
        return error_display(request)
def rated(request , id):
    if "user_number" in request.session:
        r = request.POST 
        star = r.get("stars")
        cmt = r.get("comments")
        user = user_model.objects.get(token = request.session["user_number"])
        
        product = product_models.objects.get(token = id)
        busi = product.business_mdl
        ratings.objects.create(user = user , product_id = product , ratings = star)
        cmt_token =product.token[6:10]+user.token[1:3]+random.randint(4000000,80000000) 
        if cmt != "":
            comments.objects.create(comment_token =cmt_token ,user = user , product_id = product_id , comment = cmt , business = busi)
            
            