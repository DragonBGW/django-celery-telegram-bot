from django.urls import path
from .views import public_view, protected_view
from django.urls import path
from .views import public_view, protected_view, register_user

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
]


urlpatterns = [
    path("public/", public_view),
    path("protected/", protected_view),
    path("register/", register_user),   # ⬅️ new
]
