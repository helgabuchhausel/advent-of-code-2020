
import re

file = open('data.txt', 'r')
data = file.read().split('\n\n')
data = [line.replace('\n', ' ') for line in data]
file.close()

fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")

#rules
#byr (Birth Year) - four digits; at least 1920 and at most 2002.
byr = ("byr:[1]{1}[9]{1}[2-9]{1}[0-9]{1}", "byr:[2]{1}[0]{2}[0-2]{1}" ) #

#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
iyr = ("iyr:[2]{1}[0]{1}[1]{1}[0-9]{1}", "iyr:[2]{1}[0]{1}[2]{1}[0]{1}" )

#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
eyr = ("eyr:[2]{1}[0]{1}[2]{1}[0-9]{1}", "eyr:[2]{1}[0]{1}[3]{1}[0]{1}")

#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
hgt = ("hgt:[1]{1}[5-8]{1}[0-9]{1}cm", "hgt:[1]{1}[9]{1}[0-3]{1}cm",  "hgt:[5]{1}[9]{1}in", "hgt:[6]{1}[0-9]{1}in", "hgt:[7]{1}[0-6]{1}in")


#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
hcl = ("hcl:#[0-9a-f]{6}")

#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
ecl = ( "ecl:amb","ecl:blu", "ecl:brn", "ecl:gry",  "ecl:grn", "ecl:hzl", "ecl:oth")

#pid (Passport ID) - a nine-digit number, including leading zeroes.
pid = ("pid:[0-9]{9}" )

# fields check
def allFieldsCheck(passport):
    found = 0
    for x in range(len(fields)):
        if re.search(fields[x], passport):
            found += 1
    return found

# all fields found 
def foundAll(found, length):
    if found == length:
        return True

#only missing field is cid
def missingCid(found, length, passport):
    if length == found and not re.search("cid", passport):
        return True

#part one
def casualPassportCheck():
    all = 0
    for passport in data:
        found = allFieldsCheck(passport)
        if foundAll(found, len(fields)) or missingCid(found, len(fields)-1, passport):
            all += 1
    return all

# checks the if one field is between the constraints
def fieldValidityCheck(passport, patterns):
    for pattern in patterns:
        if re.search(pattern, passport):
            return True
    return False


#part two
def strictPassportCheck():
    all = 0
    for passport in data:
        found = allFieldsCheck(passport)
        if foundAll(found, len(fields)) or missingCid(found, len(fields)-1, passport):
            #expression to do 
            if fieldValidityCheck(passport, byr) and fieldValidityCheck(passport, iyr) and fieldValidityCheck(passport, eyr) and fieldValidityCheck(passport, hgt) and fieldValidityCheck(passport, hcl) and fieldValidityCheck(passport, ecl)  and fieldValidityCheck(passport, pid):
                print(passport)
                print("\n\n\n")
                all+=1

    return all



print(casualPassportCheck())
print(strictPassportCheck())

#Your puzzle answer was 158.