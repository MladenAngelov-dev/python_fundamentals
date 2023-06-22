class Party:
    def __init__(self) -> None:
        self.people = []
    
    def add_people(self, name):
        self.people.append(name)

    def get_party_info(self):
        party_info = {
            'going': ", ".join(self.people),
            'total': len(self.people)
        }
        result = f"Going: {party_info['going']}\nTotal: {party_info['total']}"
        return result
party = Party()

while True:
    name = input()

    if name == "End":
        break
    party.add_people(name)

print(party.get_party_info())
