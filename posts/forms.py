from django import forms
from .models import Ministers, Sermon, UpcomingEvents, Homepage, PhotoGallery
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = '__all__'
        widgets = {
            "sermon_date": DatePickerInput(),
            #'sermon_notes': forms.TextArea(),
        }


class UpcomingEventsForm(forms.ModelForm):
    class Meta:
        model = UpcomingEvents
        fields = "__all__"
        widgets = {
            'event_date': DatePickerInput(),
        }


class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = '__all__'
        widgets = {
            'date_taken': DatePickerInput(),
        }


class HomepageForm(forms.ModelForm):
    class Meta:
        model = Homepage
        fields = "__all__"
        widgets = {
            'event_date': DatePickerInput(),
            'service_1_start_time': TimePickerInput(),
            'service_2_start_time': TimePickerInput(),
            'service_3_start_time': TimePickerInput(),
            'service_4_start_time': TimePickerInput(),
            'latest_sermon_date': DatePickerInput(),
            'event_1_date': DatePickerInput(),
            'event_2_date': DatePickerInput(),
            'event_3_date': DatePickerInput(),
            'event_4_date': DatePickerInput(),
            'event_1_start_time': TimePickerInput(),
            'event_2_start_time': TimePickerInput(),
            'event_3_start_time': TimePickerInput(),
            'event_4_start_time': TimePickerInput(),
            #'church_location': MediumEditorTextarea(),
            #'mission': MediumEditorTextarea(),
        }


class MinistersForm(forms.ModelForm):
    class Meta:
        model = Ministers
        fields = '__all__'
        ordering = ["-minister_authority"]
        widgets = {
            'minister_name': forms.TextInput(attrs={'class': 'textinputclass'}),
            #'word_of_encouragement': MediumEditorTextarea(),
        }
