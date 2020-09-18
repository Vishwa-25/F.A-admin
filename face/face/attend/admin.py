from django.contrib import admin
from .models import face


# Register your models here.
class faceAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', )


admin.site.register(face, faceAdmin)
admin.site.site_header = 'Security_admin'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Admin_view'
