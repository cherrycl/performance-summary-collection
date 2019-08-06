from robot.api import logger
import time
import copy
import StartupTimeHandler

# all_up_time : record startup time for deploy EdgeX at once
all_up_time = dict()
all_up_time_without_recreate = dict()
all_up_time_no_secty = dict()
all_up_time_without_recreate_no_secty = dict()
all_up_time_with_redis_no_secty = dict()
all_up_time_with_redis_without_recreate_no_secty = dict()
all_up_time_exclude_rulesengine = dict()
all_up_time_exclude_rulesengine_without_recreate = dict()
all_up_time_exclude_rulesengine_no_secty = dict()
all_up_time_exclude_rulesengine_without_recreate_no_secty = dict()
all_up_time_with_redis_exclude_rulesengine_no_secty = dict()
all_up_time_with_redis_exclude_rulesengine_without_recreate_no_secty = dict()


class AllServicesStartupAtOnce(object):

    def start_time_is_recorded(self):
        self.start_time = time.time()
        logger.info("\n --- Start time %s seconds ---" % self.start_time, also_console=True)

    def fetch_services_start_up_time(self):
        global all_up_time

        all_up_time = get_services_start_up_time(self.start_time, StartupTimeHandler.services)

    def fetch_services_start_up_time_without_creating_containers(self):
        global all_up_time_without_recreate

        all_up_time_without_recreate = get_services_start_up_time(self.start_time,
                                                                                 StartupTimeHandler.services)
    def fetch_services_start_up_time_no_secty(self):
        global all_up_time_no_secty

        all_up_time_no_secty = get_services_start_up_time(self.start_time, StartupTimeHandler.services)

    def fetch_services_start_up_time_without_creating_containers_no_secty(self):
        global all_up_time_without_recreate_no_secty

        all_up_time_without_recreate_no_secty = get_services_start_up_time(self.start_time,
                                                                                 StartupTimeHandler.services)
    def fetch_services_start_up_time_redis_no_secty(self):
        global all_up_time_with_redis_no_secty

        all_up_time_with_redis_no_secty = get_services_start_up_time(self.start_time, StartupTimeHandler.services)

    def fetch_services_start_up_time_without_creating_containers_redis_no_secty(self):
        global all_up_time_with_redis_without_recreate_no_secty

        all_up_time_with_redis_without_recreate_no_secty = get_services_start_up_time(self.start_time,
                                                                                 StartupTimeHandler.services)

    # Exclude rulesengine
    def fetch_services_start_up_time_exclude_rulesengine(self):
        global all_up_time_exclude_rulesengine

        services_exclude_rulesengine = copy.deepcopy(StartupTimeHandler.services)
        services_exclude_rulesengine.pop("support-rulesengine", None)  # exclude rulesengine

        all_up_time_exclude_rulesengine = get_services_start_up_time(self.start_time,
                                                                                   services_exclude_rulesengine)

    # Exclude rulesengine
    def fetch_services_start_up_time_without_creating_containers_exclude_rulesengine(self):
        global all_up_time_exclude_rulesengine_without_recreate

        services_exclude_rulesengine = copy.deepcopy(StartupTimeHandler.services)
        services_exclude_rulesengine.pop("support-rulesengine", None)  # exclude rulesengine

        all_up_time_exclude_rulesengine_without_recreate = get_services_start_up_time(self.start_time,
                                                                                                    services_exclude_rulesengine)
    
    # Exclude rulesengine, no security
    def fetch_services_start_up_time_exclude_rulesengine_no_secty(self):
        global all_up_time_exclude_rulesengine_no_secty

        services_exclude_rulesengine = copy.deepcopy(StartupTimeHandler.services)
        services_exclude_rulesengine.pop("support-rulesengine", None)  # exclude rulesengine

        all_up_time_exclude_rulesengine_no_secty = get_services_start_up_time(self.start_time,
                                                                                   services_exclude_rulesengine)

    # Exclude rulesengine, no security
    def fetch_services_start_up_time_without_creating_containers_exclude_rulesengine_no_secty(self):
        global all_up_time_exclude_rulesengine_without_recreate_no_secty

        services_exclude_rulesengine = copy.deepcopy(StartupTimeHandler.services)
        services_exclude_rulesengine.pop("support-rulesengine", None)  # exclude rulesengine

        all_up_time_exclude_rulesengine_without_recreate_no_secty = get_services_start_up_time(self.start_time,
                                                                                                    services_exclude_rulesengine)
    
    # Exclude rulesengine, using redis, no security
    def fetch_services_start_up_time_exclude_rulesengine_redis_no_secty(self):
        global all_up_time_with_redis_exclude_rulesengine_no_secty

        services_exclude_rulesengine = copy.deepcopy(StartupTimeHandler.services)
        services_exclude_rulesengine.pop("support-rulesengine", None)  # exclude rulesengine

        all_up_time_with_redis_exclude_rulesengine_no_secty = get_services_start_up_time(self.start_time,
                                                                                   services_exclude_rulesengine)

    # Exclude rulesengine, using redis, no security
    def fetch_services_start_up_time_without_creating_containers_exclude_rulesengine_redis_no_secty(self):
        global all_up_time_with_redis_exclude_rulesengine_without_recreate_no_secty

        services_exclude_rulesengine = copy.deepcopy(StartupTimeHandler.services)
        services_exclude_rulesengine.pop("support-rulesengine", None)  # exclude rulesengine

        all_up_time_with_redis_exclude_rulesengine_without_recreate_no_secty = get_services_start_up_time(self.start_time,
                                                                                                    services_exclude_rulesengine)

    def show_the_comparison_table(self):
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time:", all_up_time, all_up_time_without_recreate)
    
    def show_the_comparison_table_no_secty(self):
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time (no security):",
                                                             all_up_time_no_secty,
                                                             all_up_time_without_recreate_no_secty)
    
    def show_the_comparison_table_redis_no_secty(self):
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time using Redis (no security):",
                                                             all_up_time_with_redis_no_secty,
                                                             all_up_time_with_redis_without_recreate_no_secty)

    def show_the_comparison_table_for_exclude_rulesengine_case(self):
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time (exclude rulesengine):",
                                                             all_up_time_exclude_rulesengine,
                                                             all_up_time_exclude_rulesengine_without_recreate)

    def show_the_comparison_table_for_exclude_rulesengine_case_no_secty(self):
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time (exclude rulesengine and no security):",
                                                             all_up_time_exclude_rulesengine_no_secty,
                                                             all_up_time_exclude_rulesengine_without_recreate_no_secty)

    def show_the_comparison_table_for_exclude_rulesengine_case_redis_no_secty(self):
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time using Redis (exclude rulesengine and no security):",
                                                             all_up_time_with_redis_exclude_rulesengine_no_secty,
                                                             all_up_time_with_redis_exclude_rulesengine_without_recreate_no_secty)

def find_total_startup_time(result):
    largest_time = 0
    for k in result:
        if largest_time < result[k]["startupTime"]:
            largest_time = result[k]["startupTime"]

    return str(largest_time)


def get_services_start_up_time(start_time, containers):
    result = dict()
    for k in containers:
        StartupTimeHandler.fetch_service_start_up_time_by_container_name(containers[k], start_time, result)

    total_startup_time = find_total_startup_time(result)
    result["Total startup time"] = {}
    result["Total startup time"]["binaryStartupTime"] = ""
    result["Total startup time"]["startupTime"] = total_startup_time

    return result
