from django.urls import path
from . import views

print("Myapp Urls Called")

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('validate_otp/',views.validate_otp,name='validate_otp'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('new_password/',views.new_password,name='new_password'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
    path('seller_product_detail/<int:pk>/',views.seller_product_detail,name="seller_product_detail"),
    path('user_product_detail/<int:pk>/',views.user_product_detail,name='user_product_detail'),
    path('seller_product_edit/<int:pk>/',views.seller_product_edit,name='seller_product_edit'),
    path('seller_product_delete/<int:pk>/',views.seller_product_delete,name='seller_product_delete'),
    path('user_view_product/<str:cn>/',views.user_view_product,name='user_view_product'),
    path('user_product_detail/<int:pk>/',views.user_product_detail,name='user_product_detail'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('mywishlist/',views.mywishlist,name='mywishlist'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('mycart/',views.mycart,name='mycart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('change_qty/',views.change_qty,name="change_qty"),
    path('pay/',views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
]