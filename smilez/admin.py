from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)
admin.site.site_header = 'Smilez Shop'
admin.site.site_title = 'Smilez store'
list_display = ('fname', 'email', 'message')
list_editable = ('email', 'message')
