from django.contrib import admin

# Register your models here.
# adding this will allow the superuser online to see this and make edits.....

from .models import Job


admin.site.register(Job)

