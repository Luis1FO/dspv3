# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output
import dash_html_components as html
from app import app
import data

# Importar los datos de los archivos data.py
data_plan = data.plandata
data_cod = data.coddata
data_cons = data.consdata
data_pru = data.prudata
lan_data = data.landata
dsp_data = data.dspdata
op_data = data.opdata
mon_data = data.mondata

# Callback para mostrar las propiedades de la tabla
@app.callback(
    Output('output', 'children'),
    [Input('table', 'cols'),
     Input('table', 'rows'),
     Input('table', 'rowOrder'),
     Input('table', 'colOrder'),
     Input('table', 'aggregatorName'),
     Input('table', 'rendererName')],
    prevent_initial_call=True
)
def display_table_properties(cols, rows, row_order, col_order, aggregator, renderer):
    # Formatear las propiedades de la tabla para mostrarlas en el HTML
    table_properties = [
        html.P(f'Columnas: {cols}'),
        html.P(f'Filas: {rows}'),
        html.P(f'Orden de Filas: {row_order}'),
        html.P(f'Orden de Columnas: {col_order}'),
        html.P(f'Agregador: {aggregator}'),
        html.P(f'Renderizador: {renderer}')
    ]
    return table_properties



