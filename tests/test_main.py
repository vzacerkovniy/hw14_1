from unittest.mock import patch

import pytest

from src.main import Category, Product, read_json


@pytest.fixture
def prod():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def cat():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться " "просмотром, станет вашим другом и помощником",
        ["product"],
    )


def test_prod_init(prod):
    assert prod.name == "Samsung Galaxy S23 Ultra"
    assert prod.description == "256GB, Серый цвет, 200MP камера"
    assert prod.price == 180000.0
    assert prod.quantity == 5


def test_cat_init(cat):
    assert cat.name == "Телевизоры"
    assert cat.description == (
        "Современный телевизор, который позволяет наслаждаться " "просмотром, станет вашим другом и помощником"
    )
    assert cat.products == ["product"]
    assert cat.product_count == 1
    assert cat.category_count == 1
