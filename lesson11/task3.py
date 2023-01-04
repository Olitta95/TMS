import re

proverka = re.compile(r'([A-Za-z0-9]*[\W])*[A-Za-z0-9]+@[A-Za-z0-9_-]{,63}+(\.[A-Z|a-z]{2,})+')
def function_email(email):
    if re.fullmatch(proverka, email):
      print("True email")
    else:
      print("False email")
function_email("Les^n!ik*ova1995@majhjhjhjh13434433453_43-54il.com")
function_email("Лесниковф@ma_il.com")


