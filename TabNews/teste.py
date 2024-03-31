
import requests
import pandas as pd
import datetime
import json
import os

# path_json = "/data/contents/json/"

# if not os.path.exists(path_json):
#     print("diretorio criado")
#     os.makedirs(path_json)

def get_response(**kwargs):
    url = "https://www.tabnews.com.br/api/v1/contents"
    response = requests.get(url, params=kwargs)
    return response

now = datetime.datetime.now().strftime("%Y%m%d%H%m")
def save_data(data, option='json'):
    match option:
        case 'json':
            with open(f"data/contents/json/{now}", "w") as open_file:
                json.dump(data, open_file, indent=4)

        case 'dataframe':
            df = pd.DataFrame(data)
            df.to_parquet(f"data/contents/parquet/{now}.parquet", index=False)
        
        case '_':
            print("Nada para salvar")


if __name__ == "__main__":
    
    response = get_response(page=1, per_page=100, strategy="new")
    data = response.json()

    save_data(data, option='json')