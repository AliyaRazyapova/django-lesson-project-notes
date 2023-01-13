from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return False
        return request.user == obj.user

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
