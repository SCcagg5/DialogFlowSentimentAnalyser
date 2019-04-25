# **DialogFlow** unary tests app
---

# The App:

Create an account key and allow language API using:
 * https://console.cloud.google.com/apis/credentials/serviceaccountkey
 * https://console.cloud.google.com/apis/api/language.googleapis.com

To launch the app use: `docker-compose up -d --build` from inside the git directory

 * _You **NEED** to store your `GOOGLE_APPLICATION_CREDENTIALS.json` inside the root of the repo_
 * *There is two mode **PROD** and **DEV** :*
   * _**PROD** clone and run the actual git repo_
   * _**DEV** is using your locals files to run_
 * *By default, the mode is set to **PROD** in the `docker-compose.yml` file, to change it set `- PROD=1` to `- PROD=0`*


### Tech :
 
  * **APP**: Docker
  * **FRONT**: /
  * **END**: Python3
  
  
---

# Back end:

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

Warning: * the token params is changed every new call
         * the first part (before the `_`) should'nt change, if it change report bug

### Launching the App:  

From inside the `back-end` dir:

 * `docker build -t sent_back_img .`
 * `docker run --detach --name dialogCorrect -p5000:8080 -it sent_back_img`

