from django.contrib import admin
from .models import (
    Author ,
    Book ,
    Genre ,
    Publisher,
     ) 



# admin.site.register(Publisher)
admin.site.register(Genre)


def make_published(modeladmin, request , queryset):

    result = queryset.update(status='publish')

    if result == 1:
        message_bit = "یه پست  "
    else :
        message_bit = "{} پست ".format(result)

    modeladmin.message_user(request,"{} با موفقیت انتشار یافت".format(message_bit))

def make_draft(modeladmin , request , queryset):
    result = queryset.update(status = 'draft')

    if result == 1:
        message_bit = "یه پست  "
    else :
        message_bit = "{} پست ".format(result)

    modeladmin.message_user(request,"{}  با موفقیت پیشنویس یافت :)".format(message_bit))



make_draft.short_description = 'پیش نویس شو'
make_published.short_description = 'انتشار بده'
# export_as_json.short_description = 'export'


    


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'date_of_birth', 'date_of_death','nick_name')

    fields = [
        'first_name',
        'last_name',
        'nick_name',
        ('date_of_birth', 'date_of_death'),
    ]
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'display_author' , 'summary','img', 'display_genre', 'pages','publisher')
    
    def display_author(self,obj):
        return ','.join([author.first_name for author in obj.author.all()[:2] ])

    def display_genre(self , obj):
        return ','.join([genre.name for genre in obj.genre.all()[:3] ])
    
    display_genre.short_description = 'ژانر'
    list_filter = ('author', 'publisher')
    search_fields = ('title', 'summary')
    actions = [make_published , make_draft  ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','phone')