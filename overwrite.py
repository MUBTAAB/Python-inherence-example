# overwrite methods with __init__ problems
# via Péter Paczko

from sklearn.linear_model import LinearRegression
class LinearRegressionExt(object):
    def __init__(self, *args, **kwargs):
        if kwargs.get('peter') != None:
            print(kwargs.get('peter', 3))
            del(kwargs['peter'])
        self.regression = LinearRegression(*args, **kwargs)
    
    def reference(self):
        return self.regression
