def xor(ensemble1, ensemble2):
    return ( ensemble1 | ensemble2) - ( ensemble1 & ensemble2)

print ( xor({0,1,2,3,4,5}, {1,2}) )