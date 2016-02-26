# probe-py
a simple API client for probe apis in python

## how to install

install the probe-py package like this

$pip install git+https://github.com/loanzen/probe-py.git#egg=probe

## how to run

from probe import ProbeClient


client = ProbeClient('your api key')

### to search company with the company name starting substring

client.search_company('company_name_starts_with')

### to search an authorized signatory with pan/din

client.search_authorized_signatory('pan_number', 'pan')

### to get company details (you will need cin of company)

client.get_company_details('company_cin')


### list companies authorized signatories

client.get_company_authorized_signatories('Company_cin')

### to get the company charges
client.get_company_charges('company_cin')