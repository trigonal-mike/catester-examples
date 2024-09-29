def check_password(x):
    if len(x) < 10:
        print("abc")
    else:
        print("ok")

#$STDOUTTEST test1
#$PROPERTY setUpCode ["check_password('1234567890')"]
#$TESTVAR stdout
#$PROPERTY qualification startsWith
#$PROPERTY pattern "ok"

