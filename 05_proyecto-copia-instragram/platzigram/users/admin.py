from django.contrib import admin

from users.models import Profile


# Register your models here.
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','phone_number','website','picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website')
    search_fields = ('user__email','user__first_name','user_last_name')