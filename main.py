import sys
import json
import datetime
import traceback
from configparser import ConfigParser
from cryptography.fernet import Fernet


# instantiate config Parser

config = ConfigParser()

def main(configPath):
    try:
        #key = Fernet.generate_key()
        #print(key)
        key = b'jhj1m0i98bMghl4jCk57hmMuW4fdvFv--S1SSmsCijE='
        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword")  # required to be bytes
        print(ciphered_text)

        ciphered_text = b'gAAAAABhsOdnGpEEm0fcdUO7cDdmwhnvW-q99Nm8-xY1-bsQBljnS9QZWqzPzJOr7oMWhUkd3j8XlIPMWhqCmH_aRQbqPiTwcFCf0rsTYNSQ1Pyty8IELc4='
        unciphered_text = (cipher_suite.decrypt(ciphered_text))
        print(unciphered_text.decode("utf-8"))
        config.read(configPath)
        print("Starting kafka consumer with following details::")
        host = config['mysql']['host']
        user = config['mysql']['user']
        passwd = config['mysql']['passwd']
        db = config['mysql']['db']

        print('MySQL configuration:')

        print(f'Host: {host}')
        print(f'User: {user}')
        print(f'Password: {passwd}')
        print(f'Database: {db}')

        host2 = config['postgresql']['host']
        user2 = config['postgresql']['user']
        passwd2 = config['postgresql']['passwd']
        db2 = config['postgresql']['db']

        print('PostgreSQL configuration:')

        print(f'Host: {host2}')
        print(f'User: {user2}')
        print(f'Password: {passwd2}')
        print(f'Database: {db2}')



    except Exception as e:
        print(str(datetime.datetime.now()) + "____________ Exception occurred in main() ________________")
        print("Exception::msg %s" % str(e))
        print(traceback.format_exc())


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main('config.cnf')
