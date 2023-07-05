from django.urls import path
from .apiviews import *


urlpatterns = [
    ############## 1 #################
    path('', HomepageListCreateAPIView.as_view()),
    path('<int:pk>/', HomepageRetrieveUpdateDestroyAPIView.as_view()),
    ################## 2 ########################
    path('ministers/', MinistersListCreateAPIView.as_view()),
    path('minister/<int:pk>', MinistersRetrieveUpdateDestroyAPIView.as_view()),
    ###################### 3 #######################
    path('sermons/', SermonListCreateAPIView.as_view()),
    path('sermons/int:pk>/', SermonRetrieveUpdateDestroyAPIView.as_view()),
    ############################## 4 ###################### 
    path('gallery/', PhotoGalleryListCreateAPIView.as_view()),
    path('gallery/<int:pk>/', PhotoGalleryRetrieveUpdateDestroyAPIView.as_view()),
    ####################################### 5 ########################
    path('events/',UpcomingEventsListCreateAPIView.as_view()),
    path('events/<int:pk>/',UpcomingEventsRetrieveUpdateDestroyAPIView.as_view()),
]