from django.contrib import admin
from .models import Language, Stage, Branch, Author, Project

# Register your models here.

admin.site.register(Language)
admin.site.register(Stage)
admin.site.register(Branch)
admin.site.register(Author)
admin.site.register(Project)
