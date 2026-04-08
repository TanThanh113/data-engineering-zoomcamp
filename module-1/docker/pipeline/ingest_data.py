import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

year = 2021
month = 1

@click.command()
@click.option('--pg-user', default='thanh123', help = "PostgreSQL User")
@click.option('--pg-pass', default='1234', help = "PostgreSQL Password")
@click.option('--pg-host', default='localhost', help = "PostgreSQL Host")
@click.option('--pg-port', default='5433', help = "PostgreSQL Port")
@click.option('--pg-db', default='ny_taxi', help = "PostgreSQL Database Name")
@click.option('--target-table', default='yellow_taxi_date', help = "Target Table Name")
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):
    engine_url = f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
    engine = create_engine(engine_url)

    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"
    url = f"{prefix}yellow_tripdata_{year}-{month:02d}.csv.gz"

    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64"
    }

    parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
    ]

    print(f"Đang tải dữ liệu từ: {url}...")
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100000
    )
    try:
        first_chunk = next(df_iter)
    except StopIteration:
        print("File CSV trống!")
        return

    first_chunk.head(0).to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="replace"
    )
    print("Table created")
    first_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )
    print("Inserted first chunk:", len(first_chunk))
    for df_chunk in tqdm(df_iter):
        df_chunk.to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="append"
        )
        print("Inserted chunk:", len(df_chunk))

    print("Completed!!")

if __name__ == '__main__':
    run()