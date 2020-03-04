
from django.core.management.base import BaseCommand, CommandError

from smpl_fias.utils.importdata import load_xml


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filepath', type=str, required=True)
        parser.add_argument('-r', '--region_code', type=str)
        parser.add_argument('-l', '--levels', type=str)
        parser.add_argument('-i', '--ignore_inactive', action='store_true')

    def handle(self, *args, **options):
        load_xml(
            options['filepath'],
            ignore_inactive=options['ignore_inactive'],
            region_code=options['region_code'],
            levels=[int(level) for level in options['levels'].split(',') if level.isdigit()]
        )
