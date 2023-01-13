from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UserAdmin(DjangoUserAdmin):
    ordering = ("-created_at",)
    list_display = ("id", "email", "name", "role", "created_at")
    list_filter = ("role", "created_at")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Персональная информация", {"fields": ("name",)}),
        (
            "Доступы",
            {
                "fields": (
                    "role",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Даты", {
            "fields": ("last_login",)
        }),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
