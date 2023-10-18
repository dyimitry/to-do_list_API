from fast_api_client.client import Client

client = Client(base_url="http://127.0.0.1:8000")
aaa = client.get_httpx_client()



# pip install swagger-codegen