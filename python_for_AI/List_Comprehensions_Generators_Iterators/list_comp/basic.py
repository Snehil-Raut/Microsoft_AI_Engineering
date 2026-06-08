# 1. Square numbers
# Given:
# numbers = [1,2,3,4,5]
# Creae:
# [1,4,9,16,25]

# numbers = [1,2,3,4,5]
# square = [x*x for x in numbers]
# print(square)

# 2. Convert names to uppercase
# Given:
# names = ["alice", "bob", "charlie"]
# Create:
# ["ALICE", "BOB", "CHARLIE"]

# names = ["alice", "bob", "charlie"]
# upper = [s.upper() for s in names]
# print(upper)

# 4. Get even numbers
# Given:
# nums = [1,2,3,4,5,6,7,8]
# Output:
# [2,4,6,8]

# nums = [1,2,3,4,5,6,7,8]
# even = [x for x in nums if x%2==0]
# print(even)

# 11. Extract domains from emails

# Given:

# emails = ["a@gmail.com", "b@yahoo.com", "c@outlook.com"]

# Output:

# ["gmail.com", "yahoo.com", "outlook.com"]

# emails = ["a@gmail.com", "b@yahoo.com", "c@outlook.com"]
# domains = [ email.split("@")[1] for email in emails ]
# print(domains)

# 2. Flatten nested list
# Given:
# matrix = [[1,2],[3,4],[5,6]]
# Output:
# [1,2,3,4,5,6]

# matrix = [[1,2],[3,4],[5,6]]
# flat = [ele for x in matrix for ele in x]
# print(flat)