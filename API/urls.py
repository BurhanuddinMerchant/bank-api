from django.urls import include, path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r"banks", BankViewSet)
# router.register(r"branches/autocomplete", BankFilteredView)
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", include("rest_framework.urls")),
    path("branches/autocomplete", BankFilteredAutocompleteView.as_view()),
    path("branches", BankFilteredSearchView.as_view()),
]
