from django.contrib import admin
from .models import Restaurant

#admin.site.register(Restaurant)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "phone",
        "rating",
        "visitor_count",
        "created_at",
        "updated_at",
    ]
    fields = ["name", "phone", "rating", "latitude", "longitude", "visitor_count"]
    
# 모델 어드민 클래스를 등록할 때는 모델과 모델 어드민 클래스를 함께 등록.
admin.site.register(Restaurant, RestaurantAdmin)