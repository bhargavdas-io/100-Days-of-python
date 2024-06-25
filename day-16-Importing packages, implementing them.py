import prettytable

table = prettytable.PrettyTable()

table.add_column("Games",["Age of Empires","Age of Mythology","Rise of Nations"],align='l')
table.add_column("Release Year",["1997","2002","2003"])
table.add_column("Copies sold",[" 25 mill","> 1 million","> 1 million"],align='l')


print(table)