from django.contrib import admin

from .models import BlockCategory, Block, MastersCategory, Masters, UslugiCategory, Uslugi

admin.site.register(BlockCategory)
admin.site.register(Block)
admin.site.register(MastersCategory)
admin.site.register(Masters)
admin.site.register(UslugiCategory)
admin.site.register(Uslugi)