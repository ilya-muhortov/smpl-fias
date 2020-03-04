
from ..models import FIAS_Object


def full_address_representation(fias_object: FIAS_Object):
    chain = []
    current_fias_object = fias_object
    while True:
        chain.append(current_fias_object)
        if current_fias_object.parent_guid:
            current_fias_object = FIAS_Object.objects.filter(aoid=current_fias_object.parent_guid).first()
            if not current_fias_object:
                break
