
#$VARIABLETEST rng-test
#$TESTVAR seed
#$TESTVAR x1

import numpy as np

seed = 123
rng = np.random.default_rng(seed)
x1 = rng.random()
