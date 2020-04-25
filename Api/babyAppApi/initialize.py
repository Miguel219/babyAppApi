## Para inicializar la base de datos por favor correr el comando py manage.py shell 
# y luego copiar este codigo y copiarlo en el shell.


from django.contrib.auth.models import User

##Se crea el primer usuario
u1 = User.objects.create_user("Jose","jose@gmail.com","jose123")
u1.save()

##Se crea el segundo usuario
u2 = User.objects.create_user("Juan","juan@gmail.com","juan123")
u2.save()

##Se crea el tercer usuario
u3 = User.objects.create_user("Marcela","marcela@gmail.com","marcela123")
u3.save()

##Se crea el cuarto usuario
u4 = User.objects.create_user("Miguel","miguel@gmail.com","andrea123")
u4.save()

##Se crea el quinto usuario
u5 = User.objects.create_user("Andrea","andrea@gmail.com","andrea123")
u5.save()