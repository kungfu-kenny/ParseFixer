import os
import json
import requests
from config import (
    LINK, 
    API_KEY,
    file_use_results,
    folder_use_storage
)


def check_presence_file(path_file:str) -> bool:
    """
    Function to check file presence
    Input:  path_file = path to the selected 
    Output: boolean for all of it
    """
    return os.path.exists(path_file) and os.path.isfile(path_file)

def check_presence_folder(path_folder:str) -> None:
    """
    Function which is deducated to develop the folder presence
    Input:  path_folder = path to it
    Output: we developed folder
    """
    (os.path.exists(path_folder) and os.path.isdir(path_folder)) or os.mkdir(path_folder)

def develop_request() -> dict:
    """
    Function to develop request and get selected values
    Input:  None
    Output: dictionary with the selected values
    """
    try:
        return json.loads(
            requests.get(
                LINK, 
                params={
                    "access_key": API_KEY
                }
            ).text
        )
    except Exception as e:
        print('We found problem with the getting data, error:', e)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        return {}

def develop_file(value_dict:dict={}) -> None:
    """
    Function which is dedicated to develop the file
    Input:  value_dict = dictionary value of captured value
    Output: we developed file of the getting values
    """
    if check_presence_file(file_use_results):
        with open(file_use_results, 'r') as previously:
            value_list = json.load(previously)
        value_list.append(value_dict)
    else:
        value_list = [value_dict]
    with open(file_use_results, 'w') as current:
        json.dump(
            value_list, 
            current,
            indent=4
        )

def develop_main() -> None:
    """
    Function which is dedicated to develop the all values
    """
    check_presence_folder(folder_use_storage)
    value_used = develop_request()
    if value_used:
        develop_file(value_used)
    

if __name__ == '__main__':
    develop_main()