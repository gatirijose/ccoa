from rest_framework import serializers
from .models import Homepage, Sermon, Ministers, PhotoGallery, UpcomingEvents

class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields = '__all__'


class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = '__all__'


class MinistersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministers
        fields = '__all__'
        
        
class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = '__all__'
        
class UpcomingEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingEvents
        fields = '__all__'