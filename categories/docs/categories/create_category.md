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
    "account_identifier": "ACCOUNT-ID",
    "category_identifier": "CATEGORY-ID",
    "category_name": "ANY CATEGORY NAME"
}
```

All fields example:


```json
{
    "account_identifier": "ACCOUNT-ID",
    "category_identifier": "CATEGORY-ID",
    "category_name": "ANY CATEGORY NAME",
    "category_description": "ANY DESCRIPTION DESCRIPTION"
}
```

## Success Responses

**Condition** : Data provided is valid.

**Code** : `200 OK`

**Content example** : Response will reflect back the created information.
```json
{
    "links": {
        "self": "any-url/stage/categories"
    },
    "data": {
        "type": "categories",
        "id": "CATEGORY-ID",
        "attributes": {
            "category_description": null,
            "category_name": "ANY CATEGORY NAME",
            "account_identifier": "ACCOUNT-ID",
            "category_identifier": "CATEGORY-ID"
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
