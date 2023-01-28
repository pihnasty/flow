import graphviz
# f = graphviz.Digraph(filename = "output/plain organogram 1.gv")
# names = ["A","B","C","D","E","F","G","H"]
# positions = ["CEO","Team A Lead","Team B Lead", "Staff A","Staff B", "Staff C", "Staff D", "Staff E"]
# for name, position in zip(names, positions):
#     f.node(name, position)
#
# #Specify edges
# f.edge("A","B"); f.edge("A","C") #CEO to Team Leads
# f.edge("B","D"); f.edge("B","E") #Team A relationship
# f.edge("C","F"); f.edge("C","G"); f.edge("C","H") #Team B relationship

# import graphviz
#
# g = graphviz.Graph("G", filename="process.gv")
#
# g.edge("run", "intr")
# g.edge('intr', 'runbl')
# g.edge('runbl', 'run')
# g.edge('run', 'kernel')
# g.edge('kernel', 'zombie')
# g.edge('kernel', 'sleep')
# g.edge('kernel', 'runmem')
# g.edge('sleep', 'swap')
# g.edge('swap', 'runswap')
# g.edge('runswap', 'new')
# g.edge('runswap', 'runmem')
# g.edge('new', 'runmem')
# g.edge('sleep', 'runmem')
#
# g.view()

import graphviz

# https://graphviz.readthedocs.io/en/stable/examples.html
f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')

f.attr('node', shape='doublecircle')
f.node('LR_0')
f.node('LR_3')
f.node('LR_4')
f.node('LR_8')

f.attr('node', shape='circle')
f.edge('LR_0', 'LR_2', label='SS(B)')
f.edge('LR_0', 'LR_1', label='SS(S)')
f.edge('LR_1', 'LR_3', label='S($end)')
f.edge('LR_2', 'LR_6', label='SS(b)')
f.edge('LR_2', 'LR_5', label='SS(a)')
f.edge('LR_2', 'LR_4', label='S(A)')
f.edge('LR_5', 'LR_7', label='S(b)')
f.edge('LR_5', 'LR_5', label='S(a)')
f.edge('LR_6', 'LR_6', label='S(b)')
f.edge('LR_6', 'LR_5', label='S(a)')
f.edge('LR_7', 'LR_8', label='S(b)')
f.edge('LR_7', 'LR_5', label='S(a)')
f.edge('LR_8', 'LR_6', label='S(b)')
f.edge('LR_8', 'LR_5', label='S(a)')

f.view()
