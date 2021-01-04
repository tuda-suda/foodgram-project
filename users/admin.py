from django.contrib import admin, auth


User = auth.get_user_model()


@admin.register(User)
class UserAdmin(auth.admin.UserAdmin):
    list_filter = ('username', 'email')
    search_fields = ('^username', '^email', '^first_name', '^last_name')
    ordering = ('username')


admin.site.unregister(auth.models.Group)
