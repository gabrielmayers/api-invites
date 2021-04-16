import requests

def check_invite():
    invite = 'e9LGYg4yvT7jHzME'
    params_req_check = {
        'invite_code': invite,
    }

    r = requests.get("http://127.0.0.1:5000/check_invite", params=params_req_check)
    print(r.text)

check_invite()
