import kafka

consumer = kafka.KafkaConsumer(bootstrap_servers='localhost:9092', group_id='bb_group')
consumer.subscribe(['BenTest'])
for msg in consumer:
    print (msg)
