from .models import Subscriber
from app_base.forms import SubscribtionForm

def subscribtion_form(request):
    form = SubscribtionForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        is_exist = Subscriber.objects.filter(email=email).exists()
        if not is_exist:
            form = SubscribtionForm(request.POST)
            if form.is_valid():
                form.save()
    ctx = {
        'form': form
    }
    return ctx