
import os
from xml.etree.ElementTree import iterparse

from smpl_fias.models import FIAS_Object


def load_xml(filepath, ignore_inactive=True, region_code=None, levels=None):

    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        raise ValueError(f'File "{filepath}" not found')

    with open(filepath) as xml_file:
        for event, element in iterparse(xml_file, events=('start', 'end')):
            if element.tag == 'Object':
                if element.attrib:
                    address = element.attrib
                    if not ignore_inactive or address['LIVESTATUS'] == '1':
                        if (region_code is None or element.attrib['REGIONCODE'] == region_code) and \
                                (levels is None or int(address['AOLEVEL']) in levels):
                            FIAS_Object.objects.update_or_create(
                                defaults=dict(
                                    parent_guid=address.get('PARENTGUID'),
                                    aoguid=address.get('AOGUID'),
                                    name=address['OFFNAME'],
                                    short_name=address['SHORTNAME'],
                                    region_code=address['REGIONCODE'],
                                    area_code=address['AREACODE'],
                                    city_code=address['CITYCODE'],
                                    postal_code=address.get('POSTALCODE'),
                                    okato=address.get('OKATO'),
                                    oktmo=address.get('OKTMO'),
                                    level=address['AOLEVEL'],
                                    kladr=address.get('CODE'),
                                    cent_status=address['CENTSTATUS'],
                                    live_status=address['LIVESTATUS'] == '1'
                                ),
                                aoid=address['AOID']
                            )
                    else:
                        fias_object = FIAS_Object.objects.filter(aoid=address['AOID']).first()
                        if fias_object:
                            fias_object.live_status = address['LIVESTATUS'] == '1'
                            fias_object.save()

                element.clear()
