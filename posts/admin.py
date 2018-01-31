from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title','content','timestamp']
	list_display_links = ['title']
	list_editable = ['content']
	list_filter = ['timestamp']
	search_fields = ['title', 'content']
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
