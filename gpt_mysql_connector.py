import mysql.connector
from flask import Flask
import yaml
import random

app = Flask(__name__)

with open('configs/connections.yaml') as ymlfile:
    cfg = yaml.load(ymlfile, Loader = yaml.SafeLoader)


if cfg['usemysql']:
    try:
        gptdb = mysql.connector.connect(
            host = cfg['mysql']['host'],
            user = cfg['mysql']['user'],
            passwd = cfg['mysql']['password'],
            database = cfg['mysql']['dbname']
        )
        print('Database Available')
        available = True
    except Exception as e:
        print("An error occurred during connection:", e)
        available = False

def is_connected():
    try:
        return gptdb.is_connected()
    except:
        return False


def test_connection():
    if cfg['usemysql']:
        if available:
            gptcursor = gptdb.cursor()
            try:
                gptcursor.execute("SELECT * FROM archive LIMIT 1")
                gptcursor.fetchall()
                return "Database Available"
            except Exception as e:
                print ("Exception occurred:", e)
                return None
        else:
            return None


def insert_gpt_prompt(prompt, text):
    if cfg['usemysql']:
        if available:
            gptcursor = gptdb.cursor()

            salt = str(random.randint(1,1000000))
            hash_val = hash(prompt + salt)
            hash_val = abs(hash_val)
            guid = format(hash_val, 'x')

            insert_query = "INSERT INTO archive (guid, prompt, response) VALUES (%s, %s, %s)"
            vars = (guid, prompt, text)
            try:
                gptcursor.execute(insert_query, vars)
                gptdb.commit()
                return guid, True
            except Exception as e:
                print("An error occured during insert:", e)
                return None, None


def get_gpt_prompt(guid):
    if cfg['usemysql']:
        if available:
            gptcursor = gptdb.cursor()
            select_query = "SELECT prompt, response FROM archive WHERE guid = %s"
            guid_s = (guid, )
            try:
                gptcursor.execute(select_query, guid_s)
                text = gptcursor.fetchone()
                if (text):
                    return text[0], True
                else:
                    return "Entry Not Found", True
            except Exception as e:
                print("Exception occurred:", e)
                return "Database Error Has Occured!", None