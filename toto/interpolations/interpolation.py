""" Fill NaN values using an interpolation method..


    Parameters
    ~~~~~~~~~~

    input_array : (Panda Obj)
        The Panda dataframe.

    Note
    ~~~~
	See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
"""
def interpolation(input_array,args={'limit':int(),'method':{"linear": True,"time":False,\
						"index":False, "pad":False,"nearest":False,"zero":True,\
						"slinear":False,"quadratic":False,"cubic":False,"spline":False,\
						"barycentric":False,"polynomial":False},\
						'limit direction':{'forward':True,'backward':False,'Both':False},\
						'limit area':{'None':True,'inside':False,'outside':False}}):

	limit=args['limit']
	#method=[key for key in args['method'] if args['method'][key]][0]
	method=args['method']
	limit_direction=args['limit direction']
	#limit_direction=[key for key in args['limit direction'] if args['limit direction'][key]][0]
	limit_area=args['limit area']
	#limit_area=[key for key in args['limit area'] if args['limit area'][key]][0]
	if limit:
		if method=='ffill' or method=='pad':
			args['limit direction']='forward'
		elif method=='bfill' or method=='backfill':
			args['limit direction']='backward'

	if limit_area=='None':
		limit_area=None



	input_array=input_array.interpolate(method=method, axis=0, limit=limit, limit_direction=limit_direction, limit_area=limit_area)

	return input_array