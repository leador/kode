from django.contrib import admin

from .models import News, Category, Tag, Advertise


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'created',
                    'updated', 'published', 'views',)
    list_display_links = ('id', 'title', 'author',)
    list_filter = ('category', 'published',)
    list_editable = ('published',)
    search_fields = ('title', 'category',)
    fields = ('author', 'title', 'slug', 'category', 'poster', 'content', 'published', 'views',)
    readonly_fields = ('views',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    prepopulated_fields = {'slug': ('title',)}


class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'redirect_url', 'click', 'active', 'created',)
    list_editable = ('active',)
    list_display_links = ('id', 'company',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Advertise, AdvertiseAdmin)
