from fastapi import status, HTTPException

def get(func, param):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_content = {
        "status": False,
        "message": "Internal Server Error"
    }
    
    try:
        result = func(...param)
        return result
    
    except Exception as e:
        if e:
            default_content["message"] = e
        raise HTTPException(status_code=status_code, detail=default_content)
    
    except:
        raise HTTPException(status_code=status_code, detail=default_content)
