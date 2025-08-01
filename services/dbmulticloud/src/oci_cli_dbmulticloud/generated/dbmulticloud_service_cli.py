# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240501

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('work_request.dbmulticloud_service_group.command_name', 'dbmulticloud'), cls=CommandGroupWithAlias, help=cli_util.override('work_request.dbmulticloud_service_group.help', """1. Oracle Azure Connector Resource: This is for installing Azure Arc Server in ExaCS VM Cluster.
  There are two way to install Azure Arc Server (Azure Identity) in ExaCS VMCluster.
    a. Using Bearer Access Token or
    b. By providing Authentication token

2. Oracle Azure Blob Container Resource: This is for to capture Azure Container details
   and same will be used in multiple ExaCS VMCluster to mount the Azure Container.

3. Oracle Azure Blob Mount Resource: This is for to mount Azure Container in ExaCS VMCluster
   using Oracle Azure Connector and Oracle Azure Blob Container Resource."""), short_help=cli_util.override('work_request.dbmulticloud_service_group.short_help', """Oracle Database MultiCloud Data plane Integration"""))
@cli_util.help_option_group
def dbmulticloud_service_group():
    pass
