HOST = '150.158.179.56'
PORT = '3306'
USERNAME = '2i_test_3'
PASSWORD = 'nxb2022'
DATABASE = '2i_test_3'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SECRET_KEY = 'ABC'

