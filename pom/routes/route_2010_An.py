"""Module for creating graph image of conveyor from 2019_WiBuKu"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2010_An(param, change_canvas_size_=False, paste_c_k=False):
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

    graph.node('lu', pos='-0.05, 0.95!', label='')
    graph.node('rd', pos='0.95, -0.05!', label='')

    graph.node('PT3_t', pos='0.72, 0.28!')
    graph.node('PT3_h', pos='0.72, 0.5!')
    graph.edge('PT3_t', 'PT3_h', taillabel='<C<SUB>3</SUB>>',
               labeldistance='3', labelangle='15')
    graph.node('PT2_t', pos='0.78, 0.5!')
    graph.node('PT2_h', pos='0.1, 0.5!')
    graph.edge('PT2_t', 'PT2_h', taillabel='<C<SUB>2</SUB>>',
               labeldistance='8', labelangle='354')
    graph.node('Gw_t', pos='0.783, 0.4915!')
    graph.node('Gw_h', pos='0.775, 0.5!')
    graph.edge('Gw_t', 'Gw_h', arrowhead='normal')
    graph.node('PT1_t', pos='0.1, 0.5!')
    graph.node('PT1_h', pos='0.1, 0.16!')
    graph.edge('PT1_t', 'PT1_h', taillabel='<C<SUB>1</SUB>>',
               labeldistance='4', labelangle='350')

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
