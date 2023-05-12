from django.contrib import admin

# Register your models here.
from .models import DeptDetails,StudentInfo,Feed,FAC,COU

admin.site.register(DeptDetails)
admin.site.register(StudentInfo)
admin.site.register(Feed)
admin.site.register(FAC)
admin.site.register(COU)