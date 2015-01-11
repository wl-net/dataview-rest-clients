import json, requests

class DataViewRestClient():
    def __init__(self, endpoint, authtoken, certificate=None):
      self.ENDPOINT = endpoint
      self.AUTHTOKEN = authtoken
      self.CERTIFICATE = certificate
      
    def get_headers(self):
      headers = {'Authorization': 'Token: ' + self.AUTHTOKEN}

    def list_models(self, name):
      return json.loads(requests.get(self.ENDPOINT + '' + name, headers=self.get_headers(), verify=self.CERTIFICATE).text)
    
    def create_model(self):
      return json.loads(requests.post(self.ENDPOINT + '' + name, headers=self.get_headers(), verify=self.CERTIFICATE).text)

    def get_model(self, name, key):
      return json.loads(requests.get(self.ENDPOINT + '' + name + '/' + str(key), headers=self.get_headers(), verify=self.CERTIFICATE).text)
      
    def update_model(self, name, key, values):
        return json.post(requests.get(self.ENDPOINT + '' + name + '/' + str(key), headers=self.get_headers(), verify=self.CERTIFICATE, data=values).text)

    def delete_model(self):
      return json.loads(requests.delete(self.ENDPOINT + '' + name + '/' + str(key), headers=self.get_headers(), verify=self.CERTIFICATE).text)
