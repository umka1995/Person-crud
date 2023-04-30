from django.urls import path
from .views import person_all,person_id,person_create,person_update,person_delete

urlpatterns = [
    path('vse_ludi/',person_all),
    path('person_id/<int:pk>/',person_id),
    path('person_create/',person_create),
    path('person_update/<int:pk>/',person_update),
    path('person_delete/<int:pk>/',person_delete)
]