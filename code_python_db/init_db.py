from model import *

db.connect()

# Create the database tables
db.create_tables([User, Exercice, UserExercice])

# Insérer des données
user1 = User.create(name='Alice')
user2 = User.create(name='Bob')
user3 = User.create(name='Charlie')

ex1 = Exercice.create(name='Squat') #AJOUTER IMAGE
ex2 = Exercice.create(name='Burpees')
ex3 = Exercice.create(name='Pompes')

UserExercice.create(user=user1, exercice=ex2, nr_fois=5)
UserExercice.create(user=user1, exercice=ex1, nr_fois=10)
UserExercice.create(user=user2, exercice=ex3, nr_fois=2)
UserExercice.create(user=user3, exercice=ex3, nr_fois=30)
