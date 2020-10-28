
PersonAndPets = [
	{
		"name": "John Doe",
		"pets": [
			{"name": "Rooster"},
			{"name": "Dog"}
		]
	},
	{
		"name": "Luke Skywalker",
		"pets": [
			{"name": "Duck"},
			{"name": "Camel"}
		]
	},
	{
		"name": "Padme Amidal",
		"pets": [
			{"name": "Bird"},
			{"name": "Fish"}
		]
	}
]

#bikin class personpet, person, pet
#menampilkan list data person dan pet
#menampilkan pet by person
#menampilkan person by pet
#menampilkan true or false, apakah jon punya pet anu, apakah pet anu milik john


class PersonPets:
    def __init__(self, person=None, pets=None):
        self.person = person
        self.pets = pets
        
    def getPetByPerson(self):
        for x in personAndPets:
            if x["name"] == self.person:
                print(x)
                
                
    def getPetAja(self):
        for x in personAndets:
            if x["name"] == self.person:
                for p in x["pets"]:
                    print(p["name"])
                    #print(p)
                    
                    
    def getPersonByPet(self):
        for x in personAndPets:
            if (x["name"] == self.person):
                for p in x["name"] == self.pets:
                    print("True")
                    fstartApp()
                
        print("False")
        
        
#cekMilik1 = PersonAndPets(person = "John Doe", pets = "Dog")
#cekMilik1.cekMilik()


def fstartApp():
    print("\n==========")
    print("what to do? (Tulis Angka)untuk Lanjut!)")
    print("1. Show all data on the list!")
    print("2. Show Pet By Person!")
    print("3. Show Person By Pet!")
    print("4. Cek Milik!\n")
    
    
    
    pilih = None
    pilih = input("")
    if(pilih == "1"):
        print("1. Show all data on the list!")
        #menampilkan list person dan pet
        print("\n#menampilkan list person dan pet")
        for x in personAndPets:
            print(x)
        fstartApp()
        
        
    elif(pilih == "2"):
        print("2. Show Pet By Person!")
        for listname in personAndPets:
            print(">> " + listName["name"])
        print("\n")
        namePerson = input("Type the name person: ")
        for listname in personAndPets:
            if (namePerson == listName["name"]):
                print("Pets owned by %s is: " % namePerson)
                petAja = PersonPets(person = namePerson)
                petAja.getPetAja()
                fstartApp()
                
        print("Liat yang bener! ULANGI LAGI")
        fstartApp()
        """
        print("Pets owned by %s is: " % namePerson)
        petAja = PersonPets(person = namePerson)
        petAja.getPetAja()
        fstartApp()
        """
        
    elif(pilih == "3"):
        print("3. Show Person by Pet!")
        for x in personAndPets:
            for namePets in x["pets"]:
                print(">> " + namePets["name"])
                #print(namePets)
                #print(namaPets.value())
        print("\n")
        namePet = input("Type the name pet: ")
        for x in personAndPets:
            for namePets in x["pets"]:
                if (namePet == namePets["name"]):
                    print("Person who owned %s is: " % namePet)
                    getPerson = PersonPets(pets = namePet)
                    getPerson.getPersonByPet()
                    fstartApp()
                    
                    
        print("Liat yang bener! ULANGI LAGI")
        fstartApp()
        """
        print("Person who owned %s is: " % namePet)
        getPerson = PersonPets(pets = namePet)
        getPerson.getPersonByPet()
        fstartApp()
        """
        
    elif(pilih == "4"):
        print("4. Cek Milik!")
        namePerson = input("Type name person: ")
        namePets = input("Type name pet: ")
        cekMilik1 = PersonPets(person = namePerson, pets = namePets)
        cekMilik1.cekMilik()
        
        
    else:
        print("Baca yang bener!")
        
fstartApp()



"""

#memnampilkan list person dan pet
print("\n#menampilkan list person dan pet")
for x in personAndPets:
    print(x)
    
    
#menampilkan pet by person
print("\n#menampilkan pet by person")
getPet = PersonalPets(person = "Padme Amidala")
getPet.getPetByPerson()


#menampilkan pet aja
print("\n#menampilkan pet aja")
petAja = PersonPet(person = "Padem Amidala")
petAja.getPetAja()


#menampilkan person by pet
print("\n#menampilkan person by pet")
getPerson = PersonPets(pets = "Fish")
getPerson.getPersonByPet()
"""


"""
for x in personAndPets:
    for n in x["name"]:
        print(n)
        
        
#Menampilkan semua pet didalam list
print("\n#menampilkan semua pet didalam list")
for x in personAndPets:
    for p in x["pets"]:
        print(p)
        
        
#Menampilkan pets by name
print("\n#menampilkan pets by name")
for x in personAndPets:
    if x["name"] == "Padme Amidala":
        for p in x["pets"]:
            print(p)

            
"""
        
        

	
	
	
	
	
	

