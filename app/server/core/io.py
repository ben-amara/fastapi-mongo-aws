
from starlette.responses import JSONResponse

def return_exception(exc):
    err = exc.errors()[0]['loc']
    if 'time_limit' in err:
        return JSONResponse({'detail':{"staus_code":405, "error_message":"time_limit only accepts seconds as input"}}) 

    return JSONResponse({'detail':{
            "status_code":400,
            "error_message":"Bad Request"
            }})  