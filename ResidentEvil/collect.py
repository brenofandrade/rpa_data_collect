
from tqdm import tqdm
from utils import *
import pandas as pd

def main():
    # Obtem os links
    links = get_links()

    # Obtem os dados para cada link na lista
    data = []
    for i in tqdm(links, total=len(links)):
        d = get_personagem_infos(i)
        d["Link"] = i
        nome = i.strip("/").split("/")[-1].replace("-", " ").title()
        d["Nome"] = nome
        data.append(d)

    # Cria uma estrutura de dados em formato tabular (Dataframe)
    df_personagens = pd.DataFrame(data)

    # Salva os dados em Disco
    df_personagens.to_csv("dados_residentevil.csv", index=False)
    df_personagens.to_parquet("dados_residentevil.parquet", index=False)
    df_personagens.to_pickle("dados_residentevil.pkl")

if __name__ == "__main__":
    main()