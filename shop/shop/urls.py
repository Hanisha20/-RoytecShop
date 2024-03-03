from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls', namespace = 'homeApp')),
    # path('accounts/', include('accounts.urls' , namespace = 'accountsApp')),
    # path('payments/', include('payments.urls', namespace = 'paymentsApp')),
    # path('products/', include('products.urls', namespace = 'productsApp')),
    path('admin/', admin.site.urls),
]
