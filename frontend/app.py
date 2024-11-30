# """This script initializes a Dash application by importing and setting a layout from the layout module. It then registers the necessary callbacks for the app using the register_callbacks function from the callbacks module. Finally, it runs the app in debug mode, allowing for live updates and error tracking during development."""

# # frontend/app.py
from dash import Dash
from layout import layout
from callbacks import register_callbacks

# Initialize Dash app
app = Dash(__name__)
app.layout = layout

# Register callbacks
register_callbacks(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)




# # frontend/app.py

# import sys
# print(sys.executable)
# from dash import Dash
# from dash import dash_bootstrap_components as dbc
# from layout import layout
# from callbacks import register_callbacks

# # Initialize Dash app with Bootstrap theme
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.layout = layout

# # Register callbacks
# register_callbacks(app)

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)
