from django.contrib import admin

from .models import Project, SiteProfile


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'headline', 'location')
    fieldsets = (
        ('Identitas', {
            'fields': ('display_name', 'pronouns', 'headline', 'location', 'photo'),
        }),
        ('Tentang', {
            'fields': ('about', 'marquee_text'),
        }),
        ('Kontak & Sosial', {
            'fields': ('email', 'github_url', 'instagram_url', 'linkedin_url'),
        }),
        ('Tech Stack', {
            'fields': ('stack',),
            'description': 'Satu grup per baris, format "Grup: item1, item2".',
        }),
    )

    def has_add_permission(self, request):
        # Profil cuma satu — kalau sudah ada, tombol "add" disembunyikan.
        if SiteProfile.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'featured', 'tagline')
    list_editable = ('order', 'featured')
    list_filter = ('featured',)
    search_fields = ('title', 'tagline', 'tech')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
        'title', 'slug', 'tagline', 'description', 'tech',
        'image', 'link_url', 'repo_url', 'featured', 'order',
    )
