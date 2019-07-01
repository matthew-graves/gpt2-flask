import gpt_mysql_connector

db_available = gpt_mysql_connector.test_connection()
if db_available:
    guid = gpt_mysql_connector.insert_gpt_prompt('prompt', 'text')
    response = (gpt_mysql_connector.get_gpt_prompt(guid))
    print(response)
