# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli


@click.command(cli_util.override('reporting_managed_instance.reporting_managed_instance_root_group.command_name', 'reporting-managed-instance'), cls=CommandGroupWithAlias, help=cli_util.override('reporting_managed_instance.reporting_managed_instance_root_group.help', """Use the OS Management Hub API to manage and monitor updates and patches for instances in OCI, your private data center, or 3rd-party clouds.
For more information, see [Overview of OS Management Hub]."""), short_help=cli_util.override('reporting_managed_instance.reporting_managed_instance_root_group.short_help', """OS Management Hub API"""))
@cli_util.help_option_group
def reporting_managed_instance_root_group():
    pass


@click.command(cli_util.override('reporting_managed_instance.managed_instance_group.command_name', 'managed-instance'), cls=CommandGroupWithAlias, help="""An object that defines the instance being managed by the service.""")
@cli_util.help_option_group
def managed_instance_group():
    pass


@click.command(cli_util.override('reporting_managed_instance.managed_instance_analytic_collection_group.command_name', 'managed-instance-analytic-collection'), cls=CommandGroupWithAlias, help="""A set of managed instance metrics returned for the [SummarizeManagedInstanceAnalytics] operation.""")
@cli_util.help_option_group
def managed_instance_analytic_collection_group():
    pass


os_management_hub_service_cli.os_management_hub_service_group.add_command(reporting_managed_instance_root_group)
reporting_managed_instance_root_group.add_command(managed_instance_group)
reporting_managed_instance_root_group.add_command(managed_instance_analytic_collection_group)


@managed_instance_group.command(name=cli_util.override('reporting_managed_instance.get_managed_instance_analytic_content.command_name', 'get-managed-instance-analytic-content'), help=u"""Returns a report of managed instances matching the given filters. You can select CSV, XML, or JSON format. \n[Command Reference](getManagedInstanceAnalyticContent)""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment. This filter returns only resources contained within the specified compartment.""")
@cli_util.option('--managed-instance-group-id', help=u"""The [OCID] of the managed instance group. This filter returns resources associated with this group.""")
@cli_util.option('--lifecycle-environment-id', help=u"""The [OCID] of the lifecycle environment. This filter returns only resource contained with the specified lifecycle environment.""")
@cli_util.option('--lifecycle-stage-id', help=u"""The [OCID] of the lifecycle stage. This resource returns resources associated with this lifecycle stage.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR", "DELETING", "ONBOARDING", "REBOOTING"]), multiple=True, help=u"""A filter to return only managed instances whose status matches the status provided.""")
@cli_util.option('--display-name', multiple=True, help=u"""A filter to return resources that match the given display names.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return resources that may partially match the given display name.""")
@cli_util.option('--security-updates-available-equals-to', type=click.INT, help=u"""A filter to return instances that have the specified number of available security updates.""")
@cli_util.option('--bug-updates-available-equals-to', type=click.INT, help=u"""A filter to return instances that have the specified number of available bug updates.""")
@cli_util.option('--security-updates-available-greater-than', type=click.INT, help=u"""A filter to return instances that have more available security updates than the number specified.""")
@cli_util.option('--bug-updates-available-greater-than', type=click.INT, help=u"""A filter to return instances that have more available bug updates than the number specified.""")
@cli_util.option('--location', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help=u"""A filter to return only resources whose location matches the given value.""")
@cli_util.option('--location-not-equal-to', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help=u"""A filter to return only resources whose location does not match the given value.""")
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"]), multiple=True, help=u"""A filter to return only resources that match the given operating system family.""")
@cli_util.option('--is-managed-by-autonomous-linux', type=click.BOOL, help=u"""Indicates whether to list only resources managed by the Autonomous Linux service.""")
@cli_util.option('--report-format', type=custom_types.CliCaseInsensitiveChoice(["csv", "json", "xml"]), help=u"""The format of the report to download. Default is CSV.""")
@cli_util.option('--report-type', type=custom_types.CliCaseInsensitiveChoice(["SECURITY", "BUGFIX", "ACTIVITY", "ALL"]), help=u"""The type of the report the user wants to download. Default is ALL.""")
@json_skeleton_utils.get_cli_json_input_option({'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def get_managed_instance_analytic_content(ctx, from_json, file, compartment_id, managed_instance_group_id, lifecycle_environment_id, lifecycle_stage_id, status, display_name, display_name_contains, security_updates_available_equals_to, bug_updates_available_equals_to, security_updates_available_greater_than, bug_updates_available_greater_than, location, location_not_equal_to, os_family, is_managed_by_autonomous_linux, report_format, report_type):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if managed_instance_group_id is not None:
        kwargs['managed_instance_group_id'] = managed_instance_group_id
    if lifecycle_environment_id is not None:
        kwargs['lifecycle_environment_id'] = lifecycle_environment_id
    if lifecycle_stage_id is not None:
        kwargs['lifecycle_stage_id'] = lifecycle_stage_id
    if status is not None and len(status) > 0:
        kwargs['status'] = status
    if display_name is not None and len(display_name) > 0:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if security_updates_available_equals_to is not None:
        kwargs['security_updates_available_equals_to'] = security_updates_available_equals_to
    if bug_updates_available_equals_to is not None:
        kwargs['bug_updates_available_equals_to'] = bug_updates_available_equals_to
    if security_updates_available_greater_than is not None:
        kwargs['security_updates_available_greater_than'] = security_updates_available_greater_than
    if bug_updates_available_greater_than is not None:
        kwargs['bug_updates_available_greater_than'] = bug_updates_available_greater_than
    if location is not None and len(location) > 0:
        kwargs['location'] = location
    if location_not_equal_to is not None and len(location_not_equal_to) > 0:
        kwargs['location_not_equal_to'] = location_not_equal_to
    if os_family is not None and len(os_family) > 0:
        kwargs['os_family'] = os_family
    if is_managed_by_autonomous_linux is not None:
        kwargs['is_managed_by_autonomous_linux'] = is_managed_by_autonomous_linux
    if report_format is not None:
        kwargs['report_format'] = report_format
    if report_type is not None:
        kwargs['report_type'] = report_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'reporting_managed_instance', ctx)
    result = client.get_managed_instance_analytic_content(
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@managed_instance_group.command(name=cli_util.override('reporting_managed_instance.get_managed_instance_content.command_name', 'get-managed-instance-content'), help=u"""Returns a report for a single managed instance whose associated erratas match the given filters. You can select CSV, XML, or JSON format. \n[Command Reference](getManagedInstanceContent)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""The [OCID] of the managed instance.""")
@cli_util.option('--vulnerability-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", "ALL"]), multiple=True, help=u"""A filter to return only vulnerabilities matching the given types.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--advisory-name', multiple=True, help=u"""The assigned erratum name. It's unique and not changeable.

Example: `ELSA-2020-5804`""")
@cli_util.option('--advisory-name-contains', help=u"""A filter to return resources that may partially match the erratum advisory name given.""")
@cli_util.option('--advisory-type', type=custom_types.CliCaseInsensitiveChoice(["SECURITY", "BUGFIX", "ENHANCEMENT"]), multiple=True, help=u"""A filter to return only errata that match the given advisory types.""")
@cli_util.option('--vulnerability-name', multiple=True, help=u"""A filter to return vulnerabilities that match the given name. For Linux instances, this refers to the advisory name. For Windows instances, this refers to the Windows update display name.""")
@cli_util.option('--vulnerability-name-contains', help=u"""A filter to return vulnerabilities that partially match the given name. For Linux instances, this refers to the advisory name. For Windows instances, this refers to the Windows update display name.""")
@cli_util.option('--report-format', type=custom_types.CliCaseInsensitiveChoice(["csv", "json", "xml"]), help=u"""The format of the report to download. Default is CSV.""")
@json_skeleton_utils.get_cli_json_input_option({'advisory-name': {'module': 'os_management_hub', 'class': 'list[string]'}, 'vulnerability-name': {'module': 'os_management_hub', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'advisory-name': {'module': 'os_management_hub', 'class': 'list[string]'}, 'vulnerability-name': {'module': 'os_management_hub', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def get_managed_instance_content(ctx, from_json, file, managed_instance_id, vulnerability_type, advisory_name, advisory_name_contains, advisory_type, vulnerability_name, vulnerability_name_contains, report_format):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if advisory_name is not None and len(advisory_name) > 0:
        kwargs['advisory_name'] = advisory_name
    if advisory_name_contains is not None:
        kwargs['advisory_name_contains'] = advisory_name_contains
    if advisory_type is not None and len(advisory_type) > 0:
        kwargs['advisory_type'] = advisory_type
    if vulnerability_name is not None and len(vulnerability_name) > 0:
        kwargs['vulnerability_name'] = vulnerability_name
    if vulnerability_name_contains is not None:
        kwargs['vulnerability_name_contains'] = vulnerability_name_contains
    if report_format is not None:
        kwargs['report_format'] = report_format
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'reporting_managed_instance', ctx)
    result = client.get_managed_instance_content(
        managed_instance_id=managed_instance_id,
        vulnerability_type=vulnerability_type,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@managed_instance_analytic_collection_group.command(name=cli_util.override('reporting_managed_instance.summarize_managed_instance_analytics.command_name', 'summarize-managed-instance-analytics'), help=u"""Returns a list of user specified metrics for a collection of managed instances. \n[Command Reference](summarizeManagedInstanceAnalytics)""")
@cli_util.option('--metric-names', required=True, type=custom_types.CliCaseInsensitiveChoice(["TOTAL_INSTANCE_COUNT", "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT", "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT", "NORMAL_INSTANCE_COUNT", "ERROR_INSTANCE_COUNT", "WARNING_INSTANCE_COUNT", "UNREACHABLE_INSTANCE_COUNT", "REGISTRATION_FAILED_INSTANCE_COUNT", "DELETING_INSTANCE_COUNT", "ONBOARDING_INSTANCE_COUNT", "INSTANCE_SECURITY_UPDATES_COUNT", "INSTANCE_BUGFIX_UPDATES_COUNT", "INSTANCE_SECURITY_ADVISORY_COUNT", "INSTANCE_BUGFIX_ADVISORY_COUNT", "REBOOTING_INSTANCE_COUNT", "NEEDS_REBOOTING_INSTANCE_COUNT"]), multiple=True, help=u"""A filter to return only metrics whose name matches the given metric names.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment. This filter returns only resources contained within the specified compartment.""")
@cli_util.option('--managed-instance-group-id', help=u"""The [OCID] of the managed instance group. This filter returns resources associated with this group.""")
@cli_util.option('--lifecycle-environment-id', help=u"""The [OCID] of the lifecycle environment. This filter returns only resource contained with the specified lifecycle environment.""")
@cli_util.option('--lifecycle-stage-id', help=u"""The [OCID] of the lifecycle stage. This resource returns resources associated with this lifecycle stage.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR", "DELETING", "ONBOARDING", "REBOOTING"]), multiple=True, help=u"""A filter to return only managed instances whose status matches the status provided.""")
@cli_util.option('--location', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help=u"""A filter to return only resources whose location matches the given value.""")
@cli_util.option('--location-not-equal-to', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help=u"""A filter to return only resources whose location does not match the given value.""")
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"]), multiple=True, help=u"""A filter to return only resources that match the given operating system family.""")
@cli_util.option('--is-managed-by-autonomous-linux', type=click.BOOL, help=u"""Indicates whether to list only resources managed by the Autonomous Linux service.""")
@cli_util.option('--display-name', multiple=True, help=u"""A filter to return resources that match the given display names.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return resources that may partially match the given display name.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `3`""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "metricName", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. The default is to sort in ascending order by metricName (previously name, which is now depricated). You can also sort by displayName (default is ascending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@json_skeleton_utils.get_cli_json_input_option({'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceAnalyticCollection'})
@cli_util.wrap_exceptions
def summarize_managed_instance_analytics(ctx, from_json, metric_names, compartment_id, managed_instance_group_id, lifecycle_environment_id, lifecycle_stage_id, status, location, location_not_equal_to, os_family, is_managed_by_autonomous_linux, display_name, display_name_contains, limit, page, sort_by, sort_order):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if managed_instance_group_id is not None:
        kwargs['managed_instance_group_id'] = managed_instance_group_id
    if lifecycle_environment_id is not None:
        kwargs['lifecycle_environment_id'] = lifecycle_environment_id
    if lifecycle_stage_id is not None:
        kwargs['lifecycle_stage_id'] = lifecycle_stage_id
    if status is not None and len(status) > 0:
        kwargs['status'] = status
    if location is not None and len(location) > 0:
        kwargs['location'] = location
    if location_not_equal_to is not None and len(location_not_equal_to) > 0:
        kwargs['location_not_equal_to'] = location_not_equal_to
    if os_family is not None and len(os_family) > 0:
        kwargs['os_family'] = os_family
    if is_managed_by_autonomous_linux is not None:
        kwargs['is_managed_by_autonomous_linux'] = is_managed_by_autonomous_linux
    if display_name is not None and len(display_name) > 0:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'reporting_managed_instance', ctx)
    result = client.summarize_managed_instance_analytics(
        metric_names=metric_names,
        **kwargs
    )
    cli_util.render_response(result, ctx)
