name = input("Name: ")
surname = input("Surname: ")
university = input("University: ")
group = input("Group_name: ")
mark = input("Average mark: ")

a = "I am {} {}, I am studying at the {} with {}, my average mark is {}".format(name.capitalize(), surname.capitalize(), university.upper(), group, mark)
print(a)