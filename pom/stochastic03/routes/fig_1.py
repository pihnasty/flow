import graphviz
from pom.stochastic03.InitData.initialize_routes import experiments


param = experiments['default']

filesCategory = 'routes_results/'
graph_name = param['graph_name']
fileName = graph_name + '.gv'

f = graphviz.Digraph(name=graph_name, filename=filesCategory + fileName,
                     format=param['file_format'],
                     engine=param['engine'],
                     )

graph_attr = param['graph_attr']
f.attr(
       rankdir=graph_attr['rankdir'],
       ratio='fill',
       size=graph_attr['size'],
       dpi=graph_attr['dpi'],
       bgcolor='white',
       center='1'
       )

node_attr = param['node_attr']
f.attr('node',
       shape=node_attr['shape'],
       penwidth=node_attr['penwidth'],
       label='',
       fixedsize='true',
       width=node_attr['width'],
       height=node_attr['height'],
       fontsize=node_attr['fontsize'],  # Flow font size
       labelloc='b'
       )
f.node('1', pos='0, 0.3!', xlabel='<&gamma;<SUB>1</SUB>(&tau;)>')
f.node('2', pos='0.17, 0.3!', xlabel='<&gamma;<SUB>2</SUB>(&tau;)>')
f.node('3', pos='0.27, 0.38!', xlabel='<&gamma;<SUB>m</SUB>(&tau;)>')
f.node('4', pos='0.60, 0.38!')
f.node('5', pos='0.90, 0.38!', xlabel='<&gamma;<SUB>M</SUB>(&tau;)>')
f.node('6', pos='1, 0.44!',
       # labelloc='c',
       xlabel='<&gamma;<SUB>M+1</SUB>(&tau;)>')

edge_attr = param['edge_attr']
f.attr('edge',
       penwidth=edge_attr['penwidth'],
       fontcolor='black',
       fontsize=edge_attr['fontsize'],  # Speed and Length of conveyer font size
       arrowsize=edge_attr['arrowsize'],
       )

f.edge('1', '2',
       taillabel='<&xi;<SUB>1</SUB>, g<SUB>1</SUB>(&tau;)>',
       # label='',
       labeldistance='2.1',
       labelangle='320'
       )
f.edge('2', '3',
       taillabel='<&xi;<SUB>2</SUB>, g<SUB>2</SUB>(&tau;)>',
       # label="",
       labeldistance='4.5',
       labelangle='310'
       )
f.edge('3', '4',
       taillabel='<&xi;<SUB>m</SUB>, g<SUB>m</SUB>(&tau;)>',
       # label="",
       labeldistance='3.8',
       labelangle='340'
       )
f.edge('4', '5')
f.edge('5', '6',
       taillabel='<&xi;<SUB>M</SUB>, g<SUB>M</SUB>(&tau;)>',
       # label="",
       labeldistance='4.7',
       labelangle='310'
       )

f.view()