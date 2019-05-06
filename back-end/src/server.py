from bottle import run, route, get, post, response, request, hook
from returnvalue import ret
from params import check
from users import user
from analysis import sentiment
import os

@get('/test/')
@post('/test/')
def base():
        try:
            params = check.json(request)
        except:
            params = []
        toret = ret(request.route.rule, params)
        return toret.ret()

@post('/sentence/')
def base():
    try:
        params = check.json(request)
    except:
        params = []
    toret = ret(request.route.rule, params)
    
    if not toret.err:
        err = check.contain(params, ["sentence", "lang"])
        if not err[0]:
            toret.add_error(err[1], err[2])
            
    if not toret.err:
        token = params["token"] if "token" in params else None
        use = user(params["lang"], token)
        score = sentiment().analyse(params["sentence"])
        use.add_score(score)
        arr = {
                "sentence": params["sentence"],
                "score": score,
                "user": {
                        "token": use.get_token(),
                        "score": use.score(),
                        "negatif": use.is_negatif()
                        }
        }
        toret.add_data(arr)

    return toret.ret()

if __name__ == '__main__':
    try:
        run(host='0.0.0.0', port=8080)
    except:
        os._exit(0)
