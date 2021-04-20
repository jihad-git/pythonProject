#def #exemple1():
#liste =["alexandre","myriam","jamel","xavier","julian","elodie","jihad","kaddour","tavia","diane","corentin","elise","ouafae","khadija","marc","slah"]
    #print(liste)

    #liste[15]="khadija"
    #liste[13]="slah"
    #print(liste)

#def swap(liste,position1=15,position2=13):
    #liste[position1], liste[position2] = liste[position2], liste[position1]
    #print(liste)
    #return liste

#swap(["alexandre","myriam","jamel","xavier","julian","elodie","jihad","kaddour","tavia","diane","corentin","elise","ouafae","khadija","marc","slah"],)

#def swap(liste,i,j):
    #liste[i],liste[j]=liste[j],liste[i]

#swap(liste,1,2)
#print(liste)

#create liste
#et1={"fantasy","thriller","horror","science-fiction","triller","hitorical","thriller","futurist"}
#print(set1)

# convert list to set
#books_list=["victor hugo","les miserables",1862,"2598 pages",\
           # "historical,fiction,tragedy",62,True,0.5]
#books_set=set(books_list)
#print(books_set)

# sample set
#A =set(["thriller","fiction","historical"])
#print(A)

#add element to set
#A.add("fantasy")
#print(A)

#remove the element from set
#A.remove("fantasy")
#print(A)

# sample sets
books_set1=set(["harry potter","hunger game","narnia","jane eyre"])
books_set2=set(["pride and prejudice", "jane eyre","hamlet","narnia"])

#print two sets
#print(books_set1,books_set2)
#print(books_set1,"\n",books_set2)
#print(books_set1,"\n",books_set2,sep="")

#find the intersections

common_elements = (books_set1 & books_set2)
print (common_elements)

books_set1.intersection(books_set2)
print(books_set1.intersection(books_set2))

#find the difference in set1 but not set2
books_set1.difference(books_set2)
print(books_set1.difference(books_set2))

books_set2.difference(books_set1)
print(books_set2.difference(books_set1))

#find the union of two sets
books_set1.union(books_set2)
print(books_set1.union(books_set2))

















#exemple1()