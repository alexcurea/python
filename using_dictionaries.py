elements = {1: "Hydrogen", 2: "Helium", 3: "Lithium", 4: "Beryllium", 5: "Boron", 6: "Carbon", 7: "Nitrogen", 8: "Oxygen", 9: "Fluorine", 10: "Neon", 11: "Sodium", 12: "Magnesium", 13: "Aluminum", 14: "Silicon", 15: "Phosphorus", 16: "Sulfur", 17: "Chlorine", 18: "Argon", 19: "Potassium", 20: "Calcium", 21: "Scandium", 22: "Titanium"}

reading = {}
reading.update({"catalyst": elements.pop(6)})
reading.update({"core": elements.pop(14)})
reading.update({"byproduct": elements.pop(8)})

for key, value in reading.items():
  print("Your " + key + " element is " + str(value) + ".")
