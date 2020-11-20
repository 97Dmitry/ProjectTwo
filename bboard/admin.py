from django.contrib import admin
from .models import Bb, Rubric



# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published') # Информация, которая будет показана на админ сайте
    list_display_links = ('title', 'content') # Поля, которые будут ссылками на обьект, на админ сайте
    search_fields = ('title', 'content') # Поля, по которым будет вестись поиск на админ сайте

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
