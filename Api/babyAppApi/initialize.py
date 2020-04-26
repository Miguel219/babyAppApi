## Para inicializar la base de datos por favor correr el comando py manage.py shell 
# y luego copiar este codigo y copiarlo en el shell.


from django.contrib.auth.models import User

##Se crea el primer usuario
u1 = User.objects.create_user("Jose","jose@gmail.com","jose123")
u1.save()
p1 = Parent(user=u1)
p1.save()

##Se crea el segundo usuario
u2 = User.objects.create_user("Juan","juan@gmail.com","juan123")
u2.save()
p2 = Parent(user=u2)
p2.save()

##Se crea el tercer usuario
u3 = User.objects.create_user("Marcela","marcela@gmail.com","marcela123")
u3.save()
p3 = Parent(user=u3)
p3.save()

##Se crea el cuarto usuario
u4 = User.objects.create_user("Miguel","miguel@gmail.com","andrea123")
u4.save()
p4 = Parent(user=u4)
p4.save()

##Se crea el quinto usuario
u5 = User.objects.create_user("Andrea","andrea@gmail.com","andrea123")
u5.save()
p5 = Parent(user=u5)
p5.save()
