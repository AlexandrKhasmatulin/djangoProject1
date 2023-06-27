from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name':'Электротранспорт', 'description':'Гироскутеры, Электросамокаты, Моноколеса, Электровелосипеды'},
            {'name':'Компьютеры', 'description':'Ноутбуки, ПК, Мониторы, комплектующие'},
            {'name':'Смартфоны', 'description':'смартфоны, гаджеты, аксессуары, сопутствующие товары'},
            {'name':'Умный Дом', 'description':'Освещение, замки, датчики, умная техника, розетки'},

        ]
        for category_item in category_list:
            Category.objects.create(**category_item)
