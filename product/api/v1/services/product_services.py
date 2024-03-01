from product.models import Product


class ProductServices:
    def __init__(self):
        self.queryset = Product.objects.all()

    def create_product(self, validated_data) -> Product:
        name = validated_data['name']
        start_date = validated_data['start_date']
        author = validated_data['author']
        price = validated_data['price']

        return Product.objects.create(name=name, author=author, start_date=start_date, price=price)
