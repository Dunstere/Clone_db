import geopandas as gpd
from sqlalchemy import create_engine

SHAPEFILE = "../data/clima_5000.shp"

DB1 = "postgresql://postgres:postgres@localhost:5432/gisdb1"

TABLE_NAME = "regions"

print("Lendo shapefile...")

gdf = gpd.read_file(SHAPEFILE)

gdf = gdf.set_crs(epsg=4674, inplace=True, allow_override=True)

epsg = gdf.crs.to_epsg()
print(f"CRS do GeoDataFrame: EPSG:{epsg}")

engine = create_engine(DB1)

print("Inserindo no PostGIS...")

gdf.to_postgis(
    TABLE_NAME,
    engine,
    if_exists="replace",
    index=False
)

print("Tabela criada com sucesso.")