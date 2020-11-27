from django.contrib import admin
from .models import School
from .models import Student
from .models import Professor
from .models import Course
from .models import EnrollsIn

# Register School as an admin site
# this allows us to edit the database from admin section
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(EnrollsIn)
