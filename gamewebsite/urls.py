from django.urls import path
from gamewebsite import views

app_name = 'gamewebsite'

urlpatterns = [
    path('', views .game_library, name = 'game_library'),
    path('contact-us/', views.contact_us, name = 'contact_us'),
    path('login/', views.log_in, name = 'log_in'),
    path('my-account/', views.my_account, name = 'my_account'),
    path('my-account/edit/', views.edit_account, name='edit_account'),
    # path('GameLibrary/<slug:game_name_slug>/', views.game_page, name='game_page')
    # path('GameLibrary/<slug:game_name_slug>/search-matches/', views.search_matches, name='search_matches'),
    ]