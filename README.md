# Simple Uncertainty Calculator

## uncertainty.py
uncertainty.py finds the uncertainty propagation using SymPy.

This function takes the following inputs:

```python
uncertainty(var_list, val_list, err_list, f):
```

- "var_list" is a list of the symbolic variables declared by the user.
- "val_list" is a list of the values (int or float) corresponding to the respective variable.
- "err_list" is a list of the uncertainties (int or float) associated with each value.
- "f" is the symbolic function declared by the user.

uncertainty.py returns a length 2 list where the first element is the result of the calculation and the second element is the uncertainty.

Please check "uncertainty.ipynb" for usage examples.

## linearPlot.py
linearPlot.py finds the linear relationship between two sets of data.

This function takes the following inputs:

```python
linearPlot(x_val, x_err, y_val, y_err, title, x_label, y_label):
```

- "x_val" is a list of the values (int or float) to be plotted on the x-axis.
- "x_err" is a list of the uncertainties (int or float) corresponding to the elements in x_val.
- "y_val" is a list of the values (int or float) to be plotted on the y-axis.
- "y_err" is a list of the uncertainties (int or float) corresponding to the elements in y_val.
- "title" is a string that describes the relationship of the input data.
- "x_label" is a string that describes the x-axis values.
- "y_label" is a string that describes the y-axis values.

linearPlot.py prints the slope and y-intercept of the linear fit between the data, along with associated uncertainties. It also returns the reduced chi-squared value for goodness of fit.

Furthermore, linearPlot.py plots the data as scatter points and the best linear fit, complete with error bars. Finally, the residual plot of the deviation to the linear fit is shown. These two graphs can be revealed by using the plt.show() function from matplotlib:

```python
plt.show()
```

Please check "linearPlot.ipynb" for usage examples.
