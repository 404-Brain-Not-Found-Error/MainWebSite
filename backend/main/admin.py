from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Developer, Project, ProjectImages, Service, Skills, Role

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'role', 'is_stock', 'github_link')
    list_display_links = ('id', 'user', 'full_name')
    list_editable = ('is_stock',)
    list_filter = ('role', 'is_stock')
    search_fields = ('user__username', 'full_name', 'biography')
    readonly_fields = ('get_avatar',)
    fieldsets = (
        ('Основное', {
            'fields': ('user', 'full_name', 'role', 'biography')
        }),
        ('Соцсети', {
            'fields': ('github', 'telegram'),
            'classes': ('collapse',)
        }),
        ('Настройки', {
            'fields': ('is_stock', 'avatar', 'get_avatar')
        }),
    )
    
    def github_link(self, obj):
        if obj.github:
            return mark_safe(f'<a href="{obj.github}" target="_blank">GitHub</a>')
        return '-'
    github_link.short_description = 'GitHub'

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="150" />')
        return 'Аватар не загружен'
    get_avatar.short_description = 'Текущий аватар'

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'projects_count')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    
    def projects_count(self, obj):
        return obj.project_set.count()
    projects_count.short_description = 'Проектов'

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'developers_count')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    
    def developers_count(self, obj):
        return obj.developer_set.count()
    developers_count.short_description = 'Разработчиков'

class ProjectImagesInline(admin.TabularInline):
    model = Project.images
    extra = 1
    readonly_fields = ('get_photo',)
    
    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.projectimages.image.url}" width="100" />')
    get_photo.short_description = 'Изображение'

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'is_stock', 'developers_list')
    list_display_links = ('id', 'title')
    list_editable = ('is_stock',)
    list_filter = ('is_stock', 'developers', 'skills')
    search_fields = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('developers', 'skills')
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'slug', 'description', 'link')
        }),
        ('Участники и технологии', {
            'fields': ('developers', 'skills')
        }),
        ('Медиа', {
            'fields': ('images',)
        }),
        ('Настройки', {
            'fields': ('is_stock', 'created_date')
        }),
    )
    
    def developers_list(self, obj):
        return ", ".join([dev.full_name for dev in obj.developers.all()])
    developers_list.short_description = 'Разработчики'


class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_photo', 'is_stock', 'project_list')
    list_display_links = ('id',)
    list_editable = ('is_stock',)
    list_filter = ('is_stock',)
    readonly_fields = ('get_large_photo',)
    exclude = ('project',)
    
    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" />')
    get_photo.short_description = 'Изображение'
    
    def get_large_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="300" />')
    get_large_photo.short_description = 'Превью'
    
    def project_list(self, obj):
        projects = obj.project_set.all()
        if projects:
            return ", ".join([p.title for p in projects])
        return 'Не используется'
    project_list.short_description = 'Проекты'

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'duration', 'is_active')
    list_display_links = ('id', 'title')
    list_editable = ('price', 'duration', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'description')
        }),
        ('Цена и сроки', {
            'fields': ('price', 'duration')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImages, ProjectImagesAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Role, RoleAdmin)