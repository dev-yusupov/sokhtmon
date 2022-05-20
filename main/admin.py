from django.contrib import admin
from .models import Currency, Contact, Post

# Register your models here.

admin.site.register(Currency)
admin.site.register(Post)
admin.site.register(Contact)