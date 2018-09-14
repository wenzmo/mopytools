def TransformGeometry(geometry, target_sref):
    '''Returns cloned geometry, which is transformed to target spatial reference'''
    import osr
    from pyproj import Proj, transform
    geom_sref= geometry.GetSpatialReference()
    transform = osr.CoordinateTransformation(geom_sref, target_sref)
    geom_trans = geometry.Clone()
    geom_trans.Transform(transform)
    return geom_trans 
