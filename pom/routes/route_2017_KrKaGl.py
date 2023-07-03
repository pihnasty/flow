"""Module for creating graph image of conveyor from 2017_KrKaGl"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2017_KrKaGl(param):
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
    graph.node('1', pos='0.95, 0.20!')
    graph.node('2', pos='0.78, 0.20!')
    graph.node('3', pos='0.71, 0.28!')
    graph.node('31', pos='0.71, 0.32!')
    graph.node('32', pos='0.83, 0.32!')
    graph.node('4', pos='0.71, 0.4!')
    graph.node('5', pos='0.85, 0.4!')
    graph.node('6', pos='0.42, 0.4!')
    graph.node('7', pos='0.42, 0.50!')
    graph.node('8', pos='0.25, 0.50!')
    graph.node('9', pos='0.05, 0.4!')
    graph.node('10', pos='0.10, 0.45!')
    graph.node('11', pos='0.85, 0.55!')
    graph.node('12', pos='1.1, 0.55!')

    edge_attr = param['edge_attr']
    graph.attr('edge',
               penwidth=edge_attr['penwidth'],
               fontcolor='black',
               fontsize=edge_attr['fontsize'],  # Speed and Length of conveyer font size
               arrowsize=edge_attr['arrowsize'],
               labeldistance='1.8'
               )
    graph.edge('1', '2', taillabel='<C<SUB>1</SUB>>', labeldistance='1.8', labelangle='340')
    graph.edge('2', '3', label='<C<SUB>2</SUB>>')
    graph.edge('3', '31', label='<C<SUB>3</SUB>>')
    graph.edge('31', '4', label='<C<SUB>5</SUB>>')
    graph.edge('32', '31', label='<C<SUB>4</SUB>>')
    graph.edge('5', '4', label='<C<SUB>8</SUB>>')
    graph.edge('4', '6', label='<C<SUB>9</SUB>>')
    graph.edge('7', '6', label='<C<SUB>11</SUB>>')
    graph.edge('8', '7', label='<C<SUB>10</SUB>>')
    graph.edge('6', '9', label='<C<SUB>12</SUB>>')
    graph.edge('9', '10', label='<C<SUB>13</SUB>>')
    graph.edge('11', '5', label='<C<SUB>7</SUB>>')
    graph.edge('12', '11', label='<C<SUB>6</SUB>>')

    graph.view()

    image_path = (files_category + graph_name + '/' +
                  file_name + '.' + param['file_format'])
    # To change the canvas size of the result image file:
    change_canvas_size(image_path,
                       new_width=int(graph_attr['x_size']),
                       new_height=int(graph_attr['y_size']),
                       dpi=int(graph_attr['dpi']))

    # To paste C_k image into the result route image:
    c_k_path = (files_category + 'c_k/c_k.jpeg')
    paste_c_k_into_route(image_path, c_k_path)

    # To change the DPI (dots per inch) metadata of the result image file:
    change_dpi_tag(image_path, int(graph_attr['dpi']))

# fig_1(experiments['default'])
