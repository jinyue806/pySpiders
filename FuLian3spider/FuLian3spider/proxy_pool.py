import requests

# 开启代理池
class Pool():
    def get_proxy():
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            return None