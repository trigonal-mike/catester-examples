var1 = 1
var2 = 2
var3 = 3
#$VARIABLETEST test-1
#$PROPERTY id test1
#$TESTVAR var1
#$PROPERTY value 1

#$VARIABLETEST test-2
#$PROPERTY id test2
#$TESTVAR var2
#$PROPERTY value 99

#$VARIABLETEST test-3
#$PROPERTY id test3
#$TESTVAR var3
#$PROPERTY value 3

#$VARIABLETEST test-4
#$PROPERTY successDependency "test1"
#$TESTVAR var1
#$PROPERTY value 1

#$VARIABLETEST test-5
#$PROPERTY successDependency "test2"
#$TESTVAR var1
#$PROPERTY value 1

#$VARIABLETEST test-6
#$PROPERTY successDependency ["test1", "test2"]
#$TESTVAR var1
#$PROPERTY value 1

#$VARIABLETEST test-7
#$PROPERTY successDependency ["test1", "test3"]
#$TESTVAR var1
#$PROPERTY value 1

#$VARIABLETEST test-8
#$PROPERTY successDependency 1
#$TESTVAR var1
#$PROPERTY value 1

#$VARIABLETEST test-9
#$PROPERTY successDependency 2
#$TESTVAR var1
#$PROPERTY value 1
