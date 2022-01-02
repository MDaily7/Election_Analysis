counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
if "Arapahoe" and "Jefferson" in counties:
    print("Arapahoe and Jefferson are in counties")
else:
    print("Arapahoe and Jefferson are not in counties")
if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else: 
    print("Neither Arapahoe or El Paso are in the list of counties")
    