# probe-py
a simple API client for probe apis in python

## how to install

you can install probe-py from pypi

$pip install probe-py

## how to run

first set an environment variable for api key

$ export api_key='your api key'


from probe import SearchApi, CompanyApi


### to search company with the company name starting substring

client = SearchApi()

client.companies_get(filters='{"nameStartsWith": "company-name"}')


### to search an authorized signatory with pan/din

client.authorized_signatories_get(filters='{"pan": "PAN Number of Signatory"}')


### to get company details using cin

client = CompanyApi()

client.companies_cin_get('Company-cin')


### list companies authorized signatories

client.companies_cin_authorized_signatories_get('Company-cin')

### to get the company charges

client.companies_cin_charges_get('Company-cin')