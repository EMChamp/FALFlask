from sqlalchemy import create_engine, MetaData, Table

class database_helpers(object):

    def __init__(self):
        self.engine = create_engine('mssql://127.0.0.1/tft_fantasy', convert_unicode=True)
        self.metadata = MetaData(bind=self.engine)
        return

    def return_challenger_league(self):
        users = Table('challenger_league', self.metadata, autoload=True)
        return users