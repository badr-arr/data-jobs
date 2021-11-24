import ast

FIRST_ELEMENT = 0
LAST_ELEMENT = -1

def parse_string(file_content: str) -> dict:
    """

    :param file_content:
    :return:
    """
    splited_content = file_content.split('|')
    resulted_json = {
        elmt.split('=')[FIRST_ELEMENT]: elmt.split('=')[LAST_ELEMENT] for elmt in splited_content
    }
    if resulted_json.get('sender', None):
        resulted_json['sender'] = ast.literal_eval(resulted_json['sender'])

    return resulted_json
