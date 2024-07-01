import redis
import time

# Conectar a la base de datos Redis


r = redis.Redis(
  host='redis-18863.c17.us-east-1-4.ec2.redns.redis-cloud.com',
  port=18863,
  password='hpULYWBoqOwYI08k6fcwwztsFsO63KqH')

# Publicar mensajes en el canal 'test_channel'
while True:
    message = input("Ingrese el mensaje a publicar: ")
    r.publish('test_channel', message)
    print(f"Mensaje publicado: {message}")
    time.sleep(1)
