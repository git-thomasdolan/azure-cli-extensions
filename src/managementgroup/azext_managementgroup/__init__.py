# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=unused-import

import azext_managementgroup._help
from azure.cli.core import AzCommandsLoader


class ManagementGroupsAPICommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_managementgroup.generated._client_factory import cf_managementgroup_cl
        managementgroup_custom = CliCommandType(
            operations_tmpl='azext_managementgroup.custom#{}',
            client_factory=cf_managementgroup_cl)
        parent = super(ManagementGroupsAPICommandsLoader, self)
        parent.__init__(cli_ctx=cli_ctx, custom_command_type=managementgroup_custom)

    def load_command_table(self, args):
        from azext_managementgroup.generated.commands import load_command_table
        load_command_table(self, args)
        try:
            from azext_managementgroup.manual.commands import load_command_table as load_command_table_manual
            load_command_table_manual(self, args)
        except ImportError as e:
            if e.name.endswith('manual.commands'):
                pass
            else:
                raise e
        return self.command_table

    def load_arguments(self, command):
        from azext_managementgroup.generated._params import load_arguments
        load_arguments(self, command)
        try:
            from azext_managementgroup.manual._params import load_arguments as load_arguments_manual
            load_arguments_manual(self, command)
        except ImportError as e:
            if e.name.endswith('manual._params'):
                pass
            else:
                raise e


COMMAND_LOADER_CLS = ManagementGroupsAPICommandsLoader
