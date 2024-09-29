x = int(input('Gib "123" ein und drücke enter: '))
y = x + 1
print(f'{x} plus 1 ist {y}')

#$VARIABLETEST stdin_stdout1
#$PROPERTY inputAnswers ["123"]
#$TESTVAR x
#$PROPERTY value 123
#$TESTVAR y
#$PROPERTY value 124

#$STDOUTTEST stdin_stdout2
#$PROPERTY inputAnswers ["123"]
#$TESTVAR stdout
#$PROPERTY qualification contains
#$PROPERTY pattern "123 plus 1 ist 124"

#$STDOUTTEST stdin_stdout2
#$PROPERTY inputAnswers ["123"]
#$TESTVAR stdout
#$PROPERTY qualification endsWith
#$PROPERTY pattern "123 plus 1 ist 124\n"

#$STDOUTTEST stdin_stdout2
#$PROPERTY inputAnswers ["123"]
#$TESTVAR stdout
#$PROPERTY qualification matches
#$PROPERTY pattern "Gib \"123\" ein und drücke enter: 123 plus 1 ist 124\n"
