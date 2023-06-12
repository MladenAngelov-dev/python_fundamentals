
# filled_atoms= []
# electron_numbers = int(input())
# # formula   2* n**2
# needed_electrons = 1
# while True:
#     atom = 2 * needed_electrons**2
#     electron_numbers -= atom
#     filled_atoms.append(atom)
#     needed_electrons += 1
#     if electron_numbers <= atom:
#         break
# print(filled_atoms)
def fill_shells(electrons):
    shells = []
    shell_number = 1 
    while electrons > 0:
        shell_capacity = 2 * shell_number**2

        if electrons >= shell_capacity:
            shells.append(shell_capacity)
            electrons -= shell_capacity
        else:
            shells.append(electrons)
            electrons = 0
        shell_number += 1
    return shells


electrons = int(input())
filled_shells = fill_shells(electrons)
print(filled_shells)
