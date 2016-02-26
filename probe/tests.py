import unittest
from .probe import ProbeClient
from apiclient.exceptions import ApiException


class TestProbeAPI(unittest.TestCase):
    API_KEY = ''

    def test_search_company_empty(self):
        client = ProbeClient(self.API_KEY)
        self.assertRaises(ApiException, client.search_company, '')

    def test_search_company_loanzen(self):
        client = ProbeClient(self.API_KEY)
        company_name = client.search_company('loanzen')['data'][0]['legal_name']
        self.assertEquals(company_name, 'LOANZEN TECHNOLOGIES PRIVATE LIMITED')

    def test_search_authorized_signatory_empty_type(self):
        client = ProbeClient(self.API_KEY)
        self.assertRaises(ApiException, client.search_authorized_signatory, 'BDYPA2435B', '')

    def test_search_authorized_signatory_empty_id(self):
        client = ProbeClient(self.API_KEY)
        self.assertRaises(ApiException, client.search_authorized_signatory, '')

    def test_search_authorized_signatory_valid(self):
        client = ProbeClient(self.API_KEY)
        authorized_signatory_name = client.search_authorized_signatory(
            'ANQPK6045G')['data'][0]['name']
        self.assertEquals(authorized_signatory_name, 'MANPREET SINGH KHURANA')

    def test_get_company_details_empty(self):
        client = ProbeClient(self.API_KEY)
        self.assertRaises(ApiException, client.get_company_details, '')

    def test_get_company_details_valid(self):
        client = ProbeClient(self.API_KEY)
        company_details = client.get_company_details('U24239DL2002PTC114413')
        self.assertFalse(len(company_details) == 0)

    def test_get_company_authorized_signatories_null(self):
        client = ProbeClient(self.API_KEY)
        self.assertRaises(ApiException, client.get_company_authorized_signatories, '')

    def test_get_company_authorized_signatories_valid(self):
        client = ProbeClient(self.API_KEY)
        company_authorized_signatories = client.get_company_authorized_signatories(
            'U24239DL2002PTC114413')
        self.assertFalse(len(company_authorized_signatories) == 0)

    def test_get_company_charges_empty(self):
        client = ProbeClient(self.API_KEY)
        self.assertRaises(ApiException, client.get_company_charges, '')

    def test_get_company_charges_valid(self):
        client = ProbeClient(self.API_KEY)
        company_charges = client.get_company_charges('U24239DL2002PTC114413')
        self.assertFalse(len(company_charges) == 0)


if __name__ == '__main__':
    unittest.main()