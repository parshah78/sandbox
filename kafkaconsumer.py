import json
from kafka import KafkaConsumer
consumer = KafkaConsumer('ats1_logstash_telephony_hdfs', bootstrap_servers=['rpbt1hsn008.webex.com:9092'],value_deserializer=lambda m: json.loads(m))
for message in consumer:
    print ("value=%s" % (message.value))

