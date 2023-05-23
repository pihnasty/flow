"""Main module to create plots/graphs of conveyer routes
"""
import sys
from pom.routes.InitData.initialize_routes import experiments
from pom.routes.fig_1 import fig_1


def main():
    fig_1(experiments['default'])


if __name__ == "__main__":
    main()
    sys.exit()
