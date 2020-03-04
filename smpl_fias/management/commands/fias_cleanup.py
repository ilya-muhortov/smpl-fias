
from django.core.management.base import BaseCommand
from smpl_fias.models import FIAS_Object


class Command(BaseCommand):

    def handle(self, *args, **options):
        confirm = input('Вы собириетесть удалить все данные? (yes/no) ')

        if confirm in ['y', 'yes']:
            FIAS_Object.objects.all().delete()
