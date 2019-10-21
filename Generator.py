import sys
from itertools import permutations
def unique_perms(series):
  s = set()
  for p in permutations(series):
    s.add(p)
  return s

#just code I want to save
#print(sorted(unique_perms('1122')))
#print(sorted(set("".join(p) for p in permutations('1122'))))

#passed variables
border1 = int(sys.argv[1]) #10 #Borders -- Use these as cutoffs where the integer you assign is the number of integers to the left of the cutoff.
border2 = int(sys.argv[2]) #30
border3 = int(sys.argv[3]) #60
passedi = int(sys.argv[4]) #Number of inactive orbitals (all will be below border1)
passeda = int(sys.argv[5]) #Number of active orbitals (all will be below border2)

#calculated variables
passeds = border3-passedi-passeda #Number of secondary orbitals

#initialization
bag1 = "" #String of length (border1) which will contain (passedi) i's and (border1-passedi) 0's.
bag2 = "" #String of length (border2-passedi) which will contain (passeda) a's and (border2-passedi-passeda) s's. 
#Filling bag1 to draw from to create permutation up to border1. This only stores "i"s, and leaves the rest of the border1 spots as empty, represented by "0".
for i in range(0,passedi):
  bag1 += "i"
while len(bag1) < border1:
  bag1 += "0"  
#print(bag1)
#Filling bag2 to draw from to create permutation up to border2. This has length greater than (border2-border1), because there are empty spots that must be filled.
for i in range(0,passeda):
  bag2 += "a"
while len(bag2) < border2-passedi:
  bag2 += "s"
#print(bag2)

#generating all permutations
#Generating all permutations of i's and 0's to be placed on the left of border1
list1=[] #Generating, but also converting, the permutation tuples "ptuples" to "plists" and putting them all in list1. Would use print(sorted(unique_perms(bag1))) but then the list elements are tuples, which are immutable
for ptuple in sorted(unique_perms(bag1)):
  plist = []
  for pelement in ptuple:
    plist.append(pelement)
  list1.append(plist)
print("bag1perms done")
#Generating all permutations of a's and s's to overwrite the 0's and fill up to border2.
list2=[] #Generating, but also converting, the permutation tuples "ptuples" to "plists" and putting them all in list2
for ptuple in sorted(unique_perms(bag2)):
  plist = []
  for pelement in ptuple:
    plist.append(pelement)
  list2.append(plist)
print("bag2perms done")
#double check -- You can use these to give a lookover and make sure things look good. 
#print(list1)
#print(list2)

list3 = [] #This will be the list of all solutions

#replace the 0s in each list1 permutation with the first digits from the list2 permutation for all list2 permutations. Then fill up to border3 length with s's. Do this with all 
for longitem in list2:
  for itemlist in list1:
    j=0
    item = itemlist.copy()
    for i in range(0,len(item)): #Filling up the 0's in the list1 permutation with the first elements from the list2 permutation
      if item[i] == "0":
        item[i] = longitem[j]
        j+=1
    item = item+longitem[j:] #Filling up to border2 with the leftovers from the list2 permutation
    while len(item) < border3: #Filling up to border3 with s's
      item.append("s")
    list3.append(",".join(item))

#print(list3)
with open("Generated.txt", "w+") as outf:
  outf.write("border1 = " + str(border1) + "\n")
  outf.write("border2 = " + str(border2) + "\n")
  outf.write("border3 = " + str(border3) + "\n")
  outf.write("passedi = " + str(passedi) + "\n")
  outf.write("passeda = " + str(passeda) + "\n")
  outf.write("listlen = " + str(len(list3)) + "\n")
  for item in list3:
    outf.write(item)
    outf.write("\n")

#tests -- Some tests I want to keep
#print("length of list is: " + str(len(list3))) #Should be C(border1, passedi)*C(border2-passedi, passeda)            
#print(any(list3.count(x) > 1 for x in list3)) #Use on small lists. Should return False, indicating that there are no duplicates in list3
