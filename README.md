# Sentiments analyser app

[![CodeFactor](https://www.codefactor.io/repository/github/sccagg5/dialogflowsentimentanalyser/badge)](https://www.codefactor.io/repository/github/sccagg5/dialogflowsentimentanalyser)
[![codebeat badge](https://codebeat.co/badges/0fd0d0b5-ca45-4452-9d05-f048323d3bd0)](https://codebeat.co/projects/github-com-sccagg5-dialogflowsentimentanalyser-master)
[![BCH compliance](https://bettercodehub.com/edge/badge/SCcagg5/DialogFlowSentimentAnalyser?branch=master)](https://bettercodehub.com/)

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

**Warning**: 
  * the `token` parameter is changed every new call
  * the first part (before the `_`) should'nt change, if it does change report bug

### Launching the App:  

From inside the `back-end` dir:

 * `docker build -t sent_back_img .`
 * `docker run --detach --name dialogCorrect -p5000:8080 -it sent_back_img`

