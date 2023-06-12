from django.urls import path
from . import views
from .views import Reservation_Page
from django.conf import settings
from django.conf.urls.static import static
from .views import ReservationPage, ReservationCreate, ReservationUpdate, ReservationList, ReservationDelete


app_name = 'bike_app'

urlpatterns = [
    # Welcome page before user log in
    path('', views.welcome),

    # Welcome page after user login
    path('welcome/<uuid:url_uuid>', views.welcome_user, name='welcome_user'),  # unique URL

    # Register page
    path('register', views.AccountRegistration.as_view(), name='register'),

    # Login Page
    path('login', views.Login, name='login'),

    # Logout page
    path('logout', views.Logout, name="logout"),

    # Feedback Page
    path('feedback/<uuid:url_uuid>', views.FeedBack_page, name='feedback'),  # unique URL

    # Bike List page
    # path('bike_list/<uuid:url_uuid>', views.bike_list, name='bike_list'),    # unique URL

    # Reservation page
    path('reserve/', Reservation_Page.as_view(), name='reserve'),

    # Bike List Page
    path('bikeList/<uuid:url_uuid>', views.bikeList_page, name='bikeList'),

    # Q&A
    path('FAQ/', views.FAQ, name='FAQ'),

    # Edit Profile
    path('edit_user/<uuid:url_uuid>', views.edit_user, name='edit_user'),

#Reservation Part
    path('reservations/', ReservationList.as_view(), name='reservations'),
    path('reserve/', ReservationCreate.as_view(), name='reserve'),
    path('reservation/<int:pk>/', ReservationPage.as_view(), name='reservation'),
    path('reservation-update/<int:pk>/', ReservationUpdate.as_view(), name='reservation-update'),
    path('reservation-delete/<int:pk>/', ReservationDelete.as_view(), name='reservation-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
