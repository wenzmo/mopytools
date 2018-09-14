def SpatialReferenceFromRaster(ds):
    '''Returns SpatialReference from raster dataset'''
    import osr
    pr = ds.GetProjection()
    sr = osr.SpatialReference()
    sr.ImportFromWkt(pr)
    return sr
