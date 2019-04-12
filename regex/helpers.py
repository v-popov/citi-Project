# Returns min(n, len(unique(values))) unique values
# values : list of strings
def get_unique_samples(values, n):
    unique_values = set(values)
    
    result = []
    while unique_values and len(result) < n:
        result.append(unique_values.pop())
        
    return result

# Imputs list of values 
# Ouputs 0 if there are more than a half symbols that are characters in the word and 1 otherwise
def is_more_digits(values):
    more_digits = True
    
    for value in values:
        more_digits *= sum(c.isalpha() for c in str(value)) <= len(str(value)) / 2
        
    return more_digits