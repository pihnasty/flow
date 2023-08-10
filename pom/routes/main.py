"""Main module to create plots/graphs of conveyer routes
"""
import sys
from pom.routes.InitData.initialize_routes import experiments
# from pom.routes.fig_1 import fig_1
from pom.routes.route_2002_Co import route_2002_Co
from pom.routes.route_2002_Co_Ck import route_2002_Co_Ck
from pom.routes.route_2010_An import route_2010_An
from pom.routes.route_2017_KrKaGl import route_2017_KrKaGl
from pom.routes.route_2019_WiBuKu import route_2019_WiBuKu
from pom.routes.c_k import C_k


def main():
    """
    Main function to create plots/graphs of conveyer routes
    :return:
    """
    # fig_1(experiments['default'])
    # route_2002_Co(experiments['default'])
    route_2002_Co_Ck(experiments['2017_KrKaGl'],
                      change_canvas_size_=True,
                      paste_c_k=True)
    # route_2019_WiBuKu(experiments['2017_KrKaGl'],
    #                   change_canvas_size_=True,
    #                   paste_c_k=True)
    # route_2017_KrKaGl(experiments['2017_KrKaGl'],
    #                   change_canvas_size_=True,
    #                   paste_c_k=True)
    # C_k(experiments['C_k'])
    route_2010_An(experiments['2017_KrKaGl'],
                      change_canvas_size_=True,
                      paste_c_k=True)


if __name__ == "__main__":
    main()
    sys.exit()
