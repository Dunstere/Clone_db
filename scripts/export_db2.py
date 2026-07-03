import geopandas as gpd
from sqlalchemy import create_engine

DB2 = "postgresql://postgres:postgres@localhost:5433/gisdb2"
TABLE = "regions"

OUTPUT_FILE = "../data/exported_regions.gpkg"

print("Conectando ao Banco de Dados 2...")
engine_db2 = create_engine(DB2) 

sql = f"""
SELECT *
FROM {TABLE}
"""

print(f"Exportando dados da tabela '{TABLE}' ...")

gdf = gpd.read_postgis(
    sql,
    con=engine_db2,
    geom_col="geometry"
)

print(f"{len(gdf)} registros prontos para exportação.")
print(f"Salvando arquivo em: {OUTPUT_FILE} ...")

gdf.to_file(
    OUTPUT_FILE,
    driver="GPKG",
    index=False
)

print("Exportação concluída com sucesso!")