# from django.contrib import admin
# from rango.models import Category, Page

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'views', 'likes')

# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url', 'views')
    

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Page, PageAdmin)


from django.contrib import admin
from .models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

    #, 'views', 'likes'

admin.site.register(Page, PageAdmin)

admin.site.register(Category)