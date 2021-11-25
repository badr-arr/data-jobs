import os
from db import DB
from ..lib.communication_parsor import get_communications_df


def main() -> None:
    """
    Insert json file into communication table
    :return:
    """
    sql_query = """
    CREATE TABLE IF NOT EXISTS communication(
    id text primary key,
    telecom text,
    created_at timestamp,
    sender_name text,
    sender_category text
    )
    """
    input_folder = "./processed"
    table_name = "communication"
    json_files_list = [f for f in os.listdir(input_folder) if f.endswith('.json')]

    database = DB("test")
    database.execute_query(query=sql_query)
    communications_df = get_communications_df(json_files_list, input_folder)
    database.insert_dataframe_into_table(table_name=table_name, df=communications_df)
    database.select_all(table_name=table_name)


if __name__ == "__main__":
    main()
