import ast
import os
import json

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
        resulted_json['sender']['category'] = resulted_json['sender'].get('profession', None)
        del resulted_json['sender']['profession']

    return resulted_json


def get_communications_df(json_files_list: list, input_folder: str) -> pd.DataFrame:
    """

    :param json_files_list:
    :param input_folder:
    :return:
    """
    communications = []
    for f in json_files_list:
        input_file = os.path.join(input_folder, f)

        opened_file = open(input_file)
        data = json.load(opened_file)

        if data.get('sender', None):
            data['sender_name'] = data['sender'].get('name', None)
            data['sender_category'] = data['sender'].get('category', None)

        del data['sender']

        communications.append(data)

    communications_df = pd.DataFrame(communications)
    communications_df['created_at'] = pd.to_datetime(
        communications_df['created_at'], format= '%Y-%m-%d %H:%M:%S')

    return communications_df
