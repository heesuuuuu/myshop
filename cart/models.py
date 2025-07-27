from django.db import models
from django.conf import settings
from products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')  # 같은 사용자가 같은 상품 여러 개 담을 수 없도록

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"
