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

```

**`/sentence/` False**
```javascript

```

### Launching the App:  

From inside the `back-end` dir:

 * `docker build -t sent_back_img .`
 * `docker run --detach --name dialogCorrect -p5000:8080 -it sent_back_img`

## Curl examples
```shell

```
