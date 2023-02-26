from django.contrib import admin
from .models import Profile


class WebFrontendAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'contact_number' ]

    class Meta:
        model = Profile


admin.site.register(Profile, WebFrontendAdmin)
