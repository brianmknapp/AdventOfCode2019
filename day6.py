from collections import defaultdict

from anytree import Node, RenderTree, Walker


def parse_orbits(all_orbits):
    nodes = defaultdict(Node)
    for orbital_pair in all_orbits:
        parent = nodes.setdefault(orbital_pair[0], Node(orbital_pair[0]))
        child = nodes.setdefault(orbital_pair[1], Node(orbital_pair[1]))
        child.parent = parent
    return nodes


def walk_nodes(_path, exceptions=None):
    count = 0
    if exceptions is None:
        exceptions = []
    if isinstance(_path, Node):
        return 1
    for node in _path:
        if node.name not in exceptions:
            count += 1
    return count


if __name__ == '__main__':
    with open('data/day6.txt') as f:
        lines = f.read().splitlines()
    orbits = [i.split(')') for i in lines]
    orbital_dict = parse_orbits(orbits)
    orbital_tree = RenderTree(orbital_dict['COM'])
    orbit_count = 0
    for k, v in orbital_dict.items():
        orbit_count += v.depth
    w = Walker()
    walked_path = w.walk(orbital_dict['YOU'], orbital_dict['SAN'])
    walked_path_nodes = 0
    for path in walked_path:
        walked_path_nodes += walk_nodes(path, ['YOU', orbital_dict['YOU'].parent.name, 'SAN'])
    print('debug')
