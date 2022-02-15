from GraphSearch import *


def main():
    graph = {'oma': ['dal', 'hou'],
             'sdf': ['mdw', 'bwi', 'dal', 'hou'],
             'bwi': ['hou', 'sdf', 'mdw', 'dal'],
             'pwm': ['mdw', 'bwi', 'hou'],
             'slc': ['bwi', 'mdw', 'dal'],
             'bze': ['hou'],
             'dal': ['mdw', 'bwi', 'hou', 'sdf', 'oma', 'slc'],
             'hou': ['dal', 'oma', 'mdw', 'bwi', 'sdf', 'slc', 'bze'],
             'mdw': ['dal', 'bwi', 'hou', 'sdf', 'slc', 'oma', 'pwm']
             }

    # find the least number of stops from:
    # oma to sdf
    path_oma_sdf = bfs_shortest_path(graph, 'oma', 'sdf')
    print("The least number of stops to get from " + path_oma_sdf[0] + " to " + path_oma_sdf[-1] + " is " +
          str(len(path_oma_sdf)) + ".")
    print("Here is your route: ")
    print(path_oma_sdf)
    print("\n")

    # bwi to slc to pwm
    path_bwi_slc = bfs_shortest_path(graph, 'bwi', 'slc')
    path_slc_pwm = bfs_shortest_path(graph, 'slc', 'pwm')
    path_bwi_slc_pwm = path_bwi_slc + path_slc_pwm
    print("The least number of stops to get from " + path_bwi_slc[0] + " to " + path_bwi_slc[-1] + " is " +
          str(len(path_bwi_slc)) + ".")
    print("The least number of stops to get from " + path_slc_pwm[0] + " to " + path_slc_pwm[-1] + " is " +
          str(len(path_slc_pwm)) + ".")
    print("Here is your route: ")
    print(path_bwi_slc_pwm)
    print("\n")

    # bze to pwm
    path_bze_pwm = bfs_shortest_path(graph, 'bze', 'pwm')
    print("The least number of stops to get from " + path_bze_pwm[0] + " to " + path_bze_pwm[-1] + " is " +
          str(len(path_bze_pwm)) + ".")
    print("Here is your route: ")
    print(path_bze_pwm)
    print("\n")


if __name__ == "__main__":
    main()
