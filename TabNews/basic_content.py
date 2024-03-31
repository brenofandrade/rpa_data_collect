# %%
import requests
import pandas as pd
import datetime
import json
import os
import time
import random

# path_json = "/data/contents/json/"


# if not os.path.exists(path_json):
#     print("diretorio criado")
#     os.makedirs(path_json)

def get_response(**kwargs):
    url = "https://www.tabnews.com.br/api/v1/contents"
    response = requests.get(url, params=kwargs)
    return response


def save_data(data, option='json', current_time=None):
    if not current_time:
        current_time = datetime.datetime.now()
    match option:
        case 'json':
            with open(f"data/contents/json/{current_time}.json", "w") as open_file:
                json.dump(data, open_file, indent=4)

        case 'dataframe':
            df = pd.DataFrame(data)
            df.to_parquet(f"data/contents/parquet/{now}.parquet", index=False)
        
        case '_':
            print("Nada para salvar")


# %%
page = 1
while True:
    now = datetime.datetime.now().strftime("%Y%m%d_%H%m%S%f")
    print(page)
    
    response = get_response(page=page, per_page=100, strategy="new")
    if response.status_code == 200:
        data = response.json()
        save_data(data, option='json', current_time=now)
        
        if len(data) < 100:
            break
        
        page += 1
        time.sleep(random.randint(3,7))
        
    else:
        print("Status code: ", response.status_code)
        time.sleep(10)

    

# # %%
# url = "https://www.tabnews.com.br/api/v1/contents"

# response = requests.get(url)
# response.status_code
# # %%
# response.text
# # %%
# response.json()
# # %%
# data = response.json()
# # %%
# type(data)
# # %%
# data[0]
# # %%
# data[1]
# # %%
# len(data)
# # %%
# url = "https://www.tabnews.com.br/api/v1/contents/?page=1&per_page=100&strategy=new"


# # %%



# # %%
# data = get_response(page=1, per_page=100, strategy="new").json()
# data
# # %%
# len(data)
# # %%
# df = pd.DataFrame(data)
# df
# # %%
# response = get_response(page=1, per_page=100, strategy="new")
# data = response.json()

    
# # %%
# print(len(data))
# print(type(data))
# print(data[0])
# # %%
# save_data(data, option='json')
# # %%

# %%
