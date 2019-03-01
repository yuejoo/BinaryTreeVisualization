def get_depth(treelist):
    depth, count = 0, 1
    while count < len(treelist):
        depth, count = depth + 1, count*2
    return depth

def create_nodes(treelist):
    cx,cy = 0,0
    row,col = 0,0
    depth = get_depth(treelist)
    spacex, spacey = 100,100
    nodes = []

    for nodeId, node in enumerate(treelist):
        x = cx + spacex*col*(2**(depth-row))
        y = cy + spacey*row     
        if node != None:
            nodes.append([node,x,y,nodeId])

        if 2**row == col+1: 
            row,col = row + 1,0
            cx = cx - spacex*(2**(depth-row))/2
        else:
            col = col + 1

    return nodes

def create_elements(treelist):
    nodes = create_nodes(treelist)

    edges = []
    length = len(treelist)
    for index in range(length):
        left = index*2 + 1
        right = index*2 + 2
        if treelist[index] != None:
            if left < length and treelist[left] != None:
                edges.append([index, left])
            if right < length and treelist[right] != None:
                edges.append([index, right])

    nodes = [
        {
            'data': {'id': index, 'label': short}, 'position': {'x': x, 'y': y} 
        }
        for short,x,y,index in nodes
    ]

    edges = [
        {'data': {'source': source, 'target': target}}
        for source, target in edges
    ]
    return nodes + edges