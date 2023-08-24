"""Module for creating graph image of conveyor from 2016_KaKrZiJuJaPi_8"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2016_KaKrZiJuJaPi_8(param, change_canvas_size_=False, paste_c_k=False):
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

    graph.node('lu', pos='0.1, 0.9!', label='')
    graph.node('rd', pos='1.0, 0.05!', label='')

    graph.node('hM21', pos='0.4, 0.62!')
    graph.node('tM21', pos='0.4, 0.3!')
    graph.edge('tM21', 'hM21', taillabel='<C<SUB>3</SUB>>',
               labeldistance='4', labelangle='345')
    graph.node('hP7', pos='0.4, 0.51!')
    graph.node('tP7', pos='0.399, 0.51!')
    graph.edge('tP7', 'hP7', arrowhead='o')
    graph.node('hP14', pos='0.4, 0.425!')
    graph.node('tP14', pos='0.399, 0.425!')
    graph.edge('tP14', 'hP14', arrowhead='o')
    graph.node('hM21g', pos='0.4, 0.3!')
    graph.node('tM21g', pos='0.4, 0.15!')
    graph.edge('tM21g', 'hM21g', taillabel='<C<SUB>2</SUB>>',
               labeldistance='3', labelangle='340', arrowhead='normal')
    graph.node('hP26', pos='0.4, 0.16!')
    graph.node('tP26', pos='0.399, 0.16!')
    graph.edge('tP26', 'hP26', arrowhead='o')
    graph.node('hS320', pos='0.4, 0.2!')
    graph.node('tS320', pos='0.915, 0.2!')
    graph.edge('tS320', 'hS320', taillabel='<C<SUB>1</SUB>>',
               labeldistance='6.5', labelangle='8')
    graph.node('hP5', pos='0.53, 0.2!')
    graph.node('tP5', pos='0.53, 0.205!')
    graph.edge('tP5', 'hP5', arrowhead='o')
    graph.node('hF14', pos='0.73, 0.2!')
    graph.node('tF14', pos='0.73, 0.205!')
    graph.edge('tF14', 'hF14', arrowhead='o')
    graph.node('hP23', pos='0.91, 0.2!')
    graph.node('tP23', pos='0.91, 0.205!')
    graph.edge('tP23', 'hP23', arrowhead='o')
    graph.node('hRR', pos='0.2, 0.62!')
    graph.node('tRR', pos='0.6, 0.62!')
    graph.edge('tRR', 'hRR', taillabel='<railroad>', arrowhead='none')

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
