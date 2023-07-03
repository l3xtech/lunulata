from decouple import config
import defender_api

def main():
    tenant_id = config('DEFENDER_TENANT_ID')
    client_id = config('DEFENDER_CLIENT_ID')
    client_secret = config('DEFENDER_CLIENT_SECRET')
    endpoint = "YOUR_ENDPOINT"

    data = defender_api.fetch_defender_data(tenant_id, client_id, client_secret, endpoint)

    if data is not None:
        print(data)

if __name__ == "__main__":
    main()

