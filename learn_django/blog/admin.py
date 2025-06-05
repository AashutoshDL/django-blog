from django.contrib import admin
from .models import Post

# Register your models here.
# here we need to add the blog model so that we can register the model which show up in the admin page GUI
admin.site.register(Post)