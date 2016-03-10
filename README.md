# probe-py
a simple API client for probe apis in python

## how to install

you can install probe-py from pypi

```bash
$ pip install probe-py
```

## how to run

first set an environment variable for api key

```bash
$ export api_key='your api key'
```

### to search company with the company name starting substring
```python

from probe import SearchApi

client = SearchApi()

client.companies_get('api version', filters='{"nameStartsWith": "company-name"}')
```

### to search an authorized signatory with pan/din
```python

from probe import SearchApi

client = SearchApi()

client.authorized_signatories_get(filters='{"pan": "PAN Number of Signatory"}')
```

### to get company details using cin

```python

from probe import CompanyApi

client = CompanyApi()

client.companies_cin_get('api version', 'Company-cin')
```

### list companies authorized signatories

```python

from probe import CompanyApi

client = CompanyApi()

client.companies_cin_authorized_signatories_get('api version', 'Company-cin')
```

### to get the company charges

```python
from probe import CompanyApi

client = CompanyApi()

client.companies_cin_charges_get('api version', 'Company-cin')
```