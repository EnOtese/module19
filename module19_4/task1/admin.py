from django.contrib import admin
from task1.models import Game, Buyer

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')
    list_display = ('title', 'cost', 'size')
    search_fields = ('title', )
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)