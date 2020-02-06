*** Settings ***
Documentation   Measure the event exported time
Library         ../lib/EdgeX.py
Library         ../lib/EventExportedTime.py

*** Test Cases ***
# Measure the event exported time
#     Given EdgeX is deployed with compose file    docker-compose-mqtt.yml
#     And mark pushed config is enable
#     And export registration is added
#     When query event with specified db  mongo
#     Then fetch the exported time with specified db  mongo
#     And show the summary table with specified db  mongo
#     And Shutdown EdgeX with compose file    docker-compose-mqtt.yml

Measure the event exported time (redis, no security)
    Given EdgeX is deployed with compose file    docker-compose-redis-mqtt.yml
    And mark pushed config is enable
    And export registration is added
    When query event with specified db  redis
    Then fetch the exported time with specified db  redis
    And show the summary table with specified db  redis
    And Shutdown EdgeX Redis