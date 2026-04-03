from django.contrib import admin
from .models import AboutGalleryImage, AboutPage, HomeContentBlock, TeamMember


@admin.register(HomeContentBlock)
class HomeContentBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not AboutPage.objects.exists()


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('full_name', 'role')


@admin.register(AboutGalleryImage)
class AboutGalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
