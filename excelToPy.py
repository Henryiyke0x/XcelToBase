import pandas as pd
# from sqlalchemy import text
import sqlalchemy as sa

# Read Excel data into a Pandas DataFrame
excel_data = pd.read_excel('added.xlsx')

connection_url = sa.engine.URL.create(
    "mysql+mysqlconnector",
    username="ExelToSql",
    password="@Excel1010",
    host='localhost',
    database="sch_data"
)
# Establish database connection using SQLAlchemy engine
engine = sa.create_engine(connection_url)

#  Create table if it doesn't exist
table_schema = f"""
CREATE TABLE IF NOT EXISTS rt_table (
    {', '.join(f'{col} TEXT' for col in excel_data.columns)}
)
"""

with engine.connect() as connection:
    connection.execute(sa.text(table_schema))

# Insert data into the table
excel_data.to_sql('rt_table', con=engine, if_exists='replace', index=False)

# Display success message
print("Data imported successfully into the database!")
