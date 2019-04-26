# Sentiments analyser app

### Route:  

Route| Method| Content Type |Parameters| Description |
:-|:-:|:-:|:-:|:-|
/test/ | POST, GET |  |  | return an empty response pattern
/sentence/ | POST | JSON | sentence, lang, token| return the score of the user ]1.000, -1.000\[

### Parameters:
```javascript
{
  "sentence" : "*YOUR TEXT*",
  "lang": "YOUR_LANG", // ["fr", "en"]
  "token": "USER'S TOKEN" //if NULL the app return a new one 
}
```

**Warning**: 
  * the `token` parameter is changed every new call
  * the first part (before the `_`) should'nt change, if it change report bug


### Return example:
**`/sentence/` True**
```javascript
{
    "succes": true,
    "error": null,
    "queryInfos": {
        "params": {
            "sentence": "je me sens mieux",
            "lang": "fr"
        },
        "route": "/sentence/"
    },
    "data": {
        "user": {
            "negatif": false,
            "token": "47609f83e45043e4b0104f856d7413a7_0.0_1",
            "score": 0
        },
        "sentence": "je me sens mieux",
        "score": 0
    },
    "status": 200
}
```

**`/sentence/` False**
```javascript
{
    "succes": false,
    "error": "Missing parameter : lang",
    "queryInfos": {
        "params": {
            "sentence": "je me sens mieux"
        },
        "route": "/sentence/"
    },
    "data": null,
    "status": 400
}
```

### Launching the App:  

From inside the `back-end` dir:

 * `docker build -t sent_back_img .`
 * `docker run --detach --name dialogCorrect -p5000:8080 -it sent_back_img`

## Curl examples
```shell
curl -X POST \
  http://localhost:5000/sentence/ \
  -H 'Content-Type: application/json' \
  -d '{
	"token": "47609f83e45043e4b0104f856d7413a7_-0.7_1",
	"sentence": "je me sens mieux",
	"lang": "fr"
}'
```
