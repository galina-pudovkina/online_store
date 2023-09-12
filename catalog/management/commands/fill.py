import json
from config.settings import BASE_DIR

from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()

        try:
            with open(BASE_DIR / 'catalog_data.json', 'r', encoding='cp1251') as file:
                category_data = json.load(file)
                for item in category_data:
                    Category.objects.create(
                        pk=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields']['description']
                    )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при импорте данных: {e}'))

        else:
            self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу данных'))
