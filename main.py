import sys
import json
import datetime
import traceback
from configparser import ConfigParser
import rsa
# instantiate config Parser
config = ConfigParser()

def main(configPath):
    try:
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

        # generate public and private keys with
        # rsa.newkeys method,this method accepts
        # key length as its parameter
        # key length should be atleast 16
        publicKey, privateKey = rsa.newkeys(512)
        print("private key:",privateKey)
        print("public key:" , publicKey)

        # this is the string that we will be encrypting
        message = "deva@123"

        # rsa.encrypt method is used to encrypt
        # string with public key string should be
        # encode to byte string before encryption
        # with encode method
        encMessage = rsa.encrypt(message.encode(),
                                 publicKey)

        print("original string: ", message)
        print("encrypted string: ", encMessage)

        # the encrypted message can be decrypted
        # with ras.decrypt method and private key
        # decrypt method returns encoded byte string,
        # use decode method to convert it to string
        # public key cannot be used for decryption

        decMessage = rsa.decrypt(encMessage, privateKey).decode()

        print("decrypted string: ", decMessage)
    except Exception as e:
        print(str(datetime.datetime.now()) + "____________ Exception occurred in main() ________________")
        print("Exception::msg %s" % str(e))
        print(traceback.format_exc())


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main('config.cnf')
