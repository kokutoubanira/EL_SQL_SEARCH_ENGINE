FROM docker.elastic.co/logstash/logstash:6.8.2

RUN rm -rf /usr/share/logstash/pipeline
COPY pipeline /usr/share/logstash/pipeline
COPY mysql-connector-java-8.0.17.jar /usr/share/logstash/mysql-connector-java-8.0.17.jar
COPY ./mapping.json ./mapping.json
#CMD ["sleep" "1m" ";" "curl", "-XPOST", "http://elasticsearch:9200/imdtable?pretty", "-d", "@mapping.json"]