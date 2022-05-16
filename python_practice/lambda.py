people = [
    {"name" : "Jackie", "major" : "EE"},
    {"name" : "Leo", "major" : "music"},
    {"name" : "Amy", "major" : "IT"}
]


people.sort(key = lambda x:x["name"])

print(people)