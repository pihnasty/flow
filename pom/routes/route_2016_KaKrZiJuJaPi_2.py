"""Module for creating graph image of conveyor from 2016_KaKrZiJuJaPi_2"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2016_KaKrZiJuJaPi_2(param, change_canvas_size_=False, paste_c_k=False):
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

    graph.node('lu', pos='0.0, 1.25!', label='')
    graph.node('rd', pos='1.0, -0.05!', label='')

    graph.node('hT1', pos='0.8, 0.05!')
    graph.node('tT1', pos='0.8, 0.175!')
    graph.edge('tT1', 'hT1', taillabel='<C<SUB>1</SUB>>',
               labeldistance='1.3', labelangle='35')
    graph.node('hT2', pos='0.8, 0.175!')
    graph.node('tT2', pos='0.8, 0.35!')
    graph.edge('tT2', 'hT2', taillabel='<C<SUB>2</SUB>>',
               labeldistance='1.5', labelangle='30')
    graph.node('hRR', pos='0.8, 0.25!')
    graph.node('tRR', pos='0.5, 0.25!')
    graph.edge('tRR', 'hRR', label='<railroad>', arrowhead='normal')
    graph.node('hT3', pos='0.8, 0.35!')
    graph.node('tT3', pos='0.8, 0.475!')
    graph.edge('tT3', 'hT3', taillabel='<C<SUB>3</SUB>>',
               labeldistance='1.3', labelangle='35')
    graph.node('hP17', pos='0.8, 0.43!')
    graph.node('tP17', pos='0.799, 0.43!')
    graph.edge('tP17', 'hP17', arrowhead='o')
    graph.node('hT4', pos='0.8, 0.475!')
    graph.node('tT4', pos='0.8, 0.6!')
    graph.edge('tT4', 'hT4', taillabel='<C<SUB>4</SUB>>',
               labeldistance='1.3', labelangle='35')
    graph.node('hUp', pos='0.8, 0.58!')
    graph.node('tUp', pos='0.799, 0.58!')
    graph.edge('tUp', 'hUp', arrowhead='o')
    graph.node('hT5', pos='0.8, 0.6!')
    graph.node('tT5', pos='0.8, 0.735!')
    graph.edge('tT5', 'hT5', taillabel='<C<SUB>5</SUB>>',
               labeldistance='1.3', labelangle='35')
    graph.node('hP37', pos='0.8, 0.725!')
    graph.node('tP37', pos='0.799, 0.725!')
    graph.edge('tP37', 'hP37', arrowhead='o')
    graph.node('hW1b', pos='0.8, 0.71!')
    graph.node('tW1b', pos='0.68, 0.71!')
    graph.edge('tW1b', 'hW1b', taillabel='<C<SUB>6</SUB>>',
               labeldistance='1.5', labelangle='330')
    graph.node('hP6', pos='0.7, 0.71!')
    graph.node('tP6', pos='0.7, 0.7105!')
    graph.edge('tP6', 'hP6', arrowhead='o')
    graph.node('hW91', pos='0.68, 0.71!')
    graph.node('tW91', pos='0.47, 0.71!')
    graph.edge('tW91', 'hW91', taillabel='<C<SUB>7</SUB>>', arrowhead='normal',
               labeldistance='2.5', labelangle='343')
    graph.node('hP28', pos='0.625, 0.71!')
    graph.node('tP28', pos='0.625, 0.7105!')
    graph.edge('tP28', 'hP28', arrowhead='o')
    graph.node('hP25', pos='0.6, 0.71!')
    graph.node('tP25', pos='0.6, 0.7105!')
    graph.edge('tP25', 'hP25', arrowhead='o')
    graph.node('hP29', pos='0.5, 0.71!')
    graph.node('tP29', pos='0.5, 0.7105!')
    graph.edge('tP29', 'hP29', arrowhead='o')
    graph.node('hP30', pos='0.48, 0.71!')
    graph.node('tP30', pos='0.48, 0.7105!')
    graph.edge('tP30', 'hP30', arrowhead='o')
    graph.node('hC232a', pos='0.53, 0.71!')
    graph.node('tC232a', pos='0.53, 0.775!')
    graph.edge('tC232a', 'hC232a', taillabel='<C<SUB>8</SUB>>',
               arrowhead='normal',
               labeldistance='0.8', labelangle='70')
    graph.node('hP6_2', pos='0.53, 0.75!')
    graph.node('tP6_2', pos='0.529, 0.75!')
    graph.edge('tP6_2', 'hP6_2', arrowhead='o')
    graph.node('hN331', pos='0.53, 0.775!')
    graph.node('tN331', pos='0.315, 0.775!')
    graph.edge('tN331', 'hN331', taillabel='<C<SUB>9</SUB>>',
               labeldistance='2.5', labelangle='343')
    graph.node('hP1', pos='0.375, 0.775!')
    graph.node('tP1', pos='0.375, 0.7755!')
    graph.edge('tP1', 'hP1', arrowhead='o')
    graph.node('hP14', pos='0.41, 0.775!')
    graph.node('tP14', pos='0.41, 0.7755!')
    graph.edge('tP14', 'hP14', arrowhead='o')
    graph.node('hP18', pos='0.45, 0.775!')
    graph.node('tP18', pos='0.45, 0.7755!')
    graph.edge('tP18', 'hP18', arrowhead='o')
    graph.node('hC242', pos='0.325, 0.775!')
    graph.node('tC242', pos='0.375, 0.89!')
    graph.edge('tC242', 'hC242', taillabel='<C<SUB>10</SUB>>',
               labeldistance='1.2', labelangle='70')
    graph.node('hP27', pos='0.358, 0.85!')
    graph.node('tP27', pos='0.355, 0.85!')
    graph.edge('tP27', 'hP27', arrowhead='o')
    graph.node('hP28_2', pos='0.362, 0.865!')
    graph.node('tP28_2', pos='0.359, 0.865!')
    graph.edge('tP28_2', 'hP28_2', arrowhead='o')
    graph.node('hN465', pos='0.37, 0.88!')
    graph.node('tN465', pos='0.2, 0.88!')
    graph.edge('tN465', 'hN465', taillabel='<C<SUB>11</SUB>>',
               labeldistance='2', labelangle='338')
    graph.node('hP15', pos='0.225, 0.88!')
    graph.node('tP15', pos='0.225, 0.8855!')
    graph.edge('tP15', 'hP15', arrowhead='o')
    graph.node('hP10', pos='0.26, 0.88!')
    graph.node('tP10', pos='0.26, 0.8855!')
    graph.edge('tP10', 'hP10', arrowhead='o')

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
