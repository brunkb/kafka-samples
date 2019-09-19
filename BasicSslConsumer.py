# use kafka-python library for compatibility
from kafka import KafkaConsumer, TopicPartition
import ssl

ssl.match_hostname = lambda cert, hostname: True

consumer = KafkaConsumer(bootstrap_servers='kafka-cluster:443',
                        security_protocol='SSL',
                        ssl_check_hostname=True,
                        ssl_cafile='CARoot.pem',
                        ssl_certfile='certificate.pem',
                        ssl_keyfile='key.pem',
                        auto_offset_reset='earliest',
                        group_id='py-group')

mytopicpartitions = 1
topicPartition=[TopicPartition('my-topic', p) for p in range(0,mytopicpartitions)]
consumer.assign(topicPartition)
consumer.seek_to_beginning()

for msg in consumer:
    print (msg)
