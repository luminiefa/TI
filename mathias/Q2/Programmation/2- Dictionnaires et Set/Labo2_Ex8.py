def common_pairs(dico1, dico2):
    return [( dico1.items() & dico2.items() )]


dico1 = {"Pain" : 4, "Fraises" : 3, "Chips" : 2, "Chocolat" : 1}
dico2 = {"Pain" : 4, "Fraises" : 3, "Lait" : 5}

print(common_pairs(dico1, dico2))
