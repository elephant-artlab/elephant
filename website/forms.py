#coding: utf-8
from django import forms

class ContactForm(forms.Form):

	name = forms.CharField(max_length=60, required=True)
	name.widget.attrs.update({'class' : 'textBox'})
	email = forms.EmailField(max_length=60, required=True)
	email.widget.attrs.update({'class' : 'textBox'})
	message = forms.CharField(required=True, widget = forms.Textarea)
	message.widget.attrs.update({'class' : 'messageBox'})
