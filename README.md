# Control-de-Encuesta
Control de Encuesta: primera evaluación de pasantía 21.1
Control de Encuestas
La API no esta completa, pero abajo hago una descripción de lo que se realizo.

Desafíos:

Se requiere:
1. Registro.
        Se genero un modelo llamado User el cual contiene los atributos que representan a un usuario que desee utilizar la aplicación, se creo la vista del usuario, por donde las peticiones entraran en:\n
        Sign up : localhost:8000/users/signup/ por el método post. 
        Login : localhost:8000/users/login/ por el metodo post
        allusers : localhost:8000/users/allusers/ por el metodo get
2. CRUD encuestas, cada encuesta puede tener múltiples preguntas\n
        Se creo un modelo llamado “Survey” el cual almacena la información que una encuesta podría tener. Dentro de los atributos de esta clase, se tenia pensado tener una llave foránea que hiciera referencia al usuario que la creo. ¡Esto no se logro completar! 
        De igual forma, se creo otro modelo que representaría al objecto pregunta llamado “Question” el cual contiene algunos atributos que caracterizan al modelo.  Dentro de los atributos también había una referencia al modelo Survey, para referirse al objecto Survey del cual pertenece.
        Los endpoint de la vista Survey:

       Crea una encuesta: newSurvey : localhost:8000/surveys/newsurvey/ por el metodo post.\n
       Regresa las encuestas : localhost:8000/surveys/retrieve/ por el método post.\n

3. Autenticación – Requerido para la creación de encuestas
      Al crear un usuario por el endpoint de signup, si toda la información se encuentra en orden, este generara un token de autenticación.

4. Responder la encuesta

