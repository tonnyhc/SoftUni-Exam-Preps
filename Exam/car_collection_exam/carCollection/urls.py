from django.urls import path, include

from car_collection_exam.carCollection.views import index, create_profile, details_profile, edit_profile, delete_profile, catalogue, \
    create_car, details_car, edit_car, delete_car

urlpatterns = [
    path('', index, name='home page'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:pk>/details/', details_car, name='details car'),
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/delete/', delete_car, name='delete_car')
    ]))

]
