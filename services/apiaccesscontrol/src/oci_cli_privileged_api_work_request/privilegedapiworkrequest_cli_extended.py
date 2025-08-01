# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.apiaccesscontrol.src.oci_cli_privileged_api_work_request.generated import privilegedapiworkrequest_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci apiaccesscontrol privileged-api-work-request work-request' -> 'oci apiaccesscontrol privileged-api-work-request'
privilegedapiworkrequest_cli.privileged_api_work_request_root_group.commands.pop(privilegedapiworkrequest_cli.work_request_group.name)
privilegedapiworkrequest_cli.privileged_api_work_request_root_group.add_command(privilegedapiworkrequest_cli.cancel_work_request)
privilegedapiworkrequest_cli.privileged_api_work_request_root_group.add_command(privilegedapiworkrequest_cli.get_work_request)
privilegedapiworkrequest_cli.privileged_api_work_request_root_group.add_command(privilegedapiworkrequest_cli.list_work_requests)
