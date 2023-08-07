import json

def default_response(success=True, status_code=200, message='', result={}, error={}):
    '''
    Function for creating response for APIs
    '''
    if success:
        return {'success': success, 'status_code': status_code, 'message': message, 'result': result, 'error': error}
    else:
        return {'success': success, 'status_code': status_code, 'message': message, 'result': result, 'error': error}


def serializer_error_format(data):
    '''
        This function is used to return single error message if field validation got failed
    '''
    data = json.loads(json.dumps(data))
    resp = []
    for key, value in data.items():
        resp.append(f"{key}: {value[0]}")
    if resp:
        return resp[-1]
    else:
        return "Unable to detect exact error"