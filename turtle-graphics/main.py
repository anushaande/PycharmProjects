from prettytable import PrettyTable
table = PrettyTable()

table.add_column("PokemonName", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"], align="l")
print(table)

