# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from .example_steps import step_entity_list
from .example_steps import step_hierarchy_setting_create
from .example_steps import step_hierarchy_setting_show
from .example_steps import step_hierarchy_setting_list
from .example_steps import step_hierarchy_setting_update
from .example_steps import step_hierarchy_setting_delete
from .example_steps import step_start_tenant_backfill
from .example_steps import step_tenant_backfill_status
from .example_steps import step_management_group_create
from .example_steps import step_management_group_show_descendant
from .example_steps import step_management_group_show
from .example_steps import step_management_group_show2
from .example_steps import step_management_group_show3
from .example_steps import step_management_group_show4
from .example_steps import step_management_group_show5
from .example_steps import step_management_group_list
from .example_steps import step_management_group_update
from .example_steps import step_management_group_delete
from .example_steps import step_management_group_subscription_create
from .example_steps import step_management_group_subscription
from .example_steps import step_management_group_subscription2
from .example_steps import step_management_group_subscription_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    step_entity_list(test, checks=[])
    step_hierarchy_setting_create(test, checks=[])
    step_hierarchy_setting_list(test, checks=[])
    step_hierarchy_setting_update(test, checks=[])
    step_hierarchy_setting_show(test, checks=[])
    step_hierarchy_setting_delete(test, checks=[])
    step_start_tenant_backfill(test, checks=[])
    step_tenant_backfill_status(test, checks=[])
    step_management_group_create(test, checks=[])
    step_management_group_show_descendant(test, checks=[])
    step_management_group_show(test, checks=[])
    step_management_group_show2(test, checks=[])
    step_management_group_show3(test, checks=[])
    step_management_group_show4(test, checks=[])
    step_management_group_show5(test, checks=[])
    step_management_group_list(test, checks=[])
    step_management_group_update(test, checks=[])
    step_management_group_delete(test, checks=[])
    step_management_group_subscription_create(test, checks=[])
    step_management_group_subscription(test, checks=[])
    step_management_group_subscription2(test, checks=[])
    step_management_group_subscription_delete(test, checks=[])
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class ManagementgroupScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(ManagementgroupScenarioTest, self).__init__(*args, **kwargs)

    def test_managementgroup_Scenario(self):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()