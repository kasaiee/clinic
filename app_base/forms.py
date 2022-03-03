from app_base.models import Subscriber
from django.forms import ModelForm


class SubscribtionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = "newsletter_input"
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        
    class Meta:
        model = Subscriber
        fields = '__all__'