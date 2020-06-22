import ResourceUsage
import PingResponse
import AllServicesStartupAtOnce
import AllServicesStartupOneByOne
import StartupTimeHandler
import EventExportedTime


class PerformanceSummary(object):

    def show_reports(self):
        # ResourceUsage.show_the_summary_table_in_html(ResourceUsage.resource_usage_with_mongo)
        ResourceUsage.show_the_summary_table_in_html(ResourceUsage.resource_usage_with_redis)

        StartupTimeHandler.show_the_comparison_table_in_html("Startup time:", AllServicesStartupAtOnce.all_up_time,
                                                             AllServicesStartupAtOnce.all_up_time_without_recreate)

        StartupTimeHandler.show_the_comparison_table_in_html("Startup time (no security):",  AllServicesStartupAtOnce.all_up_time_no_secty, 
                                                             AllServicesStartupAtOnce.all_up_time_without_recreate_no_secty)

        StartupTimeHandler.show_the_comparison_table_in_html("Startup time using Redis (no security):",  AllServicesStartupAtOnce.all_up_time_with_redis_no_secty,
                                                             AllServicesStartupAtOnce.all_up_time_with_redis_without_recreate_no_secty)
        
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time(exclude rulesengine):",
                                                             AllServicesStartupAtOnce.all_up_time_exclude_rulesengine,
                                                             AllServicesStartupAtOnce.all_up_time_exclude_rulesengine_without_recreate)
        
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time (exclude rulesengine and no security):",
                                                             AllServicesStartupAtOnce.all_up_time_exclude_rulesengine_no_secty,
                                                             AllServicesStartupAtOnce.all_up_time_exclude_rulesengine_without_recreate_no_secty)

        StartupTimeHandler.show_the_comparison_table_in_html("Startup time using Redis (exclude rulesengine and no security):",
                                                             AllServicesStartupAtOnce.all_up_time_with_redis_exclude_rulesengine_no_secty,
                                                             AllServicesStartupAtOnce.all_up_time_with_redis_exclude_rulesengine_without_recreate_no_secty)
        
        StartupTimeHandler.show_the_comparison_table_in_html("Startup time(deploy one by one):",
                                                             AllServicesStartupOneByOne.up_time,
                                                             AllServicesStartupOneByOne.up_time_without_recreate)

        PingResponse.show_the_summary_table_in_html()

        # EventExportedTime.show_the_summary_table_in_html("mongo")
        EventExportedTime.show_the_summary_table_in_html("redis")

