from django.contrib import admin
from .models import News, Review, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'is_published', 'has_image')
    list_filter = ('is_published', 'date_created')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    
    def has_image(self, obj):
        return bool(obj.image)
    has_image.short_description = 'Есть изображение'
    has_image.boolean = True

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'date_created', 'is_approved')
    list_filter = ('is_approved', 'date_created')
    search_fields = ('author_name', 'content')
    list_editable = ('is_approved',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'news', 'date_created', 'is_approved')
    list_filter = ('is_approved', 'date_created')
    search_fields = ('author_name', 'content')
    list_editable = ('is_approved',)
