# Implementación

### Descripción
Por la flexibilidad que ofrece el framework. Usaremos Django como base para nuestro proyecto, ya que tenemos la oportunidad de usar sus sistemas MVC para Frontend y Backend, además de tener la posibilidad de extenderlo con un sistema API REST o extenderlo con alguna de las bibliotecas de Python, Desde filtrado, particionamiento, uniones e incluso funciones avanzadas de búsqueda de PostgreSQL.

Elegí PostgreSQL porque hace hincapié en la extensibilidad y el cumplimiento de estándares. Se elige porque cumple con la característica y protocolo ACID, que significa Atomicidad, Consistencia, Aislamiento y Durabilidad (siglas en inglés). Por tanto, la información de la base de datos y la fiabilidad del sistema están garantizadas. Django se serviría a través de Gunicorn.

Gunicorn es un servidor WSGI Python puro para UNIX. No tiene dependencias y es fácil de instalar y usar, es el servidor de producción de Python "clásico" estándar de la industria. La ventaja final de usar Gunicorn es que, por naturaleza, es bastante rápido, además de combinarse con NGINX como proxy inverso y equilibrador de carga para administrar el tráfico entrante y distribuirlo a servidores ascendentes más lentos, desde servidores de bases de datos heredados hasta microservicios, por ejemplo. que es ideal para usar frente a Gunicorn.

  Docker es una plataforma creada para desarrollar, implementar y ejecutar aplicaciones dentro de contenedores, lo que nos permite encapsular nuestra aplicación y sus servicios, para ayudar tanto a la replicación como a la alta disponibilidad.
### Requerimentos
Vamos a crear un proyecto en Django que ofrezca recomendaciones a un usuario sobre
qué hacer en sus tiempos libres.
- Se utilizo el siguiente recurso para obtener la información de las actividades
- https://www.boredapi.com/api/activity
Ejemplo de respuesta:

    {
    "activity": "Learn how to use a french press",
    "type": "recreational",
    "participants": 1,
    "price": 0.3,
    "link": "https://en.wikipedia.org/wiki/French_press",
    "key": "4522866",
    "accessibility": 0.3
    }

- Deberá existir un endpoint que obtendrá nuevas actividades y serán registradas en una
tabla de base de datos. El endpoint  es el siguiente:

> http://127.0.0.1:8001/api/v1/activities/

- Las actividades serán diferentes para cada usuario (es necesario considerar que un usuario
puede tener cero o múltiples actividades). Se realizo haciendo una comprobación para cada nueva actividad del usuario, se verifica que no exista ya para que no tenga repetidas. **api/views.py** *line* **16**.
- El usuario podrá usar un endpoint donde se muestren sus actividades generadas. El endpoint es el siguiente: 

> http://127.0.0.1:8001/api/v1/user-activities/

- Las actividades deberán tener un campo llamado 'done' del tipo 'bool' y servirá para que
el usuario marque las actividades que haya finalizado. **api/models.py** *line* **14**.
- Las actividades en base de datos se guardarán con el valor 'done' en 'false' y el usuario
tendrá la posibilidad de usar un endpoint para cambiarlo a 'true'. El endpoint es el siguiente para pasar una actividad con su id a `done=True` : 

> http://127.0.0.1:8001/api/v1/activities/<int:id>/done

### Instalar
La instalación se realiza mediante docker-compose.

     git clone https://github.com/raulespecialist/drf-activity.git
     cd drf-activity
     docker-compose up

Para comenzar a usar la aplicación, se crearon tres usuarios.

| usuario | contraseña |
|-------|-------|
| admin | TestPass3 |
| user1 | TestPass3 |
| user2 | TestPass3 |

