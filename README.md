# Project: ScanLori API Doc

## Live Demo -dev
```sh
https://api-scanlori.techside.my.id/
```

## End-point: SignUp
### Method: POST
>```
>http://localhost:8080/api/auth/signup
>```
### Body (**raw**)

```json
{
    "username": "riyanada",
    "email": "riyanmaulana402@yahoo.co.id",
    "password": "123123",
    "roles": [
        "admin"
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: SignIn
Gets information about the authenticated user.
### Method: POST
>```
>http://localhost:8080/api/auth/signin
>```
### Body (**raw**)

```json
{
    "username": "riyanada",
    "password": "123123"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create a Food
### Method: POST
>```
>http://localhost:8080/api/foods
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Headers

|Content-Type|Value|
|---|---|
|x-access-token|{{accessToken}}|


### Body (**raw**)

```json
{
    "nama_makanan": "Air",
    "kalori_kcal": 0,
    "kolestrol_mg": 0,
    "lemak_g": 0,
    "karbohidrat_g": 0,
    "protein_g": 0,
    "kalium_mg": 0,
    "nutrisi": "-",
    "ingredient": "-"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Public
Gets information about a collection. For a complete list of this endpoint's possible values, use the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).
### Method: GET
>```
>http://localhost:8080/api/public
>```
### Headers

|Content-Type|Value|
|---|---|
|x-access-token|{{accessToken}}|

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get All Foods
Gets all of your [collections](https://www.getpostman.com/docs/collections). The response includes all of your subscribed collections.
### Method: GET
>```
>http://localhost:8080/api/foods
>```
### Headers

|Content-Type|Value|
|---|---|
|x-access-token|{{accessToken}}|

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Spesific Food
Gets all of your [collections](https://www.getpostman.com/docs/collections). The response includes all of your subscribed collections.
### Method: GET
>```
>http://localhost:8080/api/foods/2
>```
### Headers

|Content-Type|Value|
|---|---|
|x-access-token|{{accessToken}}|

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update a Food
### Method: PUT
>```
>http://localhost:8080/api/foods/2
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Headers

|Content-Type|Value|
|---|---|
|x-access-token|{{accessToken}}|


### Body (**raw**)

```json
{
    "nama_makanan": "Anggurs",
    "kalori_kcal": 30,
    "kolestrol_mg": 0,
    "lemak_g": 0.2,
    "karbohidrat_g": 6.8,
    "protein_g": 0,
    "kalium_mg": 0,
    "nutrisi": "Vitamin C, Vitamin B1",
    "ingredient": "-"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete a Food
Deletes a collection.
### Method: DELETE
>```
>http://localhost:8080/api/foods/38
>```
### Headers

|Content-Type|Value|
|---|---|
|x-access-token|{{accessToken}}|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
