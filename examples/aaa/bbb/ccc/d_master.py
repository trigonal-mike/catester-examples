import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from Week03.Unit01.unit1 import add

x = add(1, 2)

#$VARIABLETEST deep
#$TESTVAR x

#$META testDependencies ../../../Week03/Unit01/unit1.py
#$META studentSubmissionFiles ./x.py
#$META studentSubmissionFiles z\y.py
