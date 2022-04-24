# Order a group of passengers by their loyalty number so they can board based on it.

class Passenger:
    def __init__(self, name, pnr, loyalty_num):
        self.name = name
        self.pnr = pnr
        self.loyalty_num = loyalty_num
def init():
    list = []
    
    list.append(Passenger('Joe', 'ABC123', 14))
    list.append(Passenger('Zach', 'XYZ324', 16))
    list.append(Passenger('Chris', 'NBA091', 1))
    list.append(Passenger('Rob', 'BAF121', 9))
    list.append(Passenger('Joe Jr', 'ABC123', 77))
    list.append(Passenger('Joe Sr', 'ABC123', 3))
    list.append(Passenger('Wyatt', 'XYBZ2354', 99))
    list.append(Passenger('Karen', 'BADF123NA', 115))
    list.append(Passenger('Jonathan', 'DFB12A1', 4))
    return list

def main():
    passenger_list = init()
    passenger_map = dict()
    passenger_list = sorted(passenger_list, key=lambda x: x.loyalty_num)
    
    # Sort the list based on Loyalty Nums alone.
    # for pers in passenger_list:
    #     print(f'{pers.name}, {pers.loyalty_num}')
        
    for i, person in enumerate(passenger_list):
        
        # If we have already seen the PNR, and their Loyalty Num is better, we update that person's loyalty number because they are on a shared reservation.
        if person.pnr in passenger_map:
            if person.loyalty_num > passenger_map[person.pnr].loyalty_num:
                passenger_list[i].loyalty_num = passenger_map[person.pnr].loyalty_num
                
            # We don't need this else because we added the sort before the loop. It would only update the dictionary, so we'd have to loop through the list a second time.
            # else:
            #     passenger_map[person.pnr].loyalty_num = passenger_list[i].loyalty_num
        else:
            passenger_map[person.pnr] = person
            
    # Sort the list based on Loyalty Number.
    passenger_list = sorted(passenger_list, key=lambda x: x.loyalty_num)
    
    # Verify the list looks correct after updating Loyalty Numbers.
    # print('After Sorting with new Loyalty Nums') 
    # for pers in passenger_list:
    #     print(f'{pers.name}, {pers.loyalty_num}')
    

if __name__ == "__main__":
    main()
