def ReprojectPoint(geom_point, out_ref):
    inSpatialRef = geom_point.GetSpatialReference()
    coordTrans = osr.CoordinateTransformation(inSpatialRef, out_ref)
    point_rep = ogr.CreateGeometryFromWkt("POINT (" + str(geom_point.GetX()) + " " + str(geom_point.GetY()) + ")")
    point_rep.Transform(coordTrans)
    return(point_rep)