from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # 이미지 필드 추가
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    # on_delete=models.CASCADE는 Category가 삭제될 때 Product도 함께 삭제됨을 의미
    # null=True, blank=True는 이 필드가 선택적임을 의미
    # foreign key로 Category 모델과 연결
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name
