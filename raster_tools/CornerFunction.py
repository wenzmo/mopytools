def CornerFunction(in_path):
    import gdal
    from mopytools import mopyRT
    #create empty result list
    result_list = []
    
    # empty lists for each coordinate part
    ulx_all = []
    uly_all = []
    lrx_all = []
    lry_all = []

    for ras in in_path:
        # get raster
        src = gdal.Open(ras)
        sr_raster = mopyRT.SpatialReferenceFromRaster(src)
        # get upper left x and upper left y plus resolutions
        # ulx, uly is the upper left corner, lrx, lry is the lower right corner
        ulx, xres, xskew, uly, yskew, yres  = src.GetGeoTransform()
        # calculate lower right x and lower right y
        lrx = ulx + (src.RasterXSize * xres)
        lry = uly + (src.RasterYSize * yres)
        # add each coordinate to the corresponding lists
        ulx_all.append(ulx)
        uly_all.append(uly)
        lrx_all.append(lrx)
        lry_all.append(lry)
        
    # add the result coordinates to the result list
    result_list.append(("lower left x=", max(ulx_all), "y=", min(lry_all)))
    result_list.append(("upper left x=", max(ulx_all), "y=", max(uly_all)))
    result_list.append(("lower right x=", min(lrx_all), "y=", min(lry_all)))
    result_list.append(("upper right x=", min(lrx_all), "y=", max(uly_all)))
    
    for p in result_list:
        print(p)
    #return result_list
    return result_list 
