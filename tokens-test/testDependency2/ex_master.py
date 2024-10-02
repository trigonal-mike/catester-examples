#$META testDependencies ../testDependency1/ex.py
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from testDependency1.ex import add
x = add(1, 2)
#$VARIABLETEST test-unit2
#$TESTVAR x
