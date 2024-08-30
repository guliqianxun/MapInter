import json
import geopandas as gpd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, CustomJS, TapTool

# Load the GeoJSON file
gdf = gpd.read_file('china_provinces.geojson')

# Initialize a fill_color column in the GeoDataFrame
gdf['fill_color'] = 'lightblue'

# Convert GeoDataFrame to JSON, including the fill_color column
gdf_json = json.loads(gdf.to_json())
geo_source = GeoJSONDataSource(geojson=json.dumps(gdf_json))

# Create a Bokeh figure
p = figure(title="中国省级区域高亮", tools="tap", x_axis_location=None, y_axis_location=None,
           width=800, height=600)

# Remove grid lines
p.grid.grid_line_color = None

# Draw patches (provinces) with fill_color based on the GeoDataFrame
p.patches('xs', 'ys', source=geo_source, fill_alpha=0.7, line_color="black", line_width=0.5,
          fill_color={'field': 'fill_color'})

# Custom JavaScript callback to highlight selected province
callback = CustomJS(args=dict(source=geo_source), code="""
    const selected_indices = cb_obj.indices;
    const data = source.data;
    
    // Reset all fill colors to lightblue
    for (let i = 0; i < data['fill_color'].length; i++) {
        data['fill_color'][i] = 'lightblue';
    }
    
    // Highlight selected province
    for (let i = 0; i < selected_indices.length; i++) {
        data['fill_color'][selected_indices[i]] = 'yellow';
    }
    
    source.change.emit();
""")

# Set up the tap tool with the callback
tap_tool = TapTool()
tap_tool.callback = callback
p.add_tools(tap_tool)

# Output file
output_file("china_province_highlight.html")

# Show the plot
show(p)
