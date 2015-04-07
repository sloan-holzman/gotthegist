from django.contrib import admin

# Register your models here.
from ratings.models import Routes, Users, Stops, Matatus, Reviews


class RoutesAdmin(admin.ModelAdmin):
	fields = ['route_id', 'route_shot_name', 'route_desc', 'id']
	list_display = ('route_id', 'route_shot_name', 'route_desc', 'id')

class UsersAdmin(admin.ModelAdmin):
	fields = ['id', 'username']	
	list_display = ('id', 'username')

class MatatusAdmin(admin.ModelAdmin):
	fields = ['id', 'ratings', 'number_of_comments', 'plate_number']
	list_display = ('id', 'ratings', 'number_of_comments', 'plate_number')

class ReviewsAdmin(admin.ModelAdmin):
	fields = ['id', 'route_shot_name', 'plate_number', 'rating', 'date', 'username']
	list_display = ('id', 'route_shot_name', 'plate_number', 'rating', 'date', 'username')


admin.site.register(Routes, RoutesAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Stops)
admin.site.register(Matatus, MatatusAdmin)
admin.site.register(Reviews, ReviewsAdmin)