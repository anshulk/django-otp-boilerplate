from django.contrib import admin
from .models import Otp


class OtpAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp',
                    'used', 'created_at', 'updated_at')


admin.site.register(Otp, OtpAdmin)
