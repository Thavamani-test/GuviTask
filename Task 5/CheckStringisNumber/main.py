#Using st.isdigit() to handle only integers
Number = lambda st: st.isdigit()

#Using st.replace() to handle float and negative numbers
Number = lambda st: st.replace('.', '', 1).replace('-', '', 1).isdigit()

#Output
print(Number("123"))
print(Number("12.3"))
print(Number("-12.3"))
print(Number("Text"))

