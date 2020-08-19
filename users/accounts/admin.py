from django.contrib import admin

from users.accounts.models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'user_type', 'main_email',
                    'alternative_email', 'usp_email', 'formatted_phone')


admin.site.register(UserModel, UserModelAdmin)
admin.site.site_header = 'Intranet Usuários'
admin.site.site_title = 'Intranet Usuários'
admin.site.index_title = 'Intranet Usuários'
