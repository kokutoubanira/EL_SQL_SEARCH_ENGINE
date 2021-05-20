FROM docker.elastic.co/logstash/logstash:6.8.2

RUN rm -rf /usr/share/logstash/pipeline
COPY pipeline /usr/share/logstash/pipeline
COPY mysql-connector-java-8.0.17.jar /usr/share/logstash/mysql-connector-java-8.0.17.jar
COPY ./mapping_ma.json ./mapping_ma.json
COPY ./mapping_ngram.json ./mapping_ngram.json
#CMD ["sleep" "1m" ";" "curl", "-XPOST", "http://elasticsearch:9200/imdtable?pretty", "-d", "@mapping.json"]