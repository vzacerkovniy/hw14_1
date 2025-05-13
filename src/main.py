import json


class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории продукта"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


def read_json() -> dict:
    with open("../data/products.json", encoding="utf-8") as f:
        data = json.load(f)
        category_list = []
        product_list = []
        for i in data:
            cat = Category(i["name"], i["description"], i["products"])
            category_list.append(cat)
        for i in category_list:
            for c in i.products:
                prod = Product(c["name"], c["description"], c["price"], c["quantity"])
                product_list.append(prod)
        # print(category_list)
        # print(category_list[0].name)
        # print(category_list[0].description)
        # print(category_list[0].products)
        # print(category_list[0].category_count)
        # print(category_list[0].product_count)
        # print(product_list)
        # print(product_list[0].name)
        # print(product_list[0].description)
        # print(product_list[0].price)
        # print(product_list[0].quantity)
        dict_obj = {"Category obj": category_list, "Product obj": product_list}
        return dict_obj


if __name__ == "__main__":
    print(read_json())
