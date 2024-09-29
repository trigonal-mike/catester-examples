import string

#$META title "Password Validator"

#$META studentSubmissionFiles ./check_password.py

#$STDOUTTEST test1
#$PROPERTY entryPoint "check_password.py"
#$PROPERTY setUpCode ["check_password('abc')"]
#$TESTVAR stdout
#$PROPERTY qualification regexp
#$PROPERTY pattern .*Passwort zu kurz!.*


#$STDOUTTEST test2
#$PROPERTY entryPoint "check_password.py"
#$PROPERTY setUpCode ["check_password('neuespasswort')"]
#$TESTVAR stdout
#$PROPERTY qualification startsWith
#$PROPERTY pattern "Passwort enthält keine Zahl!"


#$STDOUTTEST test3
#$PROPERTY entryPoint "check_password.py"
#$PROPERTY setUpCode ["check_password('neuespasswort2')"]
#$TESTVAR stdout
#$PROPERTY qualification startsWith
#$PROPERTY pattern "Passwort enthält kein Sonderzeichen!"


#$STDOUTTEST test4
#$PROPERTY entryPoint "check_password.py"
#$PROPERTY setUpCode ["check_password('neuespasswort!2')"]
#$TESTVAR stdout
#$PROPERTY qualification startsWith
#$PROPERTY pattern "Passwort enthält keine Grossbuchstaben!"


#$STDOUTTEST test5
#$PROPERTY entryPoint "check_password.py"
#$PROPERTY setUpCode ["check_password('neuesPasswort!2')"]
#$TESTVAR stdout
#$PROPERTY qualification startsWith
#$PROPERTY pattern "Starkes Passwort"
