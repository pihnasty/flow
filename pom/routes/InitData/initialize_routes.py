experiments = {
    '2017_KrKaGl': {
        'files_category': 'routes_results/',
        #'graph_name': 'fig_1',
        'file_format': 'jpeg',
        'engine': 'neato',
        # 'engine': 'dot'
        'graph_attr': {
            'rankdir': 'LR',
            'x_size': 86.5,  # 172.8 # 86.5
            'y_size': 72.0,  # 130.0 #65.0
            'dpi': '600',
        },
        'node_attr': {
            # 'shape': 'invtriangle',
            'shape': 'none',
            'penwidth': '0',
            'width': '0',
            'height': '0',
            'fontsize': '10',  # Flow font size
        },
        'edge_attr': {
            'penwidth': '0.5',
            'fontsize': '10',  # Font size of conveyer name
            'arrowsize': '0.5',
        }
    },
    '2019_WiBuKu': {
        'files_category': 'routes_results/',
        'file_format': 'jpeg',
        'engine': 'neato',
        # 'engine': 'dot'
        'graph_attr': {
            'rankdir': 'LR',
            'x_size': 86.5,  # 172.8 # 86.5
            'y_size': 72.0,  # 130.0 #65.0
            'dpi': '600',
        },
        'node_attr': {
            'shape': 'invtriangle',
            # 'shape': 'none',
            'penwidth': '0.5',
            'width': '0.15',
            'height': '0.15',
            'fontsize': '14',  # Flow font size
        },
        'edge_attr': {
            'penwidth': '0.5',
            'fontsize': '10',  # Speed and Length of conveyer font size
            'arrowsize': '0.4',
        }
    },
    'C_k': {
        'files_category': 'routes_results/',
        'file_format': 'jpeg',
        'engine': 'neato',
        # 'engine': 'dot'
        'graph_attr': {
            'rankdir': 'LR',
            'x_size': 43.0,  # 172.8 # 86.5
            'y_size': 36.0,  # 130.0 #65.0
            'dpi': '600',
        },
        'node_attr': {
            # 'shape': 'invtriangle',
            'shape': 'none',
            'penwidth': '0.5',
            'width': '0',
            'height': '0',
            'fontsize': '8',  # Label font size
        },
        'edge_attr': {
            'penwidth': '0.5',
            'fontsize': '8',  # Flow, Speed and Length of conveyer font size
            'arrowsize': '0.5',
        }
    },
    'default': {
        'files_category': 'routes_results/',
        #'graph_name': 'fig_1',
        'file_format': 'jpeg',
        'engine': 'neato',
        # 'engine': 'dot'
        'graph_attr': {
            'rankdir': 'LR',
            # 'size': '4, 3',
            'x_size': 86.5,  # 172.8 # 86.5
            'y_size': 72.0,  # 130.0 #65.0
            'dpi': '600',
        },
        'node_attr': {
            'shape': 'invtriangle',
            # 'shape': 'none',
            'penwidth': '0.5',
            'width': '0.15',
            'height': '0.15',
            'fontsize': '14',  # Flow font size
        },
        'edge_attr': {
            'penwidth': '0.5',
            'fontsize': '10',  # Speed and Length of conveyer font size
            'arrowsize': '0.4',
        }
    }
}
