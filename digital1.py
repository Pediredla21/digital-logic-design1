from itertools import combinations

# Define functions for handling minterms and prime implicants
def generate_minterms(name):
    ascii_codes = [ord(char) for char in name.upper()]
    minterms = set()
    for code in ascii_codes:
        for digit in str(code):
            minterms.add(int(digit))
    return list(minterms)

def binary_representation(minterm, num_vars):
    return format(minterm, f'0{num_vars}b')

def combine_terms(term1, term2):
    difference = sum(1 for a, b in zip(term1, term2) if a != b)
    if difference == 1:
        return ''.join('-' if a != b else a for a, b in zip(term1, term2))
    return None

def find_prime_implicants(minterms, num_vars):
    terms = [binary_representation(minterm, num_vars) for minterm in minterms]
    prime_implicants = set()
    while terms:
        new_terms = set()
        marked = set()
        for term1, term2 in combinations(terms, 2):
            combined = combine_terms(term1, term2)
            if combined:
                new_terms.add(combined)
                marked.add(term1)
                marked.add(term2)
        prime_implicants.update(term for term in terms if term not in marked)
        terms = list(new_terms)
    return list(prime_implicants)

def find_essential_prime_implicants(minterms, prime_implicants):
    coverage = {minterm: [] for minterm in minterms}
    for prime in prime_implicants:
        for minterm in minterms:
            binary_minterm = binary_representation(minterm, len(prime))
            if all(p == '-' or p == m for p, m in zip(prime, binary_minterm)):
                coverage[minterm].append(prime)
    essential_prime_implicants = set()
    for minterm, primes in coverage.items():
        if len(primes) == 1:
            essential_prime_implicants.add(primes[0])
    return list(essential_prime_implicants)

def minimize_expression(minterms, essential_prime_implicants, num_vars, variables):
    minimized_terms = []
    for implicant in essential_prime_implicants:
        term = ''.join(
            variables[i] + ("'" if bit == '0' else '')
            for i, bit in enumerate(implicant) if bit != '-'
        )
        minimized_terms.append(term)
    minimized_expression = " + ".join(minimized_terms)
    return minimized_expression

# Part (a)
name_a = "BHAVANI"
minterms_a = generate_minterms(name_a)
num_vars_a = 4
variables_a = "ABCD"

prime_implicants_a = find_prime_implicants(minterms_a, num_vars_a)
essential_prime_implicants_a = find_essential_prime_implicants(minterms_a, prime_implicants_a)
minimized_expression_a = minimize_expression(minterms_a, essential_prime_implicants_a, num_vars_a, variables_a)

print("Part (a):")
print("Minterms:", minterms_a)
print("Prime Implicants:", prime_implicants_a)
print("Essential Prime Implicants:", essential_prime_implicants_a)
print("Minimized SOP Expression:", minimized_expression_a)
print()

# Part (b)
minterms_b = [0, 5, 7, 8, 9, 12, 13, 23, 24, 25, 28, 29, 37, 40, 42, 44, 46, 55, 56, 57, 60, 61]
num_vars_b = 6
variables_b = "ABCDEF"

prime_implicants_b = find_prime_implicants(minterms_b, num_vars_b)
essential_prime_implicants_b = find_essential_prime_implicants(minterms_b, prime_implicants_b)
minimized_expression_b = minimize_expression(minterms_b, essential_prime_implicants_b, num_vars_b, variables_b)

print("Part (b):")
print("Minterms:", minterms_b)
print("Prime Implicants:", prime_implicants_b)
print("Essential Prime Implicants:", essential_prime_implicants_b)
print("Minimized SOP Expression:", minimized_expression_b)

# Adding the 7th prime implicant to the minimized expression for part (b)
additional_prime_implicant = find_prime_implicants([7], num_vars_b)
essential_prime_implicants_b += additional_prime_implicant
minimized_expression_b_updated = minimize_expression(minterms_b, essential_prime_implicants_b, num_vars_b, variables_b)

print("\nPart (b) with 7th Prime Implicant Added:")
print("Updated Minimized SOP Expression:", minimized_expression_b_updated)