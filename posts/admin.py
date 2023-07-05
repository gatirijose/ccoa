from django.contrib import admin
from .models import Ministers, Sermon, UpcomingEvents, Homepage, PhotoGallery

@admin.register(Sermon)
class SermonModelAdmin(admin.ModelAdmin):
    list_display = ['sermon_title', 'sermon_date',
                    'sermon_time', 'preached_by']
    list_filter = ['sermon_date', 'preached_by']



@admin.register(Ministers)
class MinistersAdmin(admin.ModelAdmin):
    list_display = ['minister_full', 'minister_photo']
    list_display_links = ['minister_full']


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ['latest_sermon_date', 'vision', 'mission']


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['photo_info', 'date_taken']
    list_display_links = ['photo_info', 'date_taken']


@admin.register(UpcomingEvents)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_date', 'pub_date']
    list_filter = ['event_date']

