from django.contrib import admin

from carbon.compounds.media.admin import ImageAdmin as BaseImageAdmin
from carbon.compounds.media.admin import MediaAdmin as BaseMediaAdmin
from carbon.compounds.media.admin import SecureMediaAdmin as BaseSecureMediaAdmin
from carbon.compounds.media.admin import MediaTagAdmin as BaseMediaTagAdmin

from .models import *
from .forms import *

from django_unsaved_changes.admin import UnsavedChangesAdmin




class ImageAdmin(BaseImageAdmin, UnsavedChangesAdmin):

    batch_url_name = "admin_image_batch_view"

    form = ImageAdminForm

    core_fields = (
        'title',
        ('image','preview'),
        ('square_crop', 'width_1200_wide_crop'),
       
        ('image_variants'),
        ('clean_filename_on_upload','allow_overwrite'),
        ('alt','use_png'),
        'credit',
        'caption',
    )
    

    meta_fields = (
        ('version'),
        ('created_date', 'created_by'),
        ('modified_date', 'modified_by'),
        'admin_note'
    )

    fieldsets = (
        ("Image", {
            'fields': core_fields,
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )

    #TEMPORARY:
    def full_list(self, obj):
        
        output = ''
        output += '<strong>Caption: </strong>%s<br /><br />'%(obj.caption)
        output += '<strong>Credit: </strong>%s<br /><br />'%(obj.credit)
        output += '<strong>Alt: </strong>%s'%(obj.alt)
        return output
    full_list.allow_tags = True

    list_display = ('title','preview','image_width', 'image_height', 'display_size', 'full_list')
    list_display_links = ('title', 'preview')

    readonly_fields = (
        "version", "created_date", "created_by", "modified_date", "modified_by",
        "preview", "image_variants", "tag_list", "full_list"
    )



class MediaAdmin(BaseMediaAdmin, UnsavedChangesAdmin):
    pass

# class SecureMediaAdmin(BaseSecureMediaAdmin):
#     pass

class MediaTagAdmin(BaseMediaTagAdmin, UnsavedChangesAdmin):
    pass    


admin.site.register(Image, ImageAdmin)
admin.site.register(Media, MediaAdmin)    
# admin.site.register(SecureMedia, SecureMediaAdmin)  
admin.site.register(MediaTag, MediaTagAdmin)        