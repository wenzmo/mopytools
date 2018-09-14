def GetFieldNames(input_layer):
    '''Returns Field names of shapefiles'''
    ldefn = input_layer.GetLayerDefn()
    schema = []
    for n in range(ldefn.GetFieldCount()):
        fdefn = ldefn.GetFieldDefn(n)
        schema.append(fdefn.name)
    return(schema)
    input_layer.ResetReading()
