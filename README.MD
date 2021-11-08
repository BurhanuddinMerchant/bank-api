# Bank API Endpoints

PostgreSQL Database hosted on [CLEVER CLOUD](https://www.clever-cloud.com/) as an Add-On resource
Django Project hosted on Heroku [here](https://bank-api-task.herokuapp.com/api/)
Used [DRF](https://www.django-rest-framework.org/) for making the REST API's

Curl Scripts for accessing the API's

1. Autocomplete API

```curl
curl --location --request GET 'https://bank-api-task.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=3&offset=1'
```

2. Search Throughout the table

```curl
curl --location --request GET 'https://bank-api-task.herokuapp.com/api/branches?q=BANGALORE&limit=3&offset=0'
```

Thank You
