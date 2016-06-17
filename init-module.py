import pickle

cursors = {"male": 0, "female": 0}
pickle.dump(cursors, open("cursors.bin", "wb"))
locked_greetings={"Боб":"пресвятейший"}
pickle.dump(locked_greetings, open("locked_greetings.bin", "wb"))
greetings=[]
f = open ("greetings.txt","r")
for greeting in f:
    greetings.append(greeting[:-1])
print(greetings)
pickle.dump(greetings, open("greetings.bin", "wb"))

# app_config = pickledb.load('app_config.db', False)
# app_config.set('cursor', 'abc')
# print(app_config.get('cursor'))
# app_config.dump()
