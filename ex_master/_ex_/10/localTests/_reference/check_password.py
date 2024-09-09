import numpy as np
import matplotlib.pyplot as plt
import string


def check_password(mypassword):
    if len(mypassword) < 8:
        print("Passwort zu kurz!")
        return

    if not any(Zeichen.isdigit() for Zeichen in mypassword):
        print("Passwort enthält keine Zahl!")
        return

    if not any(Zeichen in string.punctuation for Zeichen in mypassword):
        print("Passwort enthält keine Sonderzeichen!")
        return

    if not any(Zeichen.isupper() for Zeichen in mypassword):
        print("Passwort enthält keine Grossbuchstaben!")
        return

    for i in range(len(mypassword) - 2):
        if (
            (
                ord(mypassword[i]) + 1
                == ord(mypassword[i + 1])
                == ord(mypassword[i + 2]) - 1
            )
            or (
                ord(mypassword[i]) - 1
                == ord(mypassword[i + 1])
                == ord(mypassword[i + 2]) + 1
            )
            or (ord(mypassword[i]) == ord(mypassword[i + 1]) == ord(mypassword[i + 2]))
        ):
            print("Passwort enthält fortlaufende Zahlen oder Buchstaben!")
            return

    if len([*mypassword]) != len(set(mypassword)):
        print("Passwort enthält wiederholende Zahlen oder Buchstaben!")
        return

    print("Starkes Passwort")

    pass  # TODO: Implement function


#mypassword = "gh6Da47hg!"
#check_password(mypassword)
