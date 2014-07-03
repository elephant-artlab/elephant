from django.shortcuts import render
from .models import Project, Photo
from .forms import ContactForm
from django.core.mail import send_mail



# Create your views here.

def home_view(request):
	projects = Project.objects.all()
	context = {'projects': projects}
	return render(request, 'website/index.html', context)

def project_view(request, project_id):
	project = Project.objects.get(id=project_id)
	photos = Photo.objects.filter(project__id=project_id)
	context = {
		'project': project,
		'photos': photos,
		}
	return render(request, 'website/detail.html', context)

def about_view(request):
	return render(request, 'website/about.html')

def services_view(request):
	return render(request, 'website/services.html')

def test_view(request):
	return render(request, 'website/test.html')

def contact_view(request):
	data_entered = False
	message_sent = False
	if request.method == 'POST':
		data_entered = True
		form = ContactForm(request.POST)
		if form.is_valid():
			email_content = form.cleaned_data['name'] + ' - ' + form.cleaned_data['email'] + ' - ' + form.cleaned_data['message']
			mail_status = send_mail('Contact', email_content, 'contacto@elephant-artlab.com', ['contacto@elephant-artlab.com'], fail_silently=False)
			if mail_status == 1:
				message_sent = True
				form = ContactForm()
			else:
				message_sent = False
			print mail_status
		else:
			data_entered = True
			message_sent = False
		context = {
			'form': form,
			'data_entered': data_entered,
			'message_sent': message_sent,
		}
		return render(request, 'website/contact.html', context)
	else:
		form = ContactForm()
		context = {
			'form': form,
			'data_entered': data_entered,
			'message_sent': message_sent,
		}
		return render(request, 'website/contact.html', context)

def skype_view(request):
    return render(request, 'website/skype.html')

def maintenance_view(request):
	return render(request, 'website/maintenance.html')
	