information={
    'First name':'Angelica',
    'Second name':'Guanseng',
    'Age':'18',
    'University':'BSU',
    'Course':'BSc in Cyber Security',
    'Hobbies':'Writing',
    'Favorite Food':'Fries'}

print(information)
print(information['First name'])

information["Age"] = "32"
print(information)

del information['Age']
print(information)

x=information.get('University')
print(x)

information.pop('University')
print(information)

information.update({'Age':'18'})
print(information)

print(information.keys())
print(information.values())

information.clear()
print(information)