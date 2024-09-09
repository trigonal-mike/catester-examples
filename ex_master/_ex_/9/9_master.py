print("fgdf dhg dfg K = 5.034fgg df")

x = "r"
if x == "red":
    y = "r"
elif x == (1,1,10):
    y= "r"
elif x == "r":
    y= "r"

print(y)
##$STDOUTTEST test
##$TESTVAR -
##$PROPERTY qualification regexp
##$PROPERTY pattern ^.*5.03(?!\d).*$

#$VARIABLETEST test
#$PROPERTY setUpCode ["if x == 'red':\n y = 'r'\nelif x == (1,1,10):\n y= 'r'\nelif x == 'r':\n y= 'r'"]
#$TESTVAR y
#$PROPERTY value "r"
