import requests

class ChangeTipApi:

    def __init__(self, user):
        self.token = user.social_auth.filter(provider="changetip").first().extra_data["access_token"]

    def _url(self, path):
        return "https://api.changetip.com/v2%s" % path

    def me(self):
        response = requests.get(self._url("/me/"), params={"access_token": self.token})
        assert response.status_code == 200, response.content
        return response.json()

    def tip_url(self, amount, message=None):
        data = {"amount": amount, "message": message}
        response = requests.post(self._url("/tip-url/"), params={"access_token": self.token}, data=data)
        assert response.status_code == 200, response.content
        return response.json()
