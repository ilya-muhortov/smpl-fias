
from django.db import models

from smpl_fias.models import FIAS_FederalSubject, FIAS_Locality


class DemoModel(models.Model):

    federal_subject = models.ForeignKey(FIAS_FederalSubject, related_name='demo_federal_subject',
                                        on_delete=models.CASCADE)
    locality = models.ForeignKey(FIAS_Locality, related_name='demo_locality', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.federal_subject.__str__()
