from re import search
from django.contrib import admin
from .models import Book, Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('pk', 'first_name', 'last_name',)
    search_fields=('first_name',)
    list_filter=(
        'first_name',
    )
    readonly_fields=('created_at',)
    date_hierarchy= 'created_at'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name',)
