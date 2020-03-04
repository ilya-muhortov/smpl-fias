
from django.db import models

__all__ = [
    'FIAS_FederalSubjectManager',
    'FIAS_LocalityManager',
    'FIAS_StreetManager'
]


class FIAS_FederalSubjectManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(level=1)


class FIAS_LocalityManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(level__in=[4])


class FIAS_StreetManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(level=7)
