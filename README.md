# Simple Uncertainty Calculator

## uncertainty.py
This is a Python function for finding uncertainty propagation using SymPy.

The function takes the following inputs:

uncertainty(var_list, val_list, err_list, f):
- "var_list" is a list of the symbolic variables declared by the user.
- "val_list" is a list of the values corresponding to the respective variable.
- "err_list" is a list of the uncertainties associated with each value.
- "f" is the symbolic function declared by the user.

The function returns a length 2 list where the first element is the result of the calculation and the second element is the uncertainty.

Please check "uncertainty.ipynb" for usage examples.
