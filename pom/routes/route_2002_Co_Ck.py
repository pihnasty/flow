"""Module for creating graph image of conveyor from 2002_Co"""

import datetime
import graphviz
from utils.utils import change_dpi_tag, size_mm_to_inch


def route_2002_Co_Ck(param):
    """ This function creates plot/graph of conveyor route
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
    graph.node('1', pos='0, 0.3!')
    graph.node('2', pos='0.17, 0.3!')
    graph.node('3', pos='0.27, 0.38!')
    graph.node('4', pos='0.60, 0.38!')
    graph.node('5', pos='0.90, 0.38!')
    graph.node('6', pos='1, 0.44!',)

    edge_attr = param['edge_attr']
    graph.attr('edge',
               penwidth=edge_attr['penwidth'],
               fontcolor='black',
               fontsize=edge_attr['fontsize'],  # Speed and Length of conveyer font size
               arrowsize=edge_attr['arrowsize'],
               )
    graph.edge('1', '2',
               taillabel='<C<SUB>1</SUB>>',
               # label='',
               labeldistance='1.5',
               labelangle='26'
               )
    graph.edge('2', '3',
               label='<C<SUB>2</SUB>>',
               )
    graph.edge('3', '4',
               label='<C<SUB>3</SUB>>',
               )
    graph.edge('4', '5',
               label='<C<SUB>4</SUB>>',
               )
    graph.edge('5', '6',
               label='<C<SUB>5</SUB>>',
               )
    graph.view()
    # To change the DPI (dots per inch) metadata of the result image file:
    image_path = (files_category + graph_name + '/' +
                  file_name + '.' + param['file_format'])
    change_dpi_tag(image_path, int(graph_attr['dpi']))

# fig_1(experiments['default'])
