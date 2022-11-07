# In chemistry, the molar mass of a substance is the mass in grams of one mole of the substance (grams / mole). A mole is simply a fixed very large quantity, specifically 602,214,076,000,000,000,000,000 (usually written as 6.02214076 × 1023). A molar mass calculator is a program that computes the molar mass of a substance and the number of moles of a sample of that substance. To use a molar mass calculator, a chemist enters two inputs:

# The formula for a molecule, such as H2O (water) or C6H12O6 (glucose)
# The mass in grams of a sample of the substance, such as 3.71
# The calculator computes the molar mass of the molecule by doing the following for each element in the formula:

# Sum the number of atoms of each element in the formula
# Find the atomic mass of each element
# Multiply the number of atoms by their atomic mass
# Add the product into the molar mass of the molecule
# Then the calculator uses this formula to compute the number of moles in the sample:

# number_of_moles = 
# sample_mass
# molar_mass
# Finally, the calculator prints two results for the chemist to see:

# the molar mass
# # the number of moles

element_weights = {
    'H': 1.00794,
    'He': 4.002602,
    'C': 12.011,
    'O': 15.999,
    'Ts': 294.0,
    'Og': 294.0,
}

# def tokenize(string):
#     position = 0
#     tokens = []
#     striter = iter(string)

#     character = next(striter)

#     while True:
#         try:
#             token = character

#             if character in "()":
#                 character = next(striter)
#             elif character.isnumeric():
#                 while (character := next(striter)).isnumeric():
#                     token += character

#             elif character.isupper():
#                 while (character := next(striter)).islower():
#                     token += character
#             else:
#                 raise ValueError("Can't parse")

#             tokens.append(token)


#         except StopIteration:
#             tokens.append(token)
#             tokens.append("EOF")
#             return tokens

# def get_composition(tokens_list):
#     composition = {}

#     tokens = iter(tokens_list)
#     token = next(tokens)

#     while True:
#         if(token == "EOF"):
#             break

#         num_parens = 0

#         if token == "(":
#             num_parens = 1
#             substr_tokens = []

#             while num_parens > 0:
#                 token = next(tokens)

#                 if token == "EOF":
#                     raise ValueError(f"Unbalanced Parens, tokens: {tokens_list}")
#                 elif token == "(":
#                     num_parens += 1
#                 elif token == ")":
#                     num_parens -= 1

#                 if (num_parens > 0):
#                     substr_tokens.append(token)

#             substr_tokens.append("EOF")

#             substr_composition = get_composition(substr_tokens)

#             if (token := next(tokens)).isnumeric():
#                 substr_composition = {k: int(token) * v for k,v in substr_composition.items()}

#             for k,v in substr_composition.items():
#                 if k in composition:
#                     composition[k] += v
#                 else:
#                     composition[k] = v
#             break

#         if token == ")":
#             raise ValueError(f"Unbalanced Parens, tokens: {tokens_list}")

#         if token not in element_weights:
#             raise ValueError(f"Can't find element {token}, tokens {tokens_list}")

#         element = token

#         if (token := next(tokens)).isnumeric():
#             element_count = int(token)
#             token = next(tokens)
#         else:
#             element_count = 1

#         if element in composition:
#             composition[element] += element_count
#         else:
#             composition[element] = element_count

#     return composition
    
# def convertToAMU(element_count):
#     return sum(element_weights[k] * v for k,v in element_count.items())

# if __name__ == "__main__":
#     import sys

#     if(len(sys.argv) > 1):
#         print(convertToAMU(get_composition(tokenize(sys.argv[1]))))
#     else:
#         print(f"Usage: {sys.argv[0]} [chemical_formula]")