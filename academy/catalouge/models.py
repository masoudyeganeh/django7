from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=35, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3

    ATTRIBUTE_TYPES_FIELDS = {
        (INTEGER, "INTEGER"),
        (STRING, "STRING"),
        (FLOAT, "FLOAT")
    }

    title = models.CharField(max_length=35, blank=True, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    attribute_type = models.PositiveSmallIntegerField(default=INTEGER, choices=ATTRIBUTE_TYPES_FIELDS)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=35)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=35)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    upc = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=35)
    description = models.TextField(blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}({self.product_attribute}): {self.value}"
