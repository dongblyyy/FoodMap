from django.db import models

# Create your models here.
class Restaurant(models.Model):
    # 이름
    name = models.CharField(max_length=50)
    # 주소
    address = models.CharField(max_length=255)
    # 핸드폰
    phone = models.CharField(max_length=20)
    # 위도
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # 경도
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # 평점
    rating = models.SmallIntegerField()
    # 생성 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 업데이트 시간
    updated_at = models.DateTimeField(auto_now=True)
    # 방문자수
    visitor_count = models.IntegerField(default=0)
