import sqlite3
from sqlite3 import Error
import pandas as pd


class DB:

    def __init__(self, database):
        self.myCon = sqlite3.connect(database)
        self.cur = self.myCon.cursor()

    def create_table(self, create_table_sql):
        try:
            self.cur.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_dataframe_into_table(self, table_name: str, df: pd.DataFrame) -> None:
        """

        :param table_name:
        :param df:
        :return:
        """
        df.to_sql(con=self.myCon, name=table_name, if_exists='replace', index=False)

    def select_all_communications(self, table_name):
        """

        :param table_name:
        :return:
        """
        self.cur.execute(f"SELECT * FROM {table_name}")

        rows = self.cur.fetchall()

        for row in rows:
            print(row)
