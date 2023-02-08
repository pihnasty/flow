import graphviz

filesCategory = 'routes_results/'
graph_name = 'route_2015_Co'
fileName = graph_name + '.gv'

f = graphviz.Digraph(name=graph_name, filename=filesCategory + fileName,
                     format='png',
                     engine='neato',
                     # engine='dot'
                     )
f.attr(rankdir='LR', ratio='fill', size='4,3', dpi='600',
       bgcolor='white',
       center='1'
       )

f.attr('node', shape='invtriangle', label='', fixedsize='true', width='0.2', height='0.2')
f.node('1', pos='0, 0.3!')
f.node('2', pos='0.13, 0.3!')
f.node('3', pos='0.2, 0.4!')
f.node('4', pos='0.4, 0.4!')
f.node('5', pos='0.6, 0.4!')
f.node('6', pos='0.7, 0.5!')

f.attr('edge', fontcolor='black', fontsize='12', arrowsize='0.3')
f.edge('1', '2', taillabel='1.1 km', label='C1', labeldistance='2')
f.edge('2', '3', taillabel='   5 km', label='C2', labeldistance='3')
f.edge('3', '4', taillabel='   8.6 km', label='C3')
f.edge('4', '5', taillabel='     8 km', label='C4')
f.edge('5', '6', taillabel='           1.5 km', label='C5', labeldistance='1')

f.view()
