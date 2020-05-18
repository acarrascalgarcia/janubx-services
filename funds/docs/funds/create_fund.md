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
    "account_identifier": "MOCK-ACCOUNT",
    "fund_identifier": "FUND-01", 
    "fund_name": "FUND NAME 01", 
    "currency_code": "COP"
}
```

All fields example:


```json
{
    "account_identifier": "MOCK-ACCOUNT",
    "fund_identifier": "FUND-02", 
    "fund_name": "FUND NAME 02", 
    "currency_code": "COP",
    "fund_description": "ANY DESCRIPTION HERE"
}
```

## Success Responses

**Condition** : Data provided is valid.

**Code** : `200 OK`

**Content example** : Response will reflect back the created information.

```json
{
    "links": {
        "self": "any-url/test/funds"
    },
    "data": {
        "type": "funds",
        "id": "FUND-01",
        "attributes": {
            "account_identifier": "MOCK-ACCOUNT",
            "currency_code": "COP",
            "fund_name": "FUND NAME 01",
            "fund_description": null,
            "fund_identifier": "FUND-01"
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
