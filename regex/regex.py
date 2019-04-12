import re
#from tdda import rexpy
from tdda.rexpy import *
import helpers

def analyze_column(values, current_dict=None, sample_size=10, new_col_name='new_label'):
    THRESHOLD = 0.5
    samples = helpers.get_unique_samples(values, sample_size)

    more_digits = helpers.is_more_digits(samples)
    
    if more_digits:
        if current_dict:
            for key in current_dict:
                count = 0
                for sample in samples:
                    match = re.search(current_dict[key], sample)
                    if match:
                        count += 1
                        
                relative_accuracy = count / len(samples)
                print('Regex: ', key, '; Accuracy: ', relative_accuracy)
                if relative_accuracy > THRESHOLD:
                    return current_dict, key
                
        new_regex = rexpy.extract(samples)
        
        if len(new_regex) == 1: # Handle case with more than 1 regex?
            current_dict[new_col_name] = new_regex[0]
            return current_dict, new_col_name
        
    return current_dict, None