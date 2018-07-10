def PointToRast(point,gt):
    x, y = point.GetX(), point.GetY()
    px = int((x - gt[0]) / gt[1])
    py = int((y - gt[3]) / gt[5])
    return(px, py)