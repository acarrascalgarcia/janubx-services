# Create Transaction

Allow the user to create transactions.

**URL** : `/<:stage>/transactions`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

```json
{
    "account_identifier": "[string required]",
    "category_identifier": "[string required]",
    "transaction_date": "[date-formatted string required]",
    "transaction_amount": "[number required]",
    "transaction_detail": "[string required]",
    "transaction_action": "[integer required]",
    "category_name": "[string required]"
}
```

```
transaction_date:  YYYY-mm-dd
transaction_action: -1 | 0 | 1
```

**Data examples**

Minimal fields example:

```json
{
    "account_identifier": "ACCOUNT-ID",
    "category_identifier": "CATEGORY-ID",
    "transaction_date": "2020-03-16",
    "transaction_amount": 45000,
    "transaction_detail": "ANY TRANSACTION DETAIL",
    "transaction_action": -1,
    "category_name": "ANY CATEGORY NAME"
}
```

All fields example:


```json
{
    "account_identifier": "ACCOUNT-ID",
    "category_identifier": "CATEGORY-ID",
    "transaction_date": "2020-03-16",
    "transaction_amount": 45000,
    "transaction_detail": "ANY TRANSACTION DETAIL",
    "transaction_action": -1,
    "category_name": "ANY CATEGORY NAME"
}
```

## Success Responses

**Condition** : Data provided is valid.

**Code** : `200 OK`

**Content example** : Response will reflect back the created information.

```json
{
    "links": {
        "self": "any-url/stage/transactions"
    },
    "data": {
        "type": "transactions",
        "id": "TRANSACTION-ID",
        "attributes": {
            "transaction_identifier": "TRANSACTION-ID",
            "category_identifier": "CATEGORY-ID",
            "transaction_amount": 45000,
            "transaction_detail": "ANY TRANSACTION DETAIL",
            "transaction_date": "2020-03-16",
            "account_identifier": "ACCOUNT-ID",
            "category_name": "ANY CATEGORY NAME",
            "transaction_action": -1
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
