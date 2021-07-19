
import isotonic2pmml
import numpy as np
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state

n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50. * np.log1p(np.arange(n))

###############################################################################
# Fit IsotonicRegression
ir = IsotonicRegression()
y_ = ir.fit_transform(x, y)

# Export to PMML.
isotonic2pmml.topmml(x,
                     y_,
                     datafield_name='x',
                     targetfield_name='y',
                     outputfile='test.pmml')
