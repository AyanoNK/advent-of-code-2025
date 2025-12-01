from client import AdventOfCodeClient

client = AdventOfCodeClient()

my_data = client.get_input(year=2025, day=1)

print(my_data)
