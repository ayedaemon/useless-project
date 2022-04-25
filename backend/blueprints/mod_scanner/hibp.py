import requests
class Hibp:
    @staticmethod
    def get(observable: str)-> list:
        url = f"https://haveibeenpwned.com/api/v3/breaches?domain={observable}"
        headers = {
            "user-agent": "script"
        }
        resp = requests.get(url, headers=headers)
        return resp
