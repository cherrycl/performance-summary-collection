*** Settings ***
Documentation   Measure the startup time for starting services one by one
...             Get service startup time with creating containers
...             Get service startup time without creating containers
Library         ../lib/EdgeX.py
Library         ../lib/AllServicesStartupOneByOne.py


*** Test Cases ***
Get core-data start up with creating containers
    Given dependency services are deployed redis       support-logging
    And start time is recorded
    When deploy service redis      core-data
    Then fetch startup time from service     core-data
    [Teardown]  Stop EdgeX Redis

Get core-data start up without creating containers
    Given dependency services are deployed redis     support-logging
    And start time is recorded
    When deploy service redis      core-data
    Then fetch startup time from service without recreate     core-data
    [Teardown]  Shutdown EdgeX Redis

Get core-metadata start up with creating containers
    Given dependency services are deployed redis       support-logging
    And start time is recorded
    When deploy service redis      core-metadata
    Then fetch startup time from service     core-metadata
    [Teardown]  Stop EdgeX Redis

Get core-metadata start up without creating containers
    Given dependency services are deployed redis     support-logging
    And start time is recorded
    When deploy service redis      core-metadata
    Then fetch startup time from service without recreate     core-metadata
    [Teardown]  Shutdown EdgeX Redis

Get core-command start up with creating containers
    Given dependency services are deployed redis       support-logging     core-metadata
    And start time is recorded
    When deploy service redis      core-command
    Then fetch startup time from service     core-command
    [Teardown]  Stop EdgeX Redis

Get core-command start up without creating containers
    Given dependency services are deployed redis     support-logging       core-metadata
    And start time is recorded
    When deploy service redis      core-command
    Then fetch startup time from service without recreate     core-command
    [Teardown]  Shutdown EdgeX Redis

Get support-logging start up with creating containers
    Given dependency services are deployed redis
    And start time is recorded
    When deploy service redis      support-logging
    Then fetch startup time from service     support-logging
    [Teardown]  Stop EdgeX Redis

Get support-logging start up without creating containers
    Given dependency services are deployed redis
    And start time is recorded
    When deploy service redis      support-logging
    Then fetch startup time from service without recreate     support-logging
    [Teardown]  Shutdown EdgeX Redis

Get support-notifications start up with creating containers
    Given dependency services are deployed redis       support-logging
    And start time is recorded
    When deploy service redis      support-notifications
    Then fetch startup time from service     support-notifications
    [Teardown]  Stop EdgeX Redis

Get support-notifications start up without creating containers
    Given dependency services are deployed redis       support-logging
    And start time is recorded
    When deploy service redis      support-notifications
    Then fetch startup time from service without recreate     support-notifications
    [Teardown]  Shutdown EdgeX Redis

Get support-scheduler start up with creating containers
    Given dependency services are deployed redis       support-logging
    And start time is recorded
    When deploy service redis      support-scheduler
    Then fetch startup time from service     support-scheduler
    [Teardown]  Stop EdgeX Redis

Get support-scheduler start up without creating containers
    Given dependency services are deployed redis       support-logging
    And start time is recorded
    When deploy service redis      support-scheduler
    Then fetch startup time from service without recreate     support-scheduler
    [Teardown]  Shutdown EdgeX Redis

Get export-client start up with creating containers
    Given dependency services are deployed redis       support-logging     core-data
    And start time is recorded
    When deploy service redis      export-client
    Then fetch startup time from service     export-client
    [Teardown]  Stop EdgeX Redis

Get export-client start up without creating containers
    Given dependency services are deployed redis       support-logging     core-data
    And start time is recorded
    When deploy service redis      export-client
    Then fetch startup time from service without recreate     export-client
    [Teardown]  Shutdown EdgeX Redis

Get export-distro start up with creating containers
    Given dependency services are deployed redis       support-logging     core-data       export-client
    And start time is recorded
    When deploy service redis      export-distro
    Then fetch startup time from service     export-distro
    [Teardown]  Stop EdgeX Redis

Get export-distro start up without creating containers
    Given dependency services are deployed redis       support-logging     core-data       export-client
    And start time is recorded
    When deploy service redis      export-distro
    Then fetch startup time from service without recreate     export-distro
    [Teardown]  Shutdown EdgeX Redis

Get device-virtual start up with creating containers
    Given dependency services are deployed redis       support-logging     core-data       core-metadata       core-command
    And start time is recorded
    When deploy service redis      device-virtual
    Then fetch startup time from service     device-virtual
    [Teardown]  Stop EdgeX Redis

Get device-virtual start up without creating containers
    Given dependency services are deployed redis       support-logging     core-data       core-metadata       core-command
    And start time is recorded
    When deploy service redis      device-virtual
    Then fetch startup time from service without recreate     device-virtual
    [Teardown]  Shutdown EdgeX Redis

Show comparison tables for startup time with/without recreate containers
    show the comparison table