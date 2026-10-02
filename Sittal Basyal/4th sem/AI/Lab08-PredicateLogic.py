"""
Lab 08 (i) - Program to illustrate the concept of Predicate Logic

We represent simple first-order predicate logic statements about a
domain of people, define predicates such as Human(x) and Mortal(x),
and use them to perform logical inference (e.g., the classic
syllogism: "All humans are mortal. Socrates is a human.
Therefore, Socrates is mortal.")


"""
# Lab 08(i) - Predicate Logic

people = ["Socrates", "Plato", "Aristotle", "Rex"]
Human = {"Socrates", "Plato", "Aristotle"}

def Mortal(x):
    return x in Human

print("Domain:", people)
print("Human(x):", Human)

print("\nRule: For all x, Human(x) -> Mortal(x)")
for person in people:
    print(f"Human({person}) = {person in Human} -> Mortal({person}) = {Mortal(person)}")

exists = any(Mortal(p) and p in Human for p in people)
print("\nExists x: Human(x) AND Mortal(x) ->", exists)