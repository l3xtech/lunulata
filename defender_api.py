import requests
import json

def get_access_token(tenant_id, client_id, client_secret):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    payload = {
        "client_id": client_id,
        "scope": "https://api.securitycenter.microsoft.com/.default",
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None

def get_defender_data(access_token, endpoint):
    url = f"https://api.securitycenter.microsoft.com/{endpoint}"

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_defender_data(tenant_id, client_id, client_secret, endpoint):
    access_token = get_access_token(tenant_id, client_id, client_secret)

    if access_token is None:
        print("Failed to obtain access token.")
        return None
    
    data = get_defender_data(access_token, endpoint)

    if data is None:
        print(f"Failed to get data from endpoint {endpoint}.")
        return None
    else:
        return data

