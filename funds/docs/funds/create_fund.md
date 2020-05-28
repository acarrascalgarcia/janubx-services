# Create Fund

Allow the user to create funds.

**URL** : `/<:stage>/funds`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

```json
{
    "account_identifier": "[string required]",
    "fund_identifier": "[string required]", 
    "fund_name": "[string required]", 
    "currency_code": "[string required]",
    "fund_description": "[string]",
}
```

**Data examples**

Minimal fields example:

```json
{
	"account_identifier": "ACCOUNT-ID",
	"fund_identifier": "FUND-ID", 
	"fund_name": "ANY FUND NAME", 
	"currency_code": "COP"
}
```

All fields example:


```json
{
	"account_identifier": "ACCOUNT-ID",
	"fund_identifier": "FUND-ID", 
	"fund_name": "ANY FUND NAME", 
	"currency_code": "COP",
    "fund_description": "ANY FUND DESCRIPTION"
}
```

## Success Responses

**Condition** : Data provided is valid.

**Code** : `200 OK`

**Content example** : Response will reflect back the created information.

```json
{
    "links": {
        "self": "any-url/stage/funds"
    },
    "data": {
        "type": "funds",
        "id": "FUND-ID",
        "attributes": {
            "account_identifier": "ACCOUNT-ID",
            "currency_code": "COP",
            "fund_name": "ANY FUND NAME",
            "fund_description": null,
            "fund_identifier": "FUND-ID"
        }
    }
}
```

## Error Response

**Condition** : If provided data is invalid, e.g. a required field not sent.

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{}
```

## Notes

* Endpoint will ignore irrelevant and read-only data such as parameters that
  don't exist.
