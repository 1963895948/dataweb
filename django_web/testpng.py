from aip import AipOcr
# 百度api接口，读取图片文字

APP_ID = '20401822'
API_KEY = 'pzLvqEQplOKnCtGjBm7jUOHv'
SECRET_KEY = 'lW65AdMwiNKORMrlVN5XBeYIPlj8ZLS8'


client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])
