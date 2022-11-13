from django.contrib import admin
from simple_app.models import ActionList, ActionRecord, User

# Register your models here.
admin.site.register(ActionList)
admin.site.register(ActionRecord)
admin.site.register(User)