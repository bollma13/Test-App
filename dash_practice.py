#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:36:23 2021

@author: sambollman
"""

import dash 
import dash_html_components as html
import dash_core_components as dcc


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    children=[html.H1(children='Sample web app'),
    html.Div(children = '''Graph examples'''),
    dcc.Graph(id='dash_graph',
              figure = {'data': [{'x':[1,2,3,4,5,6,7,8,9,10,11,12], 'y':[30,33,44,58,69,78,83,81,73,60,47,35], 'type':'bar', 'name': 'High'},
                                 {'x':[1,2,3,4,5,6,7,8,9,10,11,12], 'y':[15,16,25,36,46,56,60,58,50,40,31,21], 'type':'bar', 'name': 'Low'},
                                 {'x':[1,2,3,4,5,6,7,8,9,10,11,12], 'y':[(30+15)/2, (33+16)/2, (44+25)/2,(58+36)/2,(69+46)/2,(78+56)/2,(83+60)/2,(81+58)/2,(73+50)/2,(60+40)/2,(47+31)/2,(35+21)/2], 'type':'line', 'name': 'Average'},],
                        'layout':{'title':'Lansing Temperatures',
                                  'xaxis':{'title':"Month", 'linecolor':"black"}, 
                                  'yaxis':{'title':"Temperature(F)", 'linecolor':"black"},
                                  'paper_bgcolor':'#cccedb',
                                  'plot_bgcolor':'ededed'}
    }),
    
    dcc.Graph(id='Graph2',
              figure = {'data': [{'x':[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020], 'y':[48067,48933,49928,50335,50977,51428,51195,50871,51127,50578,49695], 'type':'line', 'name': 'Michigan State University','line':dict(color='green')},
                                 {'x':[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020], 'y':[41924,42716,43426,43710,43625,43651,44718,46002,46716,48090,47907], 'type':'line', 'name': 'University of Michigan','line':dict(color='blue')}
                                 ,],
                        'layout':{'title':'Total Enrollment of MSU vs. UofM', 
                                  'xaxis':{'title':"Year", 'linecolor':"black"}, 
                                  'yaxis':{'title':"University Name", 'linecolor':"black"},
                                  'paper_bgcolor':'#cccedb',
                                  'plot_bgcolor':'ededed'}
                        
                        
                        
                })
                ])



if __name__ == '__main__':
    app.run_server(port=1029, debug = True)
                                 
                      
