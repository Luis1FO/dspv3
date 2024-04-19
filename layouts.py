# -*- coding: utf-8 -*-
# Dash components, html, and dash tables
from dash import html
# Import components PivotTable
import dash_pivottable
## Import custom data.py
import data
## Import data from data.py file

data_plan = data.plandata
data_cod=data.coddata
data_cons=data.consdata
data_pru=data.prudata
lan_data=data.landata
dsp_data=data.dspdata
op_data=data.opdata
mon_data=data.mondata

# Layout for proces DevOps
#vista planeacion
planLayout = html.Div([
dash_pivottable.PivotTable(
id='table',
data=data_plan,
#datos en el eje x
cols=['id_proyecto'],
# colOrder="key_a_to_z",
#Datos que se muestran para filtrar aqui podria ser nombre proyecto 
rows=['faseDevOps'],
#orden de los datos
rowOrder="key_a_to_z",
#rendererName="Stacked Column Chart",
rendererName="Dot Chart",
aggregatorName="Sum",
#Datos que se muestran en las barras aqui podria ser metricas
vals=['PuntosH'],
#atributos para omitir de los men�s desplegables
hiddenFromAggregators=["nombre_proyecto","PuntosH","fechaInicio","fechaFin","entregable","responsable"],
), 
html.Div(      
id='output'
)
]
)
#vista codificacion
codLayout = html.Div([
dash_pivottable.PivotTable(
id='table',
data=data_cod,
#datos en el eje x
cols=['id_proyecto'],
# colOrder="key_a_to_z",
#Datos que se muestran para filtrar aqui podria ser nombre proyecto 
rows=['faseDevOps'],
#orden de los datos
rowOrder="key_a_to_z",
rendererName="Dot Chart",
aggregatorName="Sum",
#Datos que se muestran en las barras aqui podria ser metricas
vals=["Defectos"],
#atributos para omitir de la interfaz de usuario
hiddenAttributes=["entregable"],
),
html.Div(
id='output'
)
])
#vista compilacion
consLayout = html.Div([
dash_pivottable.PivotTable(
id='table',
data=data_cons,
#datos en el eje x
cols=['id_proyecto'],
# colOrder="key_a_to_z",
#Datos que se muestran para filtrar aqui podria ser nombre proyecto 
rows=['faseDevOps'],
#orden de los datos
rowOrder="key_a_to_z",
rendererName="Dot Chart",
aggregatorName="Sum",
#Datos que se muestran en las barras aqui podria ser metricas
vals=["CompilacionExitosa"],
#atributos para omitir de la interfaz de usuario
hiddenAttributes=["entregable"],
hiddenFromAggregators=["descripcion","fechaIni","fechaFin","observaciones","entregable","responsable"],
),
html.Div( 
id='output'
)
])
#Pruebas
pruLayout = html.Div([
dash_pivottable.PivotTable(
id='table',
data=data_pru,
#datos en el eje x
#cols=['fecha','faseDevOps'],
cols=['id_proyecto'],
colOrder="key_a_to_z",
#Datos que se muestran para filtrar aqui podria ser nombre proyecto 
rows=['faseDevOps',"fecha"],
#orden de los datos
rowOrder="key_a_to_z",
rendererName="Stacked Bar Chart",
aggregatorName="Sum",
#Datos que se muestran en las barras aqui podria ser metricas
vals=["PruebasExitosa"],
#atributos para omitir de la interfaz de usuario
hiddenAttributes=["entregable"],
hiddenFromAggregators=["descripcion","fechaFin","observaciones","entregable","responsable"],
),
html.Div(
id='output'
)
])
#Lanzamiento
lanLayout = html.Div([
dash_pivottable.PivotTable(
id='table',
data=lan_data,
#datos en el eje x
#cols=['faseDevOps'],
#colOrder="key_a_to_z",
#Datos que se muestran para filtrar aqui podria ser nombre proyecto 
rows=['id_proyecto','NumLan'],
#orden de los datos
rowOrder="key_a_to_z",
rendererName="Grouped Column Chart",
aggregatorName="Sum",
#Datos que se muestran en las barras aqui podria ser metricas
vals=['Horas'],
#atributos para omitir de los men�s desplegables
hiddenFromAggregators=["descripcion","observaciones","entregable","responsable"],
), 
html.Div(      
id='output'
)
]
)
#Despliegue
dspLayout = html.Div([
dash_pivottable.PivotTable(
id='table',
data=dsp_data,
#datos en el eje x
cols=['id_proyecto'],
# colOrder="key_a_to_z",
#Datos que se muestran para filtrar aqui podria ser nombre proyecto 
rows=['fechaIni','fechaFin'],
#orden de los datos
rowOrder="key_a_to_z",
rendererName="Dot Chart",
aggregatorName="Sum",
#Datos que se muestran en las barras aqui podria ser metricas "","",
vals=['NumDespli'],
#atributos para omitir de los men�s desplegables
hiddenFromAggregators=["descripcion","observaciones","entregable","responsable"],
),
html.Div(
id='output'
)
])
#operacion
opLayout = html.Div([
dash_pivottable.PivotTable(
id='table',
data=op_data,
#datos en el eje x
#cols=['TiempoDet'],
# colOrder="key_a_to_z",
#Datos que se muestran para filtrar aqui podria ser nombre proyecto 
rows=['Errores','id_proyecto'],
#orden de los datos
rowOrder="key_a_to_z",
rendererName="Grouped Column Chart",
aggregatorName="Median",
#Datos que se muestran en las barras aqui podria ser metricas "","",
vals=['TiempoDet','Errores'],
#atributos para omitir de los men�s desplegables
hiddenFromAggregators=["descripcion","observaciones","entregable","responsable"],
),
html.Div(
id='output'
)
])
#monitoreo

monLayout = html.Div([
html.H1("Dynamically rendered tab content"),
dash_pivottable.PivotTable(
id='table',
data=mon_data,
#datos en el eje x
cols=['id_proyecto'],
# colOrder="key_a_to_z",
#Datos que se muestran para filtrar aqui podria ser nombre proyecto 
rows=['Recu'],
#orden de los datos
rowOrder="key_a_to_z",
rendererName="Dot Chart",
aggregatorName="Sum",
#Datos que se muestran en las barras aqui podria ser metricas
vals=['TiempoRec', 'Recu'],
#omitir de la parte de arrastrar y soltar
hiddenFromDragDrop=[],
#atributos para omitir de la interfaz de usuario
hiddenAttributes=[],
#atributos para omitir de los men�s desplegables
hiddenFromAggregators=[],
),
html.Div(
id='output' 
)
])
