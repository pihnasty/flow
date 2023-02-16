import graphviz

filesCategory = 'routes_results/'
graph_name = 'fig_1'
fileName = graph_name + '.gv'

f = graphviz.Digraph(name=graph_name, filename=filesCategory + fileName,
                     format='jpeg',
                     engine='neato',
                     # engine='dot'
                     )
f.attr(rankdir='LR', ratio='fill', size='4,3',
       dpi='600',
       bgcolor='white',
       center='1'
       )

f.attr('node',
       shape='invtriangle',
       # shape='none',
       penwidth='0.5',
       label='',
       fixedsize='true',
       width='0.15',
       height='0.15',
       fontsize='14',  # flow font size
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

f.attr('edge',
       penwidth='0.5',
       fontcolor='black',
       fontsize='14',  # speed and length font size
       arrowsize='0.4'
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
