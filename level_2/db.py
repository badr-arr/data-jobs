import sqlite3
from sqlite3 import Error
import pandas as pd


class DB:

    def __init__(self, database):
        self.myCon = sqlite3.connect(database)
        self.cur = self.myCon.cursor()

    def execute_query(self, query) -> None:
        """
        Execute string query
        :param query:
        :return:
        """
        try:
            self.cur.execute(query)
        except Error as e:
            print(e)

    def insert_dataframe_into_table(self, table_name: str, df: pd.DataFrame) -> None:
        """
        Insert dataframe table into table
        :param table_name:
        :param df:
        :return: None
        """
        df.to_sql(con=self.myCon, name=table_name, if_exists='replace', index=False)

    def select_all(self, table_name) -> None:
        """
        Perform a select query on given table and print rows
        :param table_name:
        :return:
        """
        self.cur.execute(f"SELECT * FROM {table_name}")

        rows = self.cur.fetchall()

        for row in rows:
            print(row)
