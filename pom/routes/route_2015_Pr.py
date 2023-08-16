"""Module for creating graph image of conveyor from 2019_WiBuKu"""

import datetime
import graphviz

from pom.routes.utils.utils import size_mm_to_inch, change_canvas_size, change_dpi_tag, paste_c_k_into_route


def route_2015_Pr(param, change_canvas_size_=False, paste_c_k=False):
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

    graph.node('lu', pos='0.1, 0.85!', label='')
    graph.node('rd', pos='0.9, 0.05!', label='')

    graph.node('C11_t', pos='0.4, 0.52!')
    graph.node('C11_h', pos='0.48, 0.62!')
    graph.edge('C11_t', 'C11_h', label='<C<SUB>1.1</SUB>>')
    graph.node('C12_t', pos='0.47, 0.62!')
    graph.node('C12_h', pos='0.63, 0.62!')
    graph.edge('C12_t', 'C12_h', taillabel='<C<SUB>1.2</SUB>>',
               labeldistance='2', labelangle='20')
    graph.node('C13_t', pos='0.63, 0.63!')
    graph.node('C13_h', pos='0.63, 0.56!')
    graph.edge('C13_t', 'C13_h', taillabel='<C<SUB>1.3</SUB>>',
               labeldistance='1.5', labelangle='310')
    graph.node('C14_t', pos='0.63, 0.56!')
    graph.node('C14_h', pos='0.63, 0.44!')
    graph.edge('C14_t', 'C14_h', label='<C<SUB>1.4</SUB>>')
    graph.node('C15_t', pos='0.63, 0.44!')
    graph.node('C15_h', pos='0.58, 0.44!')
    graph.edge('C15_t', 'C15_h', taillabel='<C<SUB>1.5</SUB>>',
               labeldistance='0.8', labelangle='60')
    graph.node('C16_t', pos='0.58, 0.46!')
    graph.node('C16_h', pos='0.58, 0.38!')
    graph.edge('C16_t', 'C16_h', label='<C<SUB>1.6</SUB>>')
    graph.node('C17_t', pos='0.58, 0.38!')
    graph.node('C17_h', pos='0.58, 0.3!')
    graph.edge('C17_t', 'C17_h', label='<C<SUB>1.7</SUB>>')
    graph.node('C18_t', pos='0.58, 0.3!')
    graph.node('C18_h', pos='0.58, 0.15!')
    graph.edge('C18_t', 'C18_h', label='<C<SUB>1.8</SUB>>')
    graph.node('C19_t', pos='0.58, 0.15!')
    graph.node('C19_h', pos='0.715, 0.18!')
    graph.edge('C19_t', 'C19_h', taillabel='<C<SUB>1.9</SUB>>',
               labeldistance='2', labelangle='20')
    graph.node('C22_t', pos='0.78, 0.62!')
    graph.node('C22_h', pos='0.63, 0.62!')
    graph.edge('C22_t', 'C22_h', taillabel='<C<SUB>2.2</SUB>>',
               labeldistance='2', labelangle='340')
    graph.node('C21_t', pos='0.93, 0.62!')
    graph.node('C21_h', pos='0.78, 0.62!')
    graph.edge('C21_t', 'C21_h', taillabel='<C<SUB>2.1</SUB>>',
               labeldistance='2', labelangle='340')
    graph.node('C33_t', pos='0.865, 0.44!')
    graph.node('C33_h', pos='0.78, 0.44!')
    graph.edge('C33_t', 'C33_h', taillabel='<C<SUB>3.3</SUB>>',
               labeldistance='1.5', labelangle='325')
    graph.node('C34_t', pos='0.78, 0.44!')
    graph.node('C34_h', pos='0.58, 0.46!')
    graph.edge('C34_t', 'C34_h', taillabel='<C<SUB>3.4</SUB>>',
               labeldistance='3', labelangle='345')
    graph.node('C41_t', pos='0.09, 0.13!')
    graph.node('C41_h', pos='0.16, 0.13!')
    graph.edge('C41_t', 'C41_h', taillabel='<C<SUB>4.1</SUB>>',
               labeldistance='1.3', labelangle='40')
    graph.node('C42_t', pos='0.16, 0.13!')
    graph.node('C42_h', pos='0.16, 0.277!')
    graph.edge('C42_t', 'C42_h', label='<C<SUB>4.2</SUB>>')
    graph.node('C43_t', pos='0.15, 0.27!')
    graph.node('C43_h', pos='0.185, 0.3!')
    graph.edge('C43_t', 'C43_h', label='<C<SUB>4.3</SUB>>')
    graph.node('C44_t', pos='0.17, 0.3!')
    graph.node('C44_h', pos='0.27, 0.3!')
    graph.edge('C44_t', 'C44_h', taillabel='<C<SUB>4.4</SUB>>',
               labeldistance='1.5', labelangle='29')
    graph.node('C45_t', pos='0.27, 0.3!')
    graph.node('C45_h', pos='0.37, 0.3!')
    graph.edge('C45_t', 'C45_h', taillabel='<C<SUB>4.5</SUB>>',
               labeldistance='1.5', labelangle='29')
    graph.node('C46_t', pos='0.37, 0.3!')
    graph.node('C46_h', pos='0.48, 0.3!')
    graph.edge('C46_t', 'C46_h', taillabel='<C<SUB>4.6</SUB>>',
               labeldistance='1.5', labelangle='29')
    graph.node('C47_t', pos='0.48, 0.3!')
    graph.node('C47_h', pos='0.58, 0.3!')
    graph.edge('C47_t', 'C47_h', taillabel='<C<SUB>4.7</SUB>>',
               labeldistance='1.5', labelangle='29')



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
