from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (Developer, Project, ProjectImages, Service, Skills, Role)


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('user','id','full_name', 'role', 'entry_date')

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title','id','slug')
    prepopulated_fields = {'slug' : ('title',)}

class RoleAdmin(admin.ModelAdmin):
    list_display = ('title','id','slug')
    prepopulated_fields = {'slug' : ('title',)}

class ProjectImagesAdmin(admin.ModelAdmin):

    list_display = ('image','id','get_photo')

    def get_photo(self, object):
        if object.image:
            return mark_safe(f'<img src= {object.image.url} width=50 >')

    get_photo.short_description = 'Фото'

class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('title','id', 'link')
    search_fields = ('title','slug')
    prepopulated_fields = {'slug' : ('title',)}

class ServiceAdmin(admin.ModelAdmin):

    list_display = ('title','id','price')




admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImages, ProjectImagesAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Role, RoleAdmin)