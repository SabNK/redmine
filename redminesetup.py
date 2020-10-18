import os
import json

REDMINE_SETUP_FILE = os.path.abspath('./res/setup.json')
with open(REDMINE_SETUP_FILE, 'r', encoding='utf-8') as task:
    setup_dict = json.load(task)
API_KEY = setup_dict['api_key']
REDMINE_URL = setup_dict['url']
VERSION = setup_dict['version']
# TODO practice generator
'''CREDENTIALS_FILE = os.path.abspath('../res/' + setup_dict['google_credentials_file'])  # имя файла с закрытым ключом
REPORT_SPREADSHEET_ID = setup_dict['report_spreadsheet_id']
REPORT_SHEET_ID = setup_dict['report_sheet_id']
DATA_LINE = 4
PROJECT_COLUMN = 1
weeks_in_RP = [9, 10, 11, 12, 13, 14]'''