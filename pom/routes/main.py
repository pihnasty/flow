"""Main module to create plots/graphs of conveyer routes
"""
import sys
from pom.routes.InitData.initialize_routes import experiments
# from pom.routes.fig_1 import fig_1
from pom.routes.route_2002_Co import route_2002_Co


def main():
    """
    Main function to create plots/graphs of conveyer routes
    :return:
    """
    # fig_1(experiments['default'])
    route_2002_Co(experiments['default'])


if __name__ == "__main__":
    main()
    sys.exit()
