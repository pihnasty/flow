"""Module for creating graph image of conveyor from 2016_KaKrZiJuJaPi_4"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2016_KaKrZiJuJaPi_4(param, change_canvas_size_=False, paste_c_k=False):
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

    graph.node('lu', pos='0.2, 0.83!', label='')
    graph.node('rd', pos='0.95, 0.1!', label='')

    graph.node('hW522', pos='0.5, 0.2!')
    graph.node('tW522', pos='0.66, 0.2!')
    graph.edge('tW522', 'hW522', taillabel='<C<SUB>1</SUB>>',
               labeldistance='2.5', labelangle='17')
    graph.node('hC11', pos='0.63, 0.2!')
    graph.node('tC11', pos='0.63, 0.205!')
    graph.edge('tC11', 'hC11', arrowhead='o')
    graph.node('hC12', pos='0.53, 0.2!')
    graph.node('tC12', pos='0.53, 0.205!')
    graph.edge('tC12', 'hC12', arrowhead='o')
    graph.node('hAS347', pos='0.55, 0.26!')
    graph.node('tAS347', pos='0.492, 0.19!')
    graph.edge('tAS347', 'hAS347', taillabel='<C<SUB>2</SUB>>',
               labeldistance='1.5', labelangle='35')
    graph.node('hAS343', pos='0.66, 0.42!')
    graph.node('tAS343', pos='0.55, 0.26!')
    graph.edge('tAS343', 'hAS343', taillabel='<C<SUB>3</SUB>>',
               labeldistance='3.7', labelangle='13')
    graph.node('hP23', pos='0.563, 0.28!')
    graph.node('tP23', pos='0.559, 0.28!')
    graph.edge('tP23', 'hP23', arrowhead='normal')
    graph.node('hZ604', pos='0.87, 0.37!')
    graph.node('tZ604', pos='0.56, 0.34!')
    graph.edge('tZ604', 'hZ604', taillabel='<C<SUB>4</SUB>>',
               labeldistance='5', labelangle='350')
    graph.node('hP15', pos='0.57, 0.342!')
    graph.node('tP15', pos='0.57, 0.3425!')
    graph.edge('tP15', 'hP15', arrowhead='o')
    graph.node('hT313', pos='0.66, 0.437!')
    graph.node('tT313', pos='0.87, 0.37!')
    graph.edge('tT313', 'hT313', taillabel='<C<SUB>5</SUB>>',
               labeldistance='3', labelangle='345')
    graph.node('hC52', pos='0.868, 0.37!')
    graph.node('tC52', pos='0.868, 0.3705!')
    graph.edge('tC52', 'hC52', arrowhead='o')
    graph.node('hA342', pos='0.66, 0.51!')
    graph.node('tA342', pos='0.66, 0.42!')
    graph.edge('tA342', 'hA342', taillabel='<C<SUB>6</SUB>>',
               labeldistance='2', labelangle='20')
    graph.node('hA34', pos='0.66, 0.445!')
    graph.node('tA34', pos='0.659, 0.445!')
    graph.edge('tA34', 'hA34', arrowhead='o')
    graph.node('hA341', pos='0.66, 0.61!')
    graph.node('tA341', pos='0.66, 0.51!')
    graph.edge('tA341', 'hA341', taillabel='<C<SUB>7</SUB>>',
               labeldistance='2', labelangle='20')
    graph.node('hRR', pos='0.8, 0.61!')
    graph.node('tRR', pos='0.4, 0.61!')
    graph.edge('tRR', 'hRR', label='<railroad>', arrowhead='none')

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
