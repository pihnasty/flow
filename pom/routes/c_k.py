"""Module for creating graph image of conveyor from 2002_Co"""

import datetime
import graphviz
import utils.utils


def C_k(param):
    """ This function creates sub-plot/graph of universal
    conveyor rout Ck
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
        size=utils.utils.size_mm_to_inch(graph_attr['x_size'],
                                         graph_attr['y_size'],
                                         decimal_places=4),
        dpi=graph_attr['dpi'],
        bgcolor='white',
        center='1',
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

    graph.node('1', pos="0.075, 0.27!")
    graph.node('2', pos="0.2, 0.27!")
    graph.node('3', pos="0.45, 0.27!")
    graph.node('4', pos="0.8, 0.27!")
    graph.node('c_k_h', pos="0.1, 0.2745!")
    graph.node('c_k_t', pos="0.1, 0.2745!")
    graph.node('c_t', pos="0.17, 0.2745!")
    graph.node('c_h', pos="0.25, 0.2745!")
    graph.node('ucb_t', pos="0.23, 0.273299!")
    graph.node('ucb_h', pos="0.23, 0.2729!")
    graph.node('cb_t', pos="0.23, 0.272!")
    graph.node('cb_h', pos="0.23, 0.271983!")
    graph.node('ucbe_t', pos="0.25, 0.27099!")
    graph.node('ucbe_h', pos="0.25, 0.27!")
    graph.node('cbe_t', pos="0.55, 0.27099!")
    graph.node('cbe_h', pos="0.55, 0.27!")

    edge_attr = param['edge_attr']
    graph.attr('edge',
               penwidth=edge_attr['penwidth'],
               fontcolor='black',
               fontsize=edge_attr['fontsize'],  # Speed and Length of conveyer font size
               fontname='Times-Roman',
               arrowsize=edge_attr['arrowsize'],
               arrowhead='open'
               )
    graph.edge('1', '2',
               headlabel='<&gamma;<SUB>k-1</SUB>(&tau;)>',
               labeldistance='1.2',
               labelangle='320'
               )
    graph.edge('2', '3',
               taillabel='<&xi;<SUB>k-1</SUB>,g<SUB>k-1</SUB>(&tau;)>',
               # label="",
               headlabel='<&gamma;<SUB>k</SUB>(&tau;)>',
               labeldistance='1.1',
               labelangle='320'
               )
    graph.edge('3', '4',
               taillabel='<&xi;<SUB>k</SUB>,g<SUB>k</SUB>(&tau;)>',
               # label="",
               labeldistance='0.8',
               labelangle='290',
               arrowhead='open'
               )
    graph.edge('c_k_t', 'c_k_h',
               taillabel='<C<SUB>k</SUB>(&tau;):>',
               labeldistance='1.2',
               labelangle='270',
               arrowsize='0',
               arrowhead='normal'
               )
    graph.edge('c_t', 'c_h',
               taillabel='<Belt conveyor>',
               labeldistance='3.9',
               labelangle='0',
               )
    graph.edge('ucb_t', 'ucb_h',
               headlabel='<Uncontrolled bunker>',
               labeldistance='4.1',
               labelangle='273',
               arrowhead='o'
               )
    graph.edge('cb_t', 'cb_h',
               headlabel='<Controlled bunker>',
               labeldistance='3.7',
               labelangle='273',
               arrowhead='normal'
               )
    graph.edge('ucbe_t', 'ucbe_h',
               arrowhead='o'
               )
    graph.edge('cbe_t', 'cbe_h',
               arrowhead='normal'
               )

    graph.view()

    image_path = (files_category + graph_name + '/' +
                  file_name + '.' + param['file_format'])
    # To cut the canvas of the result image file:
    utils.utils.cut_C_k_canvas(image_path,
                               new_width=828,
                               new_height=356,
                               paste_x=-25,
                               paste_y=-30)
    # To draw a frame around the canvas of the result image file
    # utils.utils.draw_frame(image_path,
    #                        frame_width=2,
    #                        frame_color=(0, 0, 0))
    # To change the DPI (dots per inch) metadata of the result image file:
    # utils.utils.change_dpi_tag(image_path, int(graph_attr['dpi']))
