import pandas as pd
import time as time
from sqlalchemy import create_engine

path = "data\yellow_tripdata_2021-01.csv"
database_type = "postgresql"
credential = "user"
hostport = "5433"
database_name = "NY_taxy"


def data_ingestor(path, database_type, credential, hostport, database_name):
    """
    df param: takes a datanase object 
    """
    # Setting up the postgresql engine to fascilitate database ingestion
    engine  = create_engine(f"{database_type}://{credential}:{credential}@localhost{hostport}/{database_name}")

    df_iter = pd.read_csv(f"{path}", iterator=True, chunksize=100000)


    while True:
        time_start = time()
        
        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        # Checks whether the column names allready 
        df.head(n = 0).to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")

        # If data allready exists append new rows.
        df.to_sql(name="yellow_taxi_data", con=engine, if_exists="append") 
        time_end = time()

        print(f"Data chunk is inserted in the {database_type} called {database_name}... it took %3.f seconds" % (time_end - time_start))


data_ingestor(path=path, database_type=database_type, credential=credential, hostport=hostport, database_name=database_name)
