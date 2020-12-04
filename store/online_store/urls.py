from django.urls import path
from . import views
from .views import (
    ItemListView,
    ItemDetailView,
    OrderSummaryView,
    CheckoutView,
    PaymentView
)
app_name = 'app'

urlpatterns = [
    path('', ItemListView.as_view(), name='home'),
    path('products/<slug>/',views.ItemDetailView.as_view(),name="item-detail"),
    path('checkout/',views.CheckoutView.as_view(),name="checkout"),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
]