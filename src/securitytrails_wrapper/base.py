import requests

class SecurityTrailsBase:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.securitytrails.com/v1"
        self.session = requests.Session()
        self.session.headers.update({"APIKEY": self.api_key})

    def make_request(self, method, path, **kwargs):
        url = f"{self.base_url}/{path}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            return None

        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            return None

        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            return None

        except requests.exceptions.RequestException as err:
            print("Oops: Something Else", err)
            return None
        return response.json()
