from django.db import models
from django.conf import settings

from carbon.compounds.page.models import Page as BasePage
from carbon.compounds.page.models import PageContentBlock as BasePageContentBlock
from carbon.compounds.page.models import GlobalContentBlock as BaseGlobalContentBlock
from carbon.atoms.models.content import SlideMolecule, HasSlidesMolecule

from imagekit import ImageSpec
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.admin import AdminThumbnail
from imagekit.processors import ResizeToFill, ResizeToFit

from lesleyloraine.apps.media.models import Image



class PageSlide(SlideMolecule):
    parent = models.ForeignKey('page.Page')

class Page(BasePage):
    default_template = 'page-base'
    slide_class = PageSlide

    form = models.ForeignKey('form.Form', blank=True, null=True)

    def get_page_content_blocks(self):
        blocks = PageContentBlock.objects.filter(parent=self).order_by('order')
        published = [block for block in blocks if block.is_published()]
        return published

class PageContentBlock(BasePageContentBlock):
    pass

class GlobalContentBlock(BaseGlobalContentBlock):
    pass    