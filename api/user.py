
from logging import exception
import time
import requests
from api.public import indodax

from requests_toolbelt import sessions
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 504])
adapter = HTTPAdapter(max_retries=retries)

http = sessions.BaseUrlSession(base_url="https://tanlalana.com/api/")
http.mount("https://", adapter)
http.mount("http://", adapter)


class user_indodax:
    def update_user(coin,id_users):
        try:
            param={'coin':coin,'id_users':id_users}
            url="update_user_indodax"
            http.post(url,data=param)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    def indodax_login(email,password):
        this_email=email
        this_password=password
        try:
            url="indodax_login"
            param={'email':email,'password':password}
            r=http.post(url,data=param)
            respon=r.json()
            return respon

        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return user_indodax.indodax_login(this_email,this_password)
        