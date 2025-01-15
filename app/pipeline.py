import os
import pandas as pd
import time as t
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import create_database, database_exists

path = "data/yellow_tripdata_2021-01.csv"

def data_ingestor(path):
    """
    Ingests CSV data into PostgreSQL database in chunks.
    
    Args:
        path (str): Path to the CSV file
    """
    try:
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            raise ValueError("DATABASE_URL environment variable is not set")
            
        # Create database if it doesn't exist
        engine = create_engine(database_url)
        if not database_exists(engine.url):
            create_database(engine.url)
            print("Created database")
        
        # Create iterator for the CSV file
        df_iter = pd.read_csv(path, iterator=True, chunksize=100000)
        
        # Get the first chunk
        df = next(df_iter)
        
        # Convert datetime columns
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        # Create table with first chunk
        df.head(n=0).to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")
        
        # Insert first chunk
        time_start = t.time()
        df.to_sql(name="yellow_taxi_data", con=engine, if_exists="append")
        time_end = t.time()
        print(f"First chunk ingested... took {time_end - time_start:.2f} seconds")
        
        # Process remaining chunks
        while True:
            try:
                time_start = t.time()
                df = next(df_iter)
                
                df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
                df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
                
                df.to_sql(name="yellow_taxi_data", con=engine, if_exists="append")
                
                time_end = t.time()
                print(f"Chunk ingested... took {time_end - time_start:.2f} seconds")
                
            except StopIteration:
                print("Finished ingesting all the data")
                break
                
    except SQLAlchemyError as e:
        print(f"Database error occurred: {str(e)}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    data_ingestor(path)