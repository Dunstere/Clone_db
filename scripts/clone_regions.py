import geopandas as gpd
from sqlalchemy import create_engine

DB1 = "postgresql://postgres:postgres@localhost:5432/gisdb1"
DB2 = "postgresql://postgres:postgres@localhost:5433/gisdb2"

TABLE = "regions"

print("Conectando DB1...")

engine_db1 = create_engine(DB1)

sql = f"""
SELECT *
FROM {TABLE}
"""

gdf = gpd.read_postgis(
    sql,
    engine_db1,
    geom_col="geometry"
)

print(f"{len(gdf)} registros encontrados.")

print("Conectando DB2...")

engine_db2 = create_engine(DB2)

gdf.to_postgis(
    TABLE,
    engine_db2,
    if_exists="replace",
    index=False
)

print("Transferência concluída.")