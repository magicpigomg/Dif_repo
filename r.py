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

    
start_port = 9000
end_port = 9005

for i in range(5):
    port = start_port + (i % (end_port - start_port))
    proxyTor = "socks5://127.0.0.1:" + str(port)

    optionsProxy = {"https": proxyTor}

    link = "https://api.ipify.org"

    res = requests.get(link, proxies=optionsProxy).text

    print(f'Ваш ip - {res}\n')
