from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from .models import AboutSection
from .models import Home_Section
from .models import Service





def index(request):
    header_data = Home_Section.objects.all()
    return render(request, 'index.html', {'header_data': header_data})



def about(request):
    about_data = AboutSection.objects.all()
    return render(request, 'about.html', {'about_data': about_data})



from .models import ContactSubmission
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        submission = ContactSubmission.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        submission.save()
        
        
    return render(request,'contact.html')


from .models import Feature
def feature(request):
    features = Feature.objects.all()
    return render(request, 'feature.html/', {'features': features})




def service(request):
    services_data = Service.objects.all()
    return render(request, 'service.html', {'services_data': services_data})




