def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : [v] # put in a list for df creation
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }