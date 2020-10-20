people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]

#Change "Hanna" to "Hannah"
if "Hanna" in people:
    hIndex = people.index("Hanna")
    people[hIndex] = "Hannah"

#Change "Geoffrey" to "Jeffrey"
if "Geoffrey" in people:
    gIndex = people.index("Geoffrey")
    people[gIndex] = "Jeffrey"

#Change "aparna" to "Aparna" (capitalize it)
if "aparna" in people:
    aIndex = people.index("aparna")
    people[aIndex] = "aparna".capitalize()