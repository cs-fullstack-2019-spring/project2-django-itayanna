from django.contrib import admin
from .models import NewEntry, AddRelatedContent, AuthorAccount

# Register your models here.
admin.site.register(NewEntry)
admin.site.register(AuthorAccount)
admin.site.register(AddRelatedContent)