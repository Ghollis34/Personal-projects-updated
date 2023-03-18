items_shared_between_3 = []
items_shared_between_G_C = []
items_shared_between_C_J = []
items_shared_between_G_J = []
items_for_G = []
items_for_C = []
items_for_J = []
item = []

total_cost_for_george = []
total_cost_for_charlie = []

shared_between_3_total = [sum(item / 3 for item in items_shared_between_3)]
shared_between_G_C = [sum(item / 2 for item in items_shared_between_G_C)]
shared_between_C_J = [sum(item / 2 for item in items_shared_between_C_J)]
shared_between_G_J = [sum(item / 2 for item in items_shared_between_G_J)]


total_cost_for_jacob = [sum(shared_between_3_total + shared_between_C_J + shared_between_G_J + items_for_J)]
print("The total cost for Jacob is: £" + str(total_cost_for_jacob))

total_cost_for_george = [sum(items_for_G + shared_between_3_total + shared_between_G_C + shared_between_G_J)]
print("The total cost for George is: £" + str(total_cost_for_george))

total_cost_for_charlie = [sum(items_for_C + shared_between_3_total + shared_between_C_J + shared_between_G_C)]
print("The total cost for Charlie is: £" +str(total_cost_for_charlie))
