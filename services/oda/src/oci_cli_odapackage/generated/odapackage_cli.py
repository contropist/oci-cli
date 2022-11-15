# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
from services.oda.src.oci_cli_oda.generated import oda_service_cli


@click.command(cli_util.override('odapackage.odapackage_root_group.command_name', 'odapackage'), cls=CommandGroupWithAlias, help=cli_util.override('odapackage.odapackage_root_group.help', """API to create and maintain Oracle Digital Assistant service instances."""), short_help=cli_util.override('odapackage.odapackage_root_group.short_help', """Digital Assistant Service Instance API"""))
@cli_util.help_option_group
def odapackage_root_group():
    pass


@click.command(cli_util.override('odapackage.package_group.command_name', 'package'), cls=CommandGroupWithAlias, help="""Details of `Package` object.""")
@cli_util.help_option_group
def package_group():
    pass


@click.command(cli_util.override('odapackage.imported_package_group.command_name', 'imported-package'), cls=CommandGroupWithAlias, help="""An imported/instantiated package within an instance.""")
@cli_util.help_option_group
def imported_package_group():
    pass


oda_service_cli.oda_service_group.add_command(odapackage_root_group)
odapackage_root_group.add_command(package_group)
odapackage_root_group.add_command(imported_package_group)


@imported_package_group.command(name=cli_util.override('odapackage.create_imported_package.command_name', 'create'), help=u"""Starts an asynchronous job to import a package into a Digital Assistant instance.

To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`. \n[Command Reference](createImportedPackage)""")
@cli_util.option('--current-package-id', required=True, help=u"""ID of the package to import.""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--parameter-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of parameter values to use when importing the given package. Must match those defined in the import contract.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'parameter-values': {'module': 'oda', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parameter-values': {'module': 'oda', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'ImportedPackage'})
@cli_util.wrap_exceptions
def create_imported_package(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, current_package_id, oda_instance_id, parameter_values, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['currentPackageId'] = current_package_id

    if parameter_values is not None:
        _details['parameterValues'] = cli_util.parse_json_parameter("parameter_values", parameter_values)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'odapackage', ctx)
    result = client.create_imported_package(
        oda_instance_id=oda_instance_id,
        create_imported_package_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@imported_package_group.command(name=cli_util.override('odapackage.delete_imported_package.command_name', 'delete'), help=u"""Starts an asynchronous job to delete a package from a Digital Assistant instance.

To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`. \n[Command Reference](deleteImportedPackage)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--package-id', required=True, help=u"""Unique Digital Assistant package identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_imported_package(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, package_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(package_id, six.string_types) and len(package_id.strip()) == 0:
        raise click.UsageError('Parameter --package-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'odapackage', ctx)
    result = client.delete_imported_package(
        oda_instance_id=oda_instance_id,
        package_id=package_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@imported_package_group.command(name=cli_util.override('odapackage.get_imported_package.command_name', 'get'), help=u"""Returns a list of summaries for imported packages in the instance. \n[Command Reference](getImportedPackage)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--package-id', required=True, help=u"""Unique Digital Assistant package identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'ImportedPackage'})
@cli_util.wrap_exceptions
def get_imported_package(ctx, from_json, oda_instance_id, package_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(package_id, six.string_types) and len(package_id.strip()) == 0:
        raise click.UsageError('Parameter --package-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'odapackage', ctx)
    result = client.get_imported_package(
        oda_instance_id=oda_instance_id,
        package_id=package_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@package_group.command(name=cli_util.override('odapackage.get_package.command_name', 'get'), help=u"""Returns details about a package, and how to import it. \n[Command Reference](getPackage)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--package-id', required=True, help=u"""Unique Digital Assistant package identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'Package'})
@cli_util.wrap_exceptions
def get_package(ctx, from_json, oda_instance_id, package_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(package_id, six.string_types) and len(package_id.strip()) == 0:
        raise click.UsageError('Parameter --package-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'odapackage', ctx)
    result = client.get_package(
        oda_instance_id=oda_instance_id,
        package_id=package_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@imported_package_group.command(name=cli_util.override('odapackage.list_imported_packages.command_name', 'list'), help=u"""Returns a list of summaries for imported packages in the instance. \n[Command Reference](listImportedPackages)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', help=u"""List only the information for the package with this name. Package names are unique to a publisher and may not change.

Example: `My Package`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.

The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'list[ImportedPackageSummary]'})
@cli_util.wrap_exceptions
def list_imported_packages(ctx, from_json, all_pages, page_size, oda_instance_id, name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'odapackage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_imported_packages,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_imported_packages,
            limit,
            page_size,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    else:
        result = client.list_imported_packages(
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@package_group.command(name=cli_util.override('odapackage.list_packages.command_name', 'list'), help=u"""Returns a page of summaries for packages that are available for import. The optional odaInstanceId query parameter can be used to filter packages that are available for import by a specific instance. If odaInstanceId query parameter is not provided, the returned list will include packages available within the region indicated by the request URL. The optional resourceType query param may be specified to filter packages that contain the indicated resource type. If no resourceType query param is given, packages containing all resource types will be returned. The optional name query parameter can be used to limit the list to packages whose name matches the given name. The optional displayName query parameter can be used to limit the list to packages whose displayName matches the given name. The optional isLatestVersionOnly query parameter can be used to limit the returned list to include only the latest version of any given package. If not specified, all versions of any otherwise matching package will be returned.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listPackages)""")
@cli_util.option('--oda-instance-id', help=u"""List only the information for this Digital Assistant instance.""")
@cli_util.option('--resource-type', help=u"""Resource type identifier. Used to limit query results to the items which are applicable to the given type.""")
@cli_util.option('--name', help=u"""List only the information for the package with this name. Package names are unique to a publisher and may not change.

Example: `My Package`""")
@cli_util.option('--display-name', help=u"""List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change.

Example: `My new resource`""")
@cli_util.option('--is-latest-skill-only', type=click.BOOL, help=u"""Should we return only the latest version of a package (instead of all versions)?""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.

The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'list[PackageSummary]'})
@cli_util.wrap_exceptions
def list_packages(ctx, from_json, all_pages, page_size, oda_instance_id, resource_type, name, display_name, is_latest_skill_only, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if oda_instance_id is not None:
        kwargs['oda_instance_id'] = oda_instance_id
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if name is not None:
        kwargs['name'] = name
    if display_name is not None:
        kwargs['display_name'] = display_name
    if is_latest_skill_only is not None:
        kwargs['is_latest_skill_only'] = is_latest_skill_only
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'odapackage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_packages,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_packages,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_packages(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@imported_package_group.command(name=cli_util.override('odapackage.update_imported_package.command_name', 'update'), help=u"""Starts an asynchronous job to update a package within a Digital Assistant instance.

To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`. \n[Command Reference](updateImportedPackage)""")
@cli_util.option('--current-package-id', required=True, help=u"""ID of the new package (i.e. version) to import, replacing the old imported package. Leave null if no new package resources are required. The name of the new package must must match the name of the already-imported package.""")
@cli_util.option('--parameter-values', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the updated parameter values to apply to this imported package.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--package-id', required=True, help=u"""Unique Digital Assistant package identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-replace-skills', type=click.BOOL, help=u"""Should old skills be replaced by new skills if packageId differs from already imported package?""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'parameter-values': {'module': 'oda', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parameter-values': {'module': 'oda', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'ImportedPackage'})
@cli_util.wrap_exceptions
def update_imported_package(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, current_package_id, parameter_values, oda_instance_id, package_id, freeform_tags, defined_tags, is_replace_skills, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(package_id, six.string_types) and len(package_id.strip()) == 0:
        raise click.UsageError('Parameter --package-id cannot be whitespace or empty string')
    if not force:
        if parameter_values or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to parameter-values and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if is_replace_skills is not None:
        kwargs['is_replace_skills'] = is_replace_skills
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['currentPackageId'] = current_package_id
    _details['parameterValues'] = cli_util.parse_json_parameter("parameter_values", parameter_values)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'odapackage', ctx)
    result = client.update_imported_package(
        oda_instance_id=oda_instance_id,
        package_id=package_id,
        update_imported_package_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
