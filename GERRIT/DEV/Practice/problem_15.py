statement = input("Enter a statement :")
statement_list = statement.split(" ")
print(statement_list)
statement_list.reverse()

ste = statement_list[:]  #way to copy a list to another i,e duplication
print(str(ste))

string_statement = " ".join(statement_list)
print(string_statement)

list_A = " ".join(['1','2','3'])

print(list_A)
