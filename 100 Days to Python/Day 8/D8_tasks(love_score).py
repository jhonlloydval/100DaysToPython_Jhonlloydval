# LOVE SCORE OF 2 NAMES

def calculate_love_score(name1, name2):
    true_score = 0
    for x in "TRUE":
        for y in name1.upper():
            if x == y:
                true_score += 1
        for z in name2.upper():
            if z == x:
                true_score += 1


    love_score = 0           
    for x in "LOVE":
        for y in name1.upper():
            if x == y:
                love_score += 1
        for z in name2.upper():
            if z == x:
                love_score += 1
    
    score = str(true_score) + str(love_score)
    print(score)

calculate_love_score("Lucy Driz Montalbo", "Abby Abaja Valencia")

# CORRECT CODE BASED ON THE EXERCISE



def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).upper()

    true_score = 0
    for x in "TRUE":
        for y in combined_name:
            if x == y:
                true_score += 1

    love_score = 0
    for x in "LOVE":
        for y in combined_name:
            if x == y:
                love_score += 1
    
    score = str(true_score) + str(love_score)
    print(score)

calculate_love_score("Lucy Driz Montalbo", "Abby Abaja Valencia")



# LOVE SCORE OF 2 NAMES (EXPERIMENT)
# WRONG CODE
def calculate_love_score(name1, name2):
    true_score = 0
    for x in "TRUE":
        for y,z in zip(name1.upper(), name2.upper()):
            if x == y:
                true_score += 1
            if x == z:
                true_score += 1

    love_score = 0           
    for x in "LOVE":
        for y,z in zip(name1.upper(), name2.upper()):
            if x == y:
                love_score += 1
            if x == z:
                love_score += 1

    
    score = str(true_score) + str(love_score)
    print(score)

calculate_love_score("Lucy Driz Montalbo", "Abby Abaja Valencia")
            

hi = "hi"
hi[0] = "b"
print(hi)