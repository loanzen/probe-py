import json
from apiclient.base import APIClient
from .exceptions import *


class ProbeClient(APIClient):
    
    SUPPORTED_ID_TYPES = ('din', 'pan')

    def __init__(self, api_key=None):
        super(ProbeClient, self).__init__(
            base_url='https://api.probe42.in/probe_lite',
            api_key=api_key,
            auth_header='x-api-key')

        self._companies = 'companies'
        self._company_details = 'companies/{cin}'
        self._signatories = 'authorizedSignatories'
        self._company_signatories = 'companies/{cin}/authorizedSignatories'
        self._company_charges = 'companies/{cin}/charges'

    def search_company(self, company_name):
        if not company_name:
            raise FieldEmptyException('Company Name')

        filters = {
            'nameStartsWith': '{}'.format(company_name)
        }

        return self.call(self._companies, params={'filters': json.dumps(filters)})

    def search_authorized_signatory(self, id_number, id_type='pan'):
        """
        returns details about authorized signatories

        @param id_number: string: ID of the signatory
        @param id_type: string: type of the ID either 'din' or 'pan
        """

        if id_type not in self.SUPPORTED_ID_TYPES:
            raise UnSupportedIDException()

        if not id_number:
            raise FieldEmptyException('ID')

        return self.call(self._signatories,
                         params={'filters': json.dumps({id_type: id_number})})

    def get_company_details(self, cin):
        if not cin:
            raise FieldEmptyException('Company cin')

        return self.call(self._company_details.format(cin=cin))

    def get_company_authorized_signatories(self, cin):
        if not cin:
            raise FieldEmptyException('Company in')

        return self.call(self._company_signatories.format(cin=cin))

    def get_company_charges(self, cin):
        if not cin:
            raise FieldEmptyException('Company in')

        return self.call(self._company_charges.format(cin=cin))