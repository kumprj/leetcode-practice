# Order a group of passengers by their loyalty number so they can board based on it.

class Passenger:
    def __init__(self, name, pnr, loyalty_num):
        self.name = name
        self.pnr = pnr
        self.loyalty_num = loyalty_num
def init():
    list = []
    list.append(Passenger('Joe Sr', 'ABC123', 3))
    list.append(Passenger('Joe', 'ABC123', 14))
    list.append(Passenger('Zach', 'XYZ324', 16))
    list.append(Passenger('Chris', 'NBA091', 1))
    list.append(Passenger('Rob', 'BAF121', 9))
    list.append(Passenger('Joe Jr', 'ABC123', 77))
    return list

def main():
    passenger_list = init()
    passenger_map = dict()
    
    for i, person in enumerate(passenger_list):
        if person.pnr in passenger_map:
            if person.loyalty_num > passenger_map[person.pnr].loyalty_num:
                passenger_list[i].loyalty_num = passenger_map[person.pnr].loyalty_num
            else: 
                passenger_map[person.pnr].loyalty_num = passenger_list[i].loyalty_num
                
        else:
            passenger_map[person.pnr] = person
    # Sort the lsit based on Loyalty Number.
    passenger_list = sorted(passenger_list, key=lambda x: x.loyalty_num)
    
    # Verify the list looks correct.
    # for pers in passenger_list:
    #     print(pers.name)
    

if __name__ == "__main__":
    main()
