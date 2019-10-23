from google.cloud import bigquery
from google.api_core.exceptions import NotFound

client = bigquery.Client()

DATASET_NAME = "google_budget_sandbox"
TABLE_NAME = "placeholders"

schema = [
    bigquery.SchemaField("fiscal_year", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("quarter", "STRING", mode="REQUIRED"),
]


def insert_data():
    table = get_table()

    data = [(2027, 'Q4')]
    errors = client.insert_rows(table, data)

    if len(errors):
        print(errors)
    else:
        print("Great success!!!")


def get_table():
    try:
        dataset = bigquery.Dataset(client.dataset(DATASET_NAME))
        table_ref = bigquery.Table(dataset.table(TABLE_NAME))
        return client.get_table(table_ref)

    except NotFound:
        return create_structure()


def create_structure():
    dataset = client.create_dataset(DATASET_NAME)
    table_ref = bigquery.Table(dataset.table(TABLE_NAME), schema)
    table_created = client.create_table(table_ref)

    return client.get_table(table_created)


if __name__ == '__main__':
    insert_data()
