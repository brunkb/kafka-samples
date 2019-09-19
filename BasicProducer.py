import kafka
producer = kafka.KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(101):
     producer.send('BenTest', b'msg %d' % i)
