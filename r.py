import requests

values = range(1)
port = 9002

for i in values:
    port = port + i
    proxyTor = "socks5://127.0.0.1:" + str(port)  # IP:PORT or HOST:PORT

    optionsProxy = {"https": proxyTor}

    link = "https://api.ipify.org"

    res = requests.get(link, proxies=optionsProxy).text

    print('Ваш ip', res)
