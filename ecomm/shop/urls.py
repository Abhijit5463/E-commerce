from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.index, name="ShopHome"),
   
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("checkout/", views.checkout, name="Checkout"),
     path('logout/', views.logoutUser, name='logout'),
    
   # path("handlerequest/", views.handlerequest, name="HandleRequest"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





