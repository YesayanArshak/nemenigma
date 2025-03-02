from django.contrib import admin
from django.http import HttpRequest
from django.utils import datastructures
from django.utils.translation import gettext_lazy as _


from user.models import User, Key
from user.forms import UserForm, KeyForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ['pk', 'username', 'user_type', 'creation_time']
    date_hierarchy = 'creation_time'
    fieldsets = [
        (
            None,
            {
                'fields': ['username', 'password']
            }
        ),
        (
            _('Info'),
            {
                'fields': ['user_type', 'description'],
            }
        ),
        (
            _('Dates'),
            {
                'fields': ['creation_time'],
            }
        ),
    ]

    def get_readonly_fields(self, request: HttpRequest, obj: 'admin.options._ModelT | None' = ...) -> 'datastructures._ListOrTuple[str]':
        return list(
            {field.name for field in self.opts.local_fields} | {field.name for field in self.opts.local_many_to_many}
        )
        # return super().get_readonly_fields(request, obj)

@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    form = KeyForm
    list_display = ['user', 'key_type', 'tool_type', 'creation_time']
