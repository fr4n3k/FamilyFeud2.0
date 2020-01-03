inv={}
def display_inventory(inv):
    inv={"rope": 1, "torch": 2, "gold coin": 42, "arrow":12}
    print("my inventory is", inv)

def add_to_inventory():
    dragon_loot={"gold coin":10, "dagger":1, "ruby":2, "gold apple":8}
    print("dragon inventory will be add to my inventory. it's my loot: ", dragon_loot)
    #if "dagger" not in inv:
        #inv["dagger"]=0
    #if "ruby" not in inv:
        #inv["ruby"]=0

    #for k, v in  inv.items():
        #for o, p in dragon_loot.items():
            #if o in inv.keys():
                #inv[o]+=dragon_loot[o]

    for key in dragon_loot.keys():
        if key in inv.keys():
            inv[key]+=dragon_loot[key]
        else:
            inv[key]=dragon_loot[key]#tutaj przyporzadkowuje klucz do klucza
        



    print("now i have a much more of items:=):" , inv)

def main():
    display_inventory(inv)
    add_to_inventory()

main()

            


        


