from sympy import *


# inputs:
# var_list is a list of the symbolic variables declared by the user.
# val_list is a list of the values corresponding to the respective variable.
# err_list is a list of the uncertainties associated with each value.
# f is the symbolic function declared by the user.

# outputs:
# f is the function evaluated with the given inputs.
# sum_of_partials ** 0.5 gives the associated uncertainty.

def uncertainty(var_list, val_list, err_list, f):
    sum_of_partials = 0
    for i in range(0, len(var_list)):
        f_partial = (diff(f, var_list[i]))
        for j in range(0, len(var_list)):
            f_partial = f_partial.subs(var_list[j], val_list[j])
        sum_of_partials = sum_of_partials + (f_partial * err_list[i]) ** 2  # sum is the uncertainty of the solution

    # Evaluate the original function
    for i in range(0, len(var_list)):
        f = f.subs(var_list[i], val_list[i])

    solution = [f, sum_of_partials ** 0.5]
    return solution
