import redis

r = redis.Redis(
  host='redis-18863.c17.us-east-1-4.ec2.redns.redis-cloud.com',
  port=18863,
  password='hpULYWBoqOwYI08k6fcwwztsFsO63KqH')


pubsub = r.pubsub()
pubsub.subscribe('test_channel')

print("Suscrito al canal 'test_channel'")

# Recibir y imprimir mensajes en tiempo real
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Mensaje recibido: {message['data'].decode('utf-8')}")
