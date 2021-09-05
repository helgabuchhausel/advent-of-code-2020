from operator import concat
import re

file = open('data.txt', 'r')
data = file.read().split('\n\n')
data = [line.replace('\n', ' ') for line in data]
file.close()

fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")

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


#part two
def strictPassportCheck():
    for passport in data:
        found = allFieldsCheck(passport)
        if foundAll(found, len(fields)) or missingCid(found, len(fields)-1, passport):
            print("not yet")
            
#rules
 #   byr (Birth Year) - four digits; at least 1920 and at most 2002.
 #   iyr (Issue Year) - four digits; at least 2010 and at most 2020.
 #   eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
 #   hgt (Height) - a number followed by either cm or in:
 #       If cm, the number must be at least 150 and at most 193.
 #       If in, the number must be at least 59 and at most 76.
 #   hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
 #   ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
 #   pid (Passport ID) - a nine-digit number, including leading zeroes.

    return "not yet"



print(casualPassportCheck())
print(strictPassportCheck())

