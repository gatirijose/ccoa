from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField


################ 1 ##################
class UpcomingEvents(models.Model):
    event_name = models.CharField(max_length=80)
    event_banner = CloudinaryField('image', blank=True, null=True)
    event_date = models.DateField(
        default=timezone.now()+datetime.timedelta(days=1))
    event_info = HTMLField()
    pub_date = models.DateField(auto_now_add=True)

    def upcoming_event(self):
        now = timezone.now()
        return now + datetime.timedelta(days=1) <= now <= self.pub_date

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.event_name


######################### 2 ################

class PhotoGallery(models.Model):
    photo_info = models.CharField(max_length=100)
    date_taken = models.DateField(default=timezone.now)
    photo = CloudinaryField('image')

    def get_absolute_url(self):
        return reverse('photo_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.photo_info


######################### 3 #############################
CHOICES = (
    ('Apostle', 'Apostle'),
    ('Rev', 'Rev'),
    ('PST', 'Pst')
)


class Ministers(models.Model):
    minister_authority = models.CharField(
        max_length=20, null=True, choices=CHOICES)
    minister_name = models.CharField(max_length=100)
    minister_photo = CloudinaryField('image')
    word_of_encouragement = HTMLField()

    @property
    def minister_full(self):
        return f'{self.minister_authority} {self.minister_name}'

    def get_absolute_url(self):
        return reverse("ministers_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.minister_authority} {self.minister_name}'


############################ 4 ###################################
TIME = (
    ('Morning', 'Morning'),
    ('Noon', 'Noon'),
    ('Evening', 'Evening'),
)


class Sermon(models.Model):
    sermon_title = models.CharField(max_length=100)
    preached_by = models.ForeignKey(Ministers, on_delete=models.CASCADE)
    sermon_date = models.DateField()
    sermon_time = models.CharField(max_length=15, choices=TIME, null=True)
    sermon_youtube_link = models.URLField(
        help_text='paste a youtube link "https://"')
    sermon_notes = HTMLField()

    def get_absolute_url(self):
        return reverse("sermon_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.sermon_title


########################## 5 ############################################
class Homepage(models.Model):
    ############### photos###############
    slide_photo_1 = CloudinaryField(
        'image', help_text="Enter upcoming event photo here")
    slide_photo_2 = CloudinaryField('image')
    slide_photo_3 = CloudinaryField('image')

    ######## order of services#### 1 ##
    service_1_name = models.CharField(max_length=100)
    service_1_day = models.CharField(
        max_length=30, help_text="enter the days of the week")
    service_1_start_time = models.TimeField()
    service_2_name = models.CharField(max_length=100)
    service_2_day = models.CharField(
        max_length=30, help_text="enter the days of the week")
    service_2_start_time = models.TimeField()
    service_3_name = models.CharField(max_length=100)
    service_3_day = models.CharField(
        max_length=30, help_text="enter the days of the week")
    service_3_start_time = models.TimeField()
    service_4_name = models.CharField(max_length=100)
    service_4_day = models.CharField(
        max_length=30, help_text="enter the days of the week")
    service_4_start_time = models.TimeField()

    ########## Directions ######## 2##
    church_location = HTMLField()
    youtube_link_with_directions = models.URLField(null=True)

    ########## latest sermons ######## 3###
    latest_sermon_youtube_link = models.URLField(null=True)
    preacher = models.ForeignKey(
        Ministers, on_delete=models.CASCADE, null=True)
    sermon_title = models.CharField(max_length=300, null=True)
    latest_sermon_date = models.DateField(null=True)
    latest_sermons = models.ManyToManyField(Sermon)

    ############# upcoming events ######## 4 ####
    event_1_name = models.CharField(max_length=100)
    event_1_date = models.DateField()
    event_1_start_time = models.TimeField()
    event_1_location = models.CharField(max_length=200)

    event_2_name = models.CharField(max_length=100)
    event_2_date = models.DateField()
    event_2_start_time = models.TimeField()
    event_2_location = models.CharField(max_length=200)

    event_3_name = models.CharField(max_length=100)
    event_3_date = models.DateField()
    event_3_start_time = models.TimeField()
    event_3_location = models.CharField(max_length=200)

    event_4_name = models.CharField(max_length=100)
    event_4_date = models.DateField()
    event_4_start_time = models.TimeField()
    event_4_location = models.CharField(max_length=200)

    ############# mission and vision ###### 5 ####
    vision = HTMLField()
    mission = HTMLField()

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(f'{self.id} {self.event_1_date}')
