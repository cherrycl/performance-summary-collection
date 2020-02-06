*** Settings ***
Documentation   Measure the startup time for starting all services at once
...             Get service start up time with creating containers
...             Get service start up time without creating containers
Library         ../lib/EdgeX.py
Library         ../lib/AllServicesStartupAtOnce.py

*** Test Cases ***

Get service startup time with creating containers (redis, no security)
    Given Start time is recorded
    When EdgeX with redis is deployed no secty
    Then fetch services start up time redis no secty
    [Teardown]  Stop EdgeX Redis

Get service startup time without creating containers (redis, no security)
    Given Start time is recorded
    When EdgeX with redis is deployed no secty
    Then fetch services start up time without creating containers redis no secty
    [Teardown]  Shutdown EdgeX Redis

Show comparison tables for startup time with/without recreate containers using redis no secty
    show the comparison table redis no secty