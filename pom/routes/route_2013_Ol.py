"""Module for creating graph image of conveyor from 2013_Ol"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2013_Ol(param, change_canvas_size_=False, paste_c_k=False):
    """ This function creates plot/graph for conveyor route
    :param param: parameters for the plot from pom/routes/InitData/initialize_routes.py
    :return:
    """
    files_category = param['files_category']
    # setting the name of the result image file:
    function_name_parts = __name__.split('.')
    graph_name = function_name_parts[-1]  # param['graph_name']
    dates = datetime.datetime.now()
    suffix = dates.strftime("%Y_%m_%d_%H_%M_%S")
    file_name = graph_name + '_' + suffix + '.gv'

    graph = graphviz.Digraph(name=graph_name,
                             filename=files_category + graph_name + '/' + file_name,
                             format=param['file_format'],
                             engine=param['engine'],
                             )
    graph_attr = param['graph_attr']
    graph.attr(
        rankdir=graph_attr['rankdir'],
        ratio='fill',
        size=size_mm_to_inch(graph_attr['x_size'],
                             graph_attr['y_size'],
                             decimal_places=4),
        dpi=graph_attr['dpi'],
        bgcolor='white',
        center='1'
    )
    node_attr = param['node_attr']
    graph.attr('node',
               shape=node_attr['shape'],
               penwidth=node_attr['penwidth'],
               label='',
               fixedsize='true',
               width=node_attr['width'],
               height=node_attr['height'],
               fontsize=node_attr['fontsize'],  # Flow font size
               labelloc='b'
               )

    edge_attr = param['edge_attr']
    graph.attr('edge',
               penwidth=edge_attr['penwidth'],
               fontcolor='black',
               fontsize=edge_attr['fontsize'],  # Font size of conveyer name
               arrowsize=edge_attr['arrowsize'],
               abeldistance='1.8',
               arrowhead='open'
               )

    graph.node('lu', pos='0.1, 1.15!', label='')
    graph.node('rd', pos='1., 0.17!', label='')

    graph.node('hS71', pos='0.615, 0.315!')
    graph.node('tS71', pos='0.615, 0.21!')
    graph.edge('tS71', 'hS71', label='<C<SUB>1</SUB>>')
    graph.node('hS72', pos='0.3, 0.315!')
    graph.node('tS72', pos='0.615, 0.315!')
    graph.edge('tS72', 'hS72', taillabel='<C<SUB>2</SUB>>',
               labeldistance='3.5', labelangle='350')
    graph.node('hS', pos='0.3, 0.88!')
    graph.node('tS', pos='0.3, 0.26!')
    graph.edge('tS', 'hS', label='<C<SUB>3</SUB>>')
    graph.node('hS2', pos='0.925, 0.415!')
    graph.node('tS2', pos='0.925, 0.225!')
    graph.edge('tS2', 'hS2', label='<C<SUB>4</SUB>>')
    graph.node('hS3', pos='0.3, 0.415!')
    graph.node('tS3', pos='1.12, 0.415!')
    graph.edge('tS3', 'hS3', taillabel='<C<SUB>5</SUB>>',
               labeldistance='9', labelangle='356')
    graph.node('hS11', pos='0.97, 0.5!')
    graph.node('tS11', pos='0.97, 0.64!')
    graph.edge('tS11', 'hS11', label='<C<SUB>6</SUB>>')
    graph.node('hS12', pos='0.73, 0.5!')
    graph.node('tS12', pos='1, 0.5!')
    graph.edge('tS12', 'hS12', taillabel='<C<SUB>7</SUB>>',
               labeldistance='3', labelangle='347')
    graph.node('hS13', pos='0.3, 0.5!')
    graph.node('tS13', pos='0.73, 0.5!')
    graph.edge('tS13', 'hS13', taillabel='<C<SUB>8</SUB>>',
               labeldistance='4', labelangle='351')
    graph.node('hS41', pos='0.74, 0.595!')
    graph.node('tS41', pos='0.74, 0.68!')
    graph.edge('tS41', 'hS41', label='<C<SUB>9</SUB>>')
    graph.node('hS42', pos='0.49, 0.595!')
    graph.node('tS42', pos='0.74, 0.595!')
    graph.edge('tS42', 'hS42', taillabel='<C<SUB>10</SUB>>',
               labeldistance='3', labelangle='347')
    graph.node('hS51', pos='0.49, 0.62!')
    graph.node('tS51', pos='0.49, 0.69!')
    graph.edge('tS51', 'hS51', label='<C<SUB>11</SUB>>')
    graph.node('hS52', pos='0.49, 0.5!')
    graph.node('tS52', pos='0.49, 0.62!')
    graph.edge('tS52', 'hS52', label='<C<SUB>12</SUB>>')
    graph.node('hS61', pos='0.05, 0.315!')
    graph.node('tS61', pos='0.16, 0.315!')
    graph.edge('tS61', 'hS61', taillabel='<C<SUB>13</SUB>>',
               labeldistance='1.1', labelangle='322')
    graph.node('hS62', pos='0.05, 0.475!')
    graph.node('tS62', pos='0.05, 0.315!')
    graph.edge('tS62', 'hS62', label='<C<SUB>14</SUB>>')
    graph.node('hS63', pos='0.3, 0.475!')
    graph.node('tS63', pos='0.05, 0.475!')
    graph.edge('tS63', 'hS63', taillabel='<C<SUB>15</SUB>>',
               labeldistance='3', labelangle='347')
    graph.node('hS8', pos='0.12, 0.475!')
    graph.node('tS8', pos='0.12, 0.62!')
    graph.edge('tS8', 'hS8', label='<C<SUB>16</SUB>>')

    graph.view()

    image_path = (files_category + graph_name + '/' +
                  file_name + '.' + param['file_format'])
    # To change the canvas size of the result image file:
    if change_canvas_size_:
        change_canvas_size(image_path,
                           new_width=int(graph_attr['x_size']),
                           new_height=int(graph_attr['y_size']),
                           dpi=int(graph_attr['dpi']))

    # To paste C_k image into the result route image:
    if paste_c_k:
        c_k_path = (files_category + 'c_k/c_k_5.jpeg')
        paste_c_k_into_route(image_path, c_k_path)

    # To change the DPI (dots per inch) metadata of the result image file:
    change_dpi_tag(image_path, int(graph_attr['dpi']))

# fig_1(experiments['default'])
