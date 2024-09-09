import numpy as np

x = 4.2135213
print("Hello World")
print(f"xxx{x:.2f}xxx")



#$META title "Tests"

#$STDOUTTEST printtest1
#$TESTVAR stdout
#$PROPERTY qualification regexp
#$PROPERTY pattern [\s\S]*4.21[\s\S]*
