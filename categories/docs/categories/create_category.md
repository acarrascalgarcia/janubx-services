# Create Category

Allow the user to create categories.

**URL** : `/<:stage>/categories`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

```json
{
    "account_identifier": "[string required]",
    "category_identifier": "[string required]",
    "category_name": "[string required]",
    "category_description": "[string]"
}
```

**Data examples**

Minimal fields example:

```json
{
	"account_identifier": "MOCK-ACCOUNT",
	"category_identifier": "CATEGORY-01",
	"category_name": "CATEGORY NAME 01"
}
```

All fields example:


```json
{
	"account_identifier": "MOCK-ACCOUNT",
	"category_identifier": "CATEGORY-02",
	"category_name": "CATEGORY NAME 02",
    "category_description": "ANY DESCRIPTION HERE"
}
```

## Success Responses

**Condition** : Data provided is valid.

**Code** : `200 OK`

**Content example** : Response will reflect back the created information.
```json
{
    "links": {
        "self": "any-url/test/categories"
    },
    "data": {
        "type": "categories",
        "id": "CATEGORY-01",
        "attributes": {
            "category_description": null,
            "category_name": "CATEGORY NAME 01",
            "account_identifier": "MOCK-ACCOUNT",
            "category_identifier": "CATEGORY-01"
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
