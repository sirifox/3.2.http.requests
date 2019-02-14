import requests
import os


def translate(way_text, way_result, lang_first, lang_sec='ru'):

    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    lang = lang_first + '-' + lang_sec
    params = {'lang': lang, 'srv': 'tr-text', 'id': 'f5c948f1.5c59b9e9.16d39b90-6-0',
              'key': 'trnsl.1.1.20190210T165957Z.213a8d8cc9ee59bf.316e87145b5e5bf90130e772fba39bc568290b4a'}
    write_list = []
    with open(way_text, encoding='utf-8') as f:
        for line in f:
            data = {'text': line}
            resp = requests.post(URL, data=data, params=params)
            write_list.append(resp.json()['text'][0])

    write_str = ''.join(write_list)
    with open(way_result, 'w', encoding='utf-8') as f_r:
        f_r.write(write_str)

    return 'Перевод осуществлён'


print(translate(os.path.join('3.2.http.requests', 'DE.txt'),
                os.path.join('3.2.http.requests', 'DE_RU.txt'),
                'de'))
print(translate(os.path.join('3.2.http.requests', 'FR.txt'),
                os.path.join('3.2.http.requests', 'FR_RU.txt'),
                'fr'))
print(translate(os.path.join('3.2.http.requests', 'ES.txt)',
                os.path.join('3.2.http.requests', 'ES_RU.txt)',
                'es'))
