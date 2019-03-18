from django import forms
from .models import NewEntry,AuthorAccount,AddRelatedContent


class NewEntryform(forms.ModelForm):
    class Meta:
        exclude = ['authour']
        model = NewEntry


class AddRelatedContentForm(forms.ModelForm):
    class Meta:
        exclude = ['parentPost']
        model = AddRelatedContent


class NewAuthorForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = AuthorAccount

