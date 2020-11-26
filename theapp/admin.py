from django.contrib import admin
from .models import School
from .models import Student

# Register School as an admin site
# this allows us to edit the database from admin section
admin.site.register(School)
admin.site.register(Student)
