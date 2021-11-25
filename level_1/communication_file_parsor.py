#!/usr/bin/env python3
"""
Script used to generate 1000 random communication.
"""
import os
import json

from ..lib.communication_parsor import parse_string


def main() -> None:
    """
    Main function to store parsed files into processed dir
    :return: None
    """
    input_folder = "./communications"
    output_folder = "./processed"
    json_files_list = [f for f in os.listdir(input_folder) if f.endswith('.json')]

    for f in json_files_list:
        input_file = os.path.join(input_folder, f)

        opened_file = open(input_file)
        data = opened_file.read()

        resulted_dict = parse_string(data)

        output_file = os.path.join(output_folder, f)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, "w") as file:
            json.dump(resulted_dict, file, sort_keys=True, indent=4)


if __name__ == "__main__":
    main()
