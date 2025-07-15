#a = "Ben stokes rocked yesterday gill shocked"
#b = a.replace("Ben","Archer")
#print(b)


#a = " ".join(str (i) for i in range(10))
#print(a)


#s="Shreya Shekhar"
#a=" ".join(i for i in s if i not in "aeoiu")
#print(a)

s="MONICA%MONICA&FROM*COOLIE"
a=" ".join(i for i in s if not i.isalnum())
print(a)