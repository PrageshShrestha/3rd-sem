from django.contrib import admin 
from django.urls import path , include 
from . import views
from django.conf import settings



urlpatterns = [
   path("Homepage" , views.homepage , name = "homepage"),
   path("test" , views.test ,name = "test"),
   path("signup" , views.signup , name="signup"),
   path("otp/<str:email_receiver>" , views.otp , name="otp"),
   path("adminpanel" , views.adminpanel , name = "adminpanel"),
   path("actual" , views.actual , name = "actual"),
   path("maps/<str:mode>",views.maps,name="maps"),
   path("user_page" , views.user_page , name = "user_page"),
   path("searchbar" , views.searchbar , name ="searchbar"),
   path("top_picks/<str:id>" , views.top_picks , name = "top_picks"),
   path("error" , views.error_display , name = "error_display"),
   path("save_address",views.address_adder_views , name = "save_address"),
   path("business_profile/<str:token>" , views.business_page, name="business_profile"),
   path("login" , views.login , name = "login"),
   path("category_saver" , views.category_saver , name = "category_saver"),
   path("add_product/<str:token>" , views.add_product , name = "add_product"),
   path("Myhistory" , views.history_page , name="Myhistory"),
   path("Mybookmarks",views.bookmarks , name = "Mybookmarks"),
   path("add_real_product" , views.add_real_product , name = "add_real_product"),
   path("logout" , views.logout , name = "logout"),
   path("recommendations/<str:category>",views.recommendations ,name = "recommendations"),
   path("change_info" , views.change_info , name="change_info"),
   path("ci" , views.ci , name="ci"),
   path("cep" , views.change_email_password , name="cep"),
   path("product_list" , views.product_list , name="product_list"),
   path("comments" , views.comments_page , name = "comments"),
   path("promo" , views.promo_discount , name="promo"),
   path("product/<str:id>" , views.product_page , name="product"),
]