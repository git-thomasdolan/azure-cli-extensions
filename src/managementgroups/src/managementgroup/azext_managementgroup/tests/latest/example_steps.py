# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /Entities/post/GetEntities
@try_manual
def step_entity_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup entity list',
             checks=checks)


# EXAMPLE: /HierarchySettings/put/GetGroupSettings
@try_manual
def step_hierarchy_setting_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup hierarchy-setting create '
             '--default-management-group "/providers/Microsoft.Management/managementGroups/DefaultGroup" '
             '--require-authorization-for-group-creation true '
             '--group-id "root"',
             checks=checks)


# EXAMPLE: /HierarchySettings/get/GetGroupSettings
@try_manual
def step_hierarchy_setting_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup hierarchy-setting show '
             '--group-id "root"',
             checks=checks)


# EXAMPLE: /HierarchySettings/get/ListGroupSettings
@try_manual
def step_hierarchy_setting_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup hierarchy-setting list '
             '--group-id "root"',
             checks=checks)


# EXAMPLE: /HierarchySettings/patch/GetGroupSettings
@try_manual
def step_hierarchy_setting_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup hierarchy-setting update '
             '--default-management-group "/providers/Microsoft.Management/managementGroups/DefaultGroup" '
             '--require-authorization-for-group-creation true '
             '--group-id "root"',
             checks=checks)


# EXAMPLE: /HierarchySettings/delete/GetGroupSettings
@try_manual
def step_hierarchy_setting_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup hierarchy-setting delete -y '
             '--group-id "root"',
             checks=checks)


# EXAMPLE: /managementgroup/post/StartTenantBackfill
@try_manual
def step_start_tenant_backfill(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup start-tenant-backfill',
             checks=checks)


# EXAMPLE: /managementgroup/post/TenantBackfillStatus
@try_manual
def step_tenant_backfill_status(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup tenant-backfill-status',
             checks=checks)


# EXAMPLE: /ManagementGroups/put/PutManagementGroup
@try_manual
def step_management_group_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group create '
             '--cache-control "no-cache" '
             '--display-name "ChildGroup" '
             '--id "/providers/Microsoft.Management/managementGroups/RootGroup" '
             '--group-id "ChildGroup"',
             checks=checks)


# EXAMPLE: /ManagementGroups/get/GetDescendants
@try_manual
def step_management_group_show_descendant(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group show-descendant '
             '--group-id "20000000-0000-0000-0000-000000000000"',
             checks=checks)


# EXAMPLE: /ManagementGroups/get/GetManagementGroup
@try_manual
def step_management_group_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group show '
             '--cache-control "no-cache" '
             '--group-id "20000000-0001-0000-0000-000000000000"',
             checks=checks)


# EXAMPLE: /ManagementGroups/get/GetManagementGroupsWithExpandAndRecurse
@try_manual
def step_management_group_show2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group show '
             '--expand "children" '
             '--recurse true '
             '--cache-control "no-cache" '
             '--group-id "20000000-0001-0000-0000-000000000000"',
             checks=checks)


# EXAMPLE: /ManagementGroups/get/GetManagementGroupWithAncestors
@try_manual
def step_management_group_show3(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group show '
             '--expand "ancestors" '
             '--cache-control "no-cache" '
             '--group-id "20000000-0001-0000-0000-00000000000"',
             checks=checks)


# EXAMPLE: /ManagementGroups/get/GetManagementGroupWithExpand
@try_manual
def step_management_group_show4(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group show '
             '--expand "children" '
             '--cache-control "no-cache" '
             '--group-id "20000000-0001-0000-0000-000000000000"',
             checks=checks)


# EXAMPLE: /ManagementGroups/get/GetManagementGroupWithPath
@try_manual
def step_management_group_show5(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group show '
             '--expand "path" '
             '--cache-control "no-cache" '
             '--group-id "20000000-0001-0000-0000-000000000000"',
             checks=checks)


# EXAMPLE: /ManagementGroups/get/ListManagementGroups
@try_manual
def step_management_group_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group list '
             '--cache-control "no-cache"',
             checks=checks)


# EXAMPLE: /ManagementGroups/patch/PatchManagementGroup
@try_manual
def step_management_group_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group update '
             '--cache-control "no-cache" '
             '--group-id "ChildGroup" '
             '--display-name "AlternateDisplayName" '
             '--parent-group-id "/providers/Microsoft.Management/managementGroups/AlternateRootGroup"',
             checks=checks)


# EXAMPLE: /ManagementGroups/delete/DeleteManagementGroup
@try_manual
def step_management_group_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group delete -y '
             '--cache-control "no-cache" '
             '--group-id "GroupToDelete"',
             checks=checks)


# EXAMPLE: /ManagementGroupSubscriptions/put/AddSubscriptionToManagementGroup
@try_manual
def step_management_group_subscription_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group-subscription create '
             '--cache-control "no-cache" '
             '--group-id "Group" '
             '--subscription-id "728bcbe4-8d56-4510-86c2-4921b8beefbc"',
             checks=checks)


# EXAMPLE: /ManagementGroupSubscriptions/get/GetAllSubscriptionsFromManagementGroup
@try_manual
def step_management_group_subscription(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group-subscription show-subscription-under-management-group '
             '--group-id "Group"',
             checks=checks)


# EXAMPLE: /ManagementGroupSubscriptions/get/GetSubscriptionFromManagementGroup
@try_manual
def step_management_group_subscription2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group-subscription show-subscription '
             '--cache-control "no-cache" '
             '--group-id "Group" '
             '--subscription-id "728bcbe4-8d56-4510-86c2-4921b8beefbc"',
             checks=checks)


# EXAMPLE: /ManagementGroupSubscriptions/delete/DeleteSubscriptionFromManagementGroup
@try_manual
def step_management_group_subscription_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managementgroup management-group-subscription delete -y '
             '--cache-control "no-cache" '
             '--group-id "Group" '
             '--subscription-id "728bcbe4-8d56-4510-86c2-4921b8beefbc"',
             checks=checks)
