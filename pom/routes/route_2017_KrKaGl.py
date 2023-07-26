"""Module for creating graph image of conveyor from 2017_KrKaGl"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2017_KrKaGl(param, change_canvas_size_, paste_c_k):
    """ This function creates plot/graph for conveyor route
    :param change_canvas_size_:true of false
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
               labeldistance='1.8',
               arrowhead='open'
               )

    graph.node('lu', pos='0.0, 0.75!', label='')
    graph.node('rd', pos='1.0, -0.05!', label='')

    graph.node('tA183', pos='0.85, 0.04!')
    graph.node('hA183', pos='0.72, 0.04!')
    graph.edge('tA183', 'hA183', taillabel='<C<SUB>1</SUB>>', labeldistance='1.8', labelangle='340')
    graph.node('tM41', pos='0.725, 0.03!')
    graph.node('hM41', pos='0.68, 0.15!')
    graph.edge('tM41', 'hM41', label='<C<SUB>2</SUB>>')
    graph.node('hA183L71', pos='0.84, 0.04!')
    graph.node('tA183L71', pos='0.84, 0.046!')
    graph.edge('tA183L71', 'hA183L71', arrowhead='o')
    graph.node('hP22', pos='0.717, 0.05!')
    graph.node('tP22', pos='0.726, 0.0525!')
    graph.edge('tP22', 'hP22', arrowhead='o')
    graph.node('hP18', pos='0.708, 0.075!')
    graph.node('tP18', pos='0.716, 0.0772!')
    graph.edge('tP18', 'hP18', arrowhead='o')
    graph.node('hP13', pos='0.70, 0.1!')
    graph.node('tP13', pos='0.705, 0.1013!')
    graph.edge('tP13', 'hP13', arrowhead='o')
    graph.node('hP8', pos='0.692, 0.12!')
    graph.node('tP8', pos='0.70, 0.1223!')
    graph.edge('tP8', 'hP8', arrowhead='o')
    graph.node('tL52', pos='0.68, 0.111!')
    graph.node('hL52', pos='0.68, 0.3!')
    graph.edge('tL52', 'hL52', label='<C<SUB>3</SUB>>')
    graph.node('hP24', pos='0.679, 0.12!')
    graph.node('tP24', pos='0.675, 0.12!')
    graph.edge('tP24', 'hP24', arrowhead='o')
    graph.node('hL52L621', pos='0.679, 0.15!')
    graph.node('tL52L621', pos='0.675, 0.15!')
    graph.edge('tL52L621', 'hL52L621', arrowhead='normal')
    graph.node('tL413', pos='0.78, 0.185!')
    graph.node('hL413', pos='0.68, 0.185!')
    graph.edge('tL413', 'hL413',
               taillabel='<C<SUB>4</SUB>>',
               labeldistance='1.8', labelangle='340')
    graph.node('hL413b', pos='0.679, 0.185!')
    graph.node('tL413b', pos='0.675, 0.185!')
    graph.edge('tL413b', 'hL413b', arrowhead='normal')
    graph.node('hP15', pos='0.76, 0.186!')
    graph.node('tP15', pos='0.76, 0.189!')
    graph.edge('tP15', 'hP15', arrowhead='o')
    graph.node('hP5', pos='0.679, 0.26!')
    graph.node('tP5', pos='0.675, 0.26!')
    graph.edge('tP5', 'hP5', arrowhead='o')
    graph.node('hP10', pos='0.679, 0.24!')
    graph.node('tP10', pos='0.675, 0.24!')
    graph.edge('tP10', 'hP10', arrowhead='o')
    graph.node('tL1031', pos='0.99, 0.53!')
    graph.node('hL1031', pos='0.79, 0.53!')
    graph.edge('tL1031', 'hL1031', taillabel='<C<SUB>5</SUB>>',
               labeldistance='1.7', labelangle='335')
    graph.node('hP30', pos='0.98, 0.53!')
    graph.node('tP30', pos='0.98, 0.535!')
    graph.edge('tP30', 'hP30', arrowhead='o')
    graph.node('hP12', pos='0.89, 0.53!')
    graph.node('tP12', pos='0.89, 0.535!')
    graph.edge('tP12', 'hP12', arrowhead='o')
    graph.node('tL161', pos='0.79, 0.555!')
    graph.node('hL161', pos='0.79, 0.3!')
    graph.edge('tL161', 'hL161', label='<C<SUB>6</SUB>>')
    graph.node('tP24_2', pos='0.783, 0.54!')
    graph.node('hP24_2', pos='0.789, 0.54!')
    graph.edge('tP24_2', 'hP24_2', arrowhead='o')
    graph.node('tP15_2', pos='0.783, 0.465!')
    graph.node('hP15_2', pos='0.789, 0.465!')
    graph.edge('tP15_2', 'hP15_2', arrowhead='o')
    graph.node('tP11', pos='0.783, 0.44!')
    graph.node('hP11', pos='0.789, 0.44!')
    graph.edge('tP11', 'hP11', arrowhead='o')
    graph.node('tP9c', pos='0.792, 0.3!')
    graph.node('hP9c', pos='0.62, 0.3!')
    graph.edge('tP9c', 'hP9c', taillabel='<C<SUB>7</SUB>>',
               labeldistance='1.7', labelangle='335')
    graph.node('tP83', pos='0.69, 0.305!')
    graph.node('hP83', pos='0.69, 0.3!')
    graph.edge('tP83', 'hP83', arrowhead='o')
    graph.node('tP8c', pos='0.625, 0.3!')
    graph.node('hP8c', pos='0.38, 0.3!')
    graph.edge('tP8c', 'hP8c', taillabel='<C<SUB>8</SUB>>',
               labeldistance='1.9', labelangle='340')
    graph.node('tP67', pos='0.615, 0.305!')
    graph.node('hP67', pos='0.615, 0.3!')
    graph.edge('tP67', 'hP67', arrowhead='normal')
    graph.node('tP66', pos='0.585, 0.305!')
    graph.node('hP66', pos='0.585, 0.3!')
    graph.edge('tP66', 'hP66', arrowhead='o')
    graph.node('tP57', pos='0.465, 0.305!')
    graph.node('hP57', pos='0.465, 0.3!')
    graph.edge('tP57', 'hP57', arrowhead='o')
    graph.node('tP50', pos='0.435, 0.305!')
    graph.node('hP50', pos='0.435, 0.3!')
    graph.edge('tP50', 'hP50', arrowhead='o')
    graph.node('tP7c', pos='0.383, 0.3!')
    graph.node('hP7c', pos='0.2, 0.3!')
    graph.edge('tP7c', 'hP7c', taillabel='<C<SUB>11</SUB>>',
               labeldistance='1.7', labelangle='335')
    graph.node('tP6c', pos='0.21, 0.3!')
    graph.node('hP6c', pos='0.03, 0.3!')
    graph.edge('tP6c', 'hP6c', taillabel='<C<SUB>12</SUB>>',
               labeldistance='1.7', labelangle='335')
    graph.node('tP15_3', pos='0.11, 0.305!')
    graph.node('hP15_3', pos='0.11, 0.3!')
    graph.edge('tP15_3', 'hP15_3', arrowhead='o')
    graph.node('tP5ac', pos='0.03, 0.299!')
    graph.node('hP5ac', pos='0.06, 0.34!')
    graph.edge('tP5ac', 'hP5ac', label='<C<SUB>13</SUB>>')
    graph.node('tL910b', pos='0.275, 0.48!')
    graph.node('hL910b', pos='0.42, 0.48!')
    graph.edge('tL910b', 'hL910b', taillabel='<C<SUB>9</SUB>>',
               labeldistance='1.7', labelangle='335')
    graph.node('hP14', pos='0.285, 0.48!')
    graph.node('tP14', pos='0.285, 0.486!')
    graph.edge('tP14', 'hP14', arrowhead='o')
    graph.node('hP7', pos='0.34, 0.48!')
    graph.node('tP7', pos='0.34, 0.486!')
    graph.edge('tP7', 'hP7', arrowhead='o')
    graph.node('tL142', pos='0.42, 0.515!')
    graph.node('hL142', pos='0.42, 0.3!')
    graph.edge('tL142', 'hL142', taillabel='<C<SUB>10</SUB>>',
               labeldistance='2.7', labelangle='25')
    graph.node('tP17', pos='0.414, 0.505!')
    graph.node('hP17', pos='0.42, 0.505!')
    graph.edge('tP17', 'hP17', arrowhead='o')
    graph.node('tP11_2', pos='0.414, 0.425!')
    graph.node('hP11_2', pos='0.42, 0.425!')
    graph.edge('tP11_2', 'hP11_2', arrowhead='o')
    graph.node('tP6', pos='0.414, 0.39!')
    graph.node('hP6', pos='0.42, 0.39!')
    graph.edge('tP6', 'hP6', arrowhead='o')

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
