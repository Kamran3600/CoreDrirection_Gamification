from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('fos_user_user/', views.fos_user_user),
    path('gamification_challenge/', views.gamification_challenge_view),
    path('process-challenges/', views.process_and_update_mongo),
    # path('process/',views.challenge_participant_view)
    # Add other URLs as needed
]
