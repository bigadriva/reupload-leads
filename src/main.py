import pandas as pd

from elasticsearch import Elasticsearch

# def baixar_base_antiga():
#     server = ['http://elastic.datadriva.com']
#     auth = ('elastic', 'BvfrG2NHXFa9qm')
#     with Elasticsearch(server, http_auth=auth) as elastic:
#         results = elastic.search(
#             index='totvs-curitiba-base',

#         )


# def concatenar_bases():


# def remover_cnpjs_repetidos():


# def fazer_upload():


def main():
    df1 = pd.read_csv('data/lista1.csv', dtype=str)
    df2 = pd.read_csv('data/lista2.csv', delimiter=';', dtype=str)

    print(df1.head())
    print(df2.head())
    pd.concat([df1, df2]) \
        .drop_duplicates(subset=['cnpj']) \
        .replace('(empty)', '') \
        .to_csv('data/leads.csv', sep=';', index=False)

    

if __name__ == '__main__':
    main()
