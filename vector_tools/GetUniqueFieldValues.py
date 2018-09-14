def GetUniqueFieldValues(in_layer,field_name):
    '''Returns Unique Fieldvalues'''
    import numpy as np
    feature = in_layer.GetNextFeature()
    field_vals = []
    fields_unique = []
    while feature:
        field_vals.append(feature.GetFieldAsString(field_name))
        feature = in_layer.GetNextFeature()
    for i in np.unique(field_vals):
        fields_unique.append(i)
    return(fields_unique) 
    in_layer.ResetReading()
