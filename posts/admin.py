from django.contrib import admin

from posts.models import Post


admin.site.site_title = 'Wordplease Dashboard'
admin.site.site_header = 'Wordplease Dashboard'
admin.site.index_title = 'Wordplease Dashboard'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_select_related = ['author']
    list_display = ['title', 'publish_date', 'author']
    list_filter = ['publish_date', 'author']
    search_fields = ['title', 'publish_date', 'author']
    readonly_fields = ['create_date', 'modification_date']
    # fieldsets = [
    #     ['Dates', {
    #         'fields': ['publish_date'],
    #         'classes': ['collapse']
    #     }]
    # ]
