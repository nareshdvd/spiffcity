from django.contrib import admin
from getsocial.models import Album, Category, City, Country, State, Photo

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class AlbumAdmin(admin.ModelAdmin):
    pass
admin.site.register(Album, AlbumAdmin)


class CountryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    pass
admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)


class PhotoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Photo, PhotoAdmin)