from django.contrib import admin
from posts.models import Post
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","timestamp","updated"]
	list_display_link = ["updated"]
	list_editable = ["title"]
	list_filter =["timestamp"]
	search_fields =["title","content"]
	class Meta:
		model = Post

admin.site.register(Post,PostModelAdmin)
