*** Settings ***
Documentation   Measure the startup time for starting all services(exclude rulesengine) at once
...             Get service start up time with creating containers
...             Get service start up time without creating containers
Library         Process
Library         ../lib/EdgeX.py
Library         ../lib/AllServicesStartupAtOnce.py

*** Test Cases ***
Get service start up time with creating containers
    Given Start time is recorded
    When EdgeX is deployed exclude rulesengine
    Then fetch services start up time exclude rulesengine
    [Teardown]  Stop EdgeX No RulesEngine

Get service start up time without creating containers
    Given Start time is recorded
    When EdgeX is deployed exclude rulesengine
    Then fetch services start up time without creating containers exclude rulesengine
    [Teardown]  Shutdown EdgeX No RulesEngine

Show comparison tables for start up time with/without creating containers
    show the comparison table for exclude rulesengine case

Get service startup time with creating containers (no security)
    Given Start time is recorded
    When EdgeX is deployed exclude rulesengine no secty
    Then fetch services start up time exclude rulesengine no secty
    [Teardown]  Stop EdgeX No RulesEngine

Get service startup time without creating containers (no security)
    Given Start time is recorded
    When EdgeX is deployed exclude rulesengine no secty
    Then fetch services start up time without creating containers exclude rulesengine no secty
    [Teardown]  Shutdown EdgeX No RulesEngine No Secty

Show comparison tables for start up time with/without creating containers no secty
    show the comparison table for exclude rulesengine case no secty

Get service startup time with creating containers (redis, no security)
    Given Start time is recorded
    When EdgeX with redis is deployed exclude rulesengine no secty
    Then fetch services start up time exclude rulesengine redis no secty
    [Teardown]  Stop EdgeX Redis No RulesEngine

Get service startup time without creating containers (redis, no security)
    Given Start time is recorded
    When EdgeX with redis is deployed exclude rulesengine no secty
    Then fetch services start up time without creating containers exclude rulesengine redis no secty
    [Teardown]  Shutdown EdgeX Redis No RulesEngine

Show comparison tables for start up time with/without creating containers redis no secty
    show the comparison table for exclude rulesengine case redis no secty