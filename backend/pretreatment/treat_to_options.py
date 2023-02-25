import json
import ast
import pandas as pd
from functools import reduce

def intro_options(S:pd.Series):
    
    if ("]" in S[0] or "[" in S[0]):
        opt=list(map(lambda x: ast.literal_eval(x) if type(x)==str else [] , list(S) ))
        opt=set(reduce(lambda x,y: x+y,opt))
    else : 
        opt=set(list(map(lambda x: x if type(x)==str else " ", list(S) )))
        
    
    opt=dict(zip(opt,opt))
    
    return opt

