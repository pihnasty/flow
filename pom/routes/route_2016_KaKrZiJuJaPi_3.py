"""Module for creating graph image of conveyor from 2016_KaKrZiJuJaPi_3"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2016_KaKrZiJuJaPi_3(param, change_canvas_size_=False, paste_c_k=False):
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

    graph.node('lu', pos='0.0, 0.65!', label='')
    graph.node('rd', pos='1.0, 0.05!', label='')

    graph.node('hRR', pos='0.52, 0.1!')
    graph.node('tRR', pos='0.9, 0.1!')
    graph.edge('tRR', 'hRR', taillabel='<railroad>', arrowhead='none')
    graph.node('hL41', pos='0.7, 0.1!')
    graph.node('tL41', pos='0.7, 0.28!')
    graph.edge('tL41', 'hL41', taillabel='<C<SUB>4</SUB>>',
               labeldistance='3.7', labelangle='13', arrowhead='normal')
    graph.node('hP4', pos='0.70, 0.175!')
    graph.node('tP4', pos='0.6999, 0.175!')
    graph.edge('tP4', 'hP4', arrowhead='o')
    graph.node('hP7', pos='0.70, 0.21!')
    graph.node('tP7', pos='0.6999, 0.21!')
    graph.edge('tP7', 'hP7', arrowhead='o')
    graph.node('hP15', pos='0.70, 0.27!')
    graph.node('tP15', pos='0.6999, 0.27!')
    graph.edge('tP15', 'hP15', arrowhead='o')
    graph.node('hL42', pos='0.7, 0.28!')
    graph.node('tL42', pos='0.7, 0.42!')
    graph.edge('tL42', 'hL42', taillabel='<C<SUB>3</SUB>>',
               labeldistance='2.5', labelangle='19')
    graph.node('hP51', pos='0.70, 0.38!')
    graph.node('tP51', pos='0.6999, 0.38!')
    graph.edge('tP51', 'hP51', arrowhead='o')
    graph.node('hP27', pos='0.70, 0.33!')
    graph.node('tP27', pos='0.6999, 0.33!')
    graph.edge('tP27', 'hP27', arrowhead='o')
    graph.node('hL43', pos='0.7, 0.42!')
    graph.node('tL43', pos='0.7, 0.54!')
    graph.edge('tL43', 'hL43', taillabel='<C<SUB>2</SUB>>',
               labeldistance='2.3', labelangle='21')
    graph.node('hB1', pos='0.70, 0.525!')
    graph.node('tB1', pos='0.6999, 0.525!')
    graph.edge('tB1', 'hB1', arrowhead='normal')
    graph.node('hP57', pos='0.70, 0.48!')
    graph.node('tP57', pos='0.6999, 0.48!')
    graph.edge('tP57', 'hP57', arrowhead='o')
    graph.node('hL44', pos='0.7, 0.54!')
    graph.node('tL44', pos='0.7, 0.585!')
    graph.edge('tL44', 'hL44', taillabel='<C<SUB>1</SUB>>',
               labeldistance='1.0', labelangle='55')
    graph.node('hP30', pos='0.70, 0.58!')
    graph.node('tP30', pos='0.6999, 0.58!')
    graph.edge('tP30', 'hP30', arrowhead='o')
    graph.node('hP44', pos='0.70, 0.57!')
    graph.node('tP44', pos='0.6999, 0.57!')
    graph.edge('tP44', 'hP44', arrowhead='o')
    graph.node('hP55', pos='0.70, 0.585!')
    graph.node('tP55', pos='0.6999, 0.59!')
    graph.edge('tP55', 'hP55', arrowhead='normal')

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
