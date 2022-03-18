# pip --version
# pip list
# pip install requests
# pip freeze

import requests


def return_cep_data(cep):
    return requests.get('https://viacep.com.br/ws/{}/json'.format(cep)).json()

# print(response)
# print(response.status_code)
# print(response.text)
# print(response.json())

# data = response.json()


data = return_cep_data('01001000')
print(data['logradouro'])
print(data['localidade'])


def return_html(url):
    response = requests.get(url)
    return response.text


print(return_html('https://google.com'))

# python virtual environments are used to separate project libraries
