import geopandas as gpd

# 加载 Shapefile 数据
gdf = gpd.read_file("ne_50m_admin_1_states_provinces.shp")

# 过滤出中国的省级区域
china_gdf = gdf[gdf['admin'] == 'China']

# 将数据保存为 GeoJSON 文件
china_gdf.to_file("china_provinces.geojson", driver="GeoJSON")
