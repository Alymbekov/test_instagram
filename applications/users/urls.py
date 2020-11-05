from django.urls import path, re_path

from applications.users.views import (
    get_user, search_users,
    search, add_person
)

app_name = "users"

urlpatterns = [
    path('user/<int:user_id>/', get_user, name='user_profile'),
    path('search/', search_users, name='search_users'),
    path('new-search/', search, name='new_search'),
    path('test-model-form/', add_person, name='test_model_form'),
    # re_path(r'')
    #http://localhost:8000/users/user/1/
]

# str
# int
# slug --> makers-bootcamp
# uuid - 0545313423-2132asdasdqwe



