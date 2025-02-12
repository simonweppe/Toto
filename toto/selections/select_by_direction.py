"""Extract a timeseries by direction

    Parameters
    ~~~~~~~~~~

    input_array : (Panda Obj)
        The Panda dataframe.
    method: {"Custom","centred","not-centred"}
        If ``method == 'Custom'``,
            The selected timeseries will be between the ``From`` and ``To``
            direction
        If ``method == 'centered'``
            the selected timeseries will be between split into directional
            bins centered over the North direction, with directional bins of ``dir swath``
        If ``method == 'not-centred'``,
            the selected timeseries will be between split into directional
            bins centered started at 0 deg, with directional bins of ``dir swath``
    From : float
        The minimum angle direction
    To : float
        The maximum angle direction
    dir swath : float
        The intervals for each directional bins

    Examples:
    ~~~~~~~~~

    >>> df['selected']=select_by_direction.select_by_direction(df['signal'].copy(),
                       args={'From':10,'To':30,'dir swath':45,'method':'centred'})
    >>> 


"""

from ..core.toolbox import dir_interval
import pandas as pd
import numpy as np

def select_by_direction(input_array,args={'From':float,'To':float,'dir swath':float,'method':{"Custom":False,"centred": True,"not-centred":False}}):

	#method=[key for key in args['method'] if args['method'][key]][0]
	method=args['method']
	name=input_array.name
	if type(args['dir swath'])==type(list()):
		args['dir swath']=args['dir swath'][0]


	if method == 'Custom':
		interval=[args['From'],args['To']]
	else:
		interval=dir_interval(dir_swath=args['dir swath'],mode=method)
	
	input_array = pd.DataFrame(input_array)
	for k in range(0,len(interval)-1):
            if k==1 and method != 'Custom':
                if method == 'centred':
                    mask=np.logical_or(input_array[name] >= interval[k],input_array[name] <= interval[k+1])
                else:
                    mask=(input_array[name] >= interval[k]) & (input_array[name] <= interval[k+1])
                
            else:
                mask=(input_array[name] > interval[k]) & (input_array[name] <= interval[k+1])

            new_name='%s_%.1f_%.1f' % (name,interval[k],interval[k+1])
            input_array[new_name]=input_array[name].loc[mask]
            

	#del input_array[name]

	return input_array




