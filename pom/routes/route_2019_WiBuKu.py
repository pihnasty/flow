"""Module for creating graph image of conveyor from 2019_WiBuKu"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2019_WiBuKu(param, change_canvas_size_=False, paste_c_k=False):
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

    graph.node('lu', pos='0.05, 0.85!', label='')
    graph.node('rd', pos='0.95, -0.05!', label='')

    graph.node('S320_t', pos='0.8, 0.2!')
    graph.node('S320_h', pos='0.321, 0.125!')
    graph.edge('S320_t', 'S320_h', taillabel='<C<SUB>1</SUB>>',
               labeldistance='6', labelangle='353')
    graph.node('M21_t', pos='0.321, 0.125!')
    graph.node('M21_h', pos='0.26, 0.54!')
    graph.edge('M21_t', 'M21_h', taillabel='<C<SUB>2</SUB>>',
               labeldistance='6', labelangle='353')
    graph.node('g1_t', pos='0.798, 0.21!')
    graph.node('g1_h', pos='0.798, 0.2!')
    graph.edge('g1_t', 'g1_h', arrowhead='normal')
    graph.node('g2_t', pos='0.73, 0.195!')
    graph.node('g2_h', pos='0.73, 0.19!')
    graph.edge('g2_t', 'g2_h', arrowhead='normal')
    graph.node('g3_t', pos='0.63, 0.179!')
    graph.node('g3_h', pos='0.63, 0.1745!')
    graph.edge('g3_t', 'g3_h', arrowhead='normal')
    graph.node('g4_t', pos='0.47, 0.155!')
    graph.node('g4_h', pos='0.47, 0.149!')
    graph.edge('g4_t', 'g4_h', arrowhead='normal')
    graph.node('cb1_t', pos='0.31, 0.17!')
    graph.node('cb1_h', pos='0.315, 0.17!')
    graph.edge('cb1_t', 'cb1_h', arrowhead='normal')
    graph.node('ucb1_t', pos='0.28, 0.325!')
    graph.node('ucb1_h', pos='0.292, 0.325!')
    graph.edge('ucb1_t', 'ucb1_h', arrowhead='o')
    graph.node('ucb2_t', pos='0.27, 0.44!')
    graph.node('ucb2_h', pos='0.275, 0.44!')
    graph.edge('ucb2_t', 'ucb2_h', arrowhead='o')

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
