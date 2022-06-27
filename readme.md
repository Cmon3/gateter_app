# Gateter app

App para compartir tweets o maullidos entre los usuarios

## Para ejecutar la aplicación localmente

Primeramente proceder a crear un .env file con el secret key de django
o copiarlo directamente en el campo de SECRET_KEY en el archico de setting.py en el folder
social media.

Verificar que se cumplen con los requerimientos del requirements.txt

Correr el comando python manage.py runserver para inicializar la aplicación y ir 
al http://localhost:8000/

Debido a un bug con la aplicación todavía no es posible crear nuevos usuarios directamente 
yendo a /register, pero para modo de probar la aplicación se podrían agregar usuarios en 
el directotio de /admin de la aplicación y de ahi ir a /accounts/login para entrar en la aplicación
y ver sus funcionalidades.
