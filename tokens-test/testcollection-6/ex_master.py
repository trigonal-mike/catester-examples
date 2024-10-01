var1 = input("Please input a number from 1 to 100: ")
var2 = input("Please input a number from 1 to 100: ")
var3 = int(var1) + int(var2)
print(f"the sum of {var1} and {var2} is {var3}")

#$VARIABLETEST test-1
#$PROPERTY inputAnswers 7
#$PROPERTY inputAnswers 8
#$TESTVAR var3
#$PROPERTY value 15

#$STDOUTTEST test-2
#$PROPERTY inputAnswers ["1", "2"]
#$TESTVAR -
#$PROPERTY qualification endsWith
#$PROPERTY pattern "the sum of 1 and 2 is 3\n"
