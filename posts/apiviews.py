from .models import Homepage, Sermon, Ministers, PhotoGallery, UpcomingEvents
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from rest_framework import permissions




######################### 1 ###########################
class HomepageListCreateAPIView(ListCreateAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class HomepageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    


##################################### 2 ###########################
class SermonListCreateAPIView(ListCreateAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class SermonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

################################## 3 ##############################
class MinistersListCreateAPIView(ListCreateAPIView):
    queryset = Ministers.objects.all()
    serializer_class = MinistersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class MinistersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ministers.objects.all()
    serializer_class = Ministers.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


############################# 4 ##############################
class PhotoGalleryListCreateAPIView(ListCreateAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class PhotoGalleryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


############################### 5 ###############################
class UpcomingEventsListCreateAPIView(ListCreateAPIView):
    queryset = UpcomingEvents.objects.all()
    serializer_class = UpcomingEventsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class UpcomingEventsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UpcomingEvents.objects.all()
    serializer_class = UpcomingEventsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)