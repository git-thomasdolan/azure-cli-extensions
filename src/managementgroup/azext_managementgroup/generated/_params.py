# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type
)


def load_arguments(self, _):

    with self.argument_context('managementgroup management-group list') as c:
        c.argument('skiptoken', type=str, help='Page continuation token is only used if a previous operation returned '
                   'a partial result.  If a previous response contains a nextLink element, the value of the nextLink '
                   'element will include a token parameter that specifies a starting point to use for subsequent '
                   'calls.')

    with self.argument_context('managementgroup management-group show') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('expand', arg_type=get_enum_type(['children', 'path', 'ancestors']), help='The $expand=children '
                   'query string parameter allows clients to request inclusion of children in the response payload.  '
                   '$expand=path includes the path from the root group to the current group.  $expand=ancestors '
                   'includes the ancestor Ids of the current group.')
        c.argument('recurse', arg_type=get_three_state_flag(), help='The $recurse=true query string parameter allows '
                   'clients to request inclusion of entire hierarchy in the response payload. Note that  '
                   '$expand=children must be passed up if $recurse is set to true.')
        c.argument('filter_', options_list=['--filter'], type=str, help='A filter which allows the exclusion of '
                   'subscriptions from results (i.e. \'$filter=children.childType ne Subscription\')')

    with self.argument_context('managementgroup management-group create') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('name', type=str, help='The name of the management group. For example, '
                   '00000000-0000-0000-0000-000000000000')
        c.argument('display_name', type=str, help='The friendly name of the management group. If no value is passed '
                   'then this  field will be set to the groupId.')
        c.argument('id_', options_list=['--id'], type=str, help='The fully qualified ID for the parent management '
                   'group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000'
                   '000000', arg_group='Details Parent')

    with self.argument_context('managementgroup management-group update') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('display_name', type=str, help='The friendly name of the management group.')
        c.argument('parent_group_id', type=str, help='(Optional) The fully qualified ID for the parent management '
                   'group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000'
                   '000000')

    with self.argument_context('managementgroup management-group delete') as c:
        c.argument('group_id', type=str, help='Management Group ID.')

    with self.argument_context('managementgroup management-group show-descendant') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('skiptoken', type=str, help='Page continuation token is only used if a previous operation returned '
                   'a partial result.  If a previous response contains a nextLink element, the value of the nextLink '
                   'element will include a token parameter that specifies a starting point to use for subsequent '
                   'calls.')
        c.argument('top', type=int, help='Number of elements to return when retrieving results. Passing this in will '
                   'override $skipToken.')

    with self.argument_context('managementgroup management-group wait') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('expand', arg_type=get_enum_type(['children', 'path', 'ancestors']), help='The $expand=children '
                   'query string parameter allows clients to request inclusion of children in the response payload.  '
                   '$expand=path includes the path from the root group to the current group.  $expand=ancestors '
                   'includes the ancestor Ids of the current group.')
        c.argument('recurse', arg_type=get_three_state_flag(), help='The $recurse=true query string parameter allows '
                   'clients to request inclusion of entire hierarchy in the response payload. Note that  '
                   '$expand=children must be passed up if $recurse is set to true.')
        c.argument('filter_', options_list=['--filter'], type=str, help='A filter which allows the exclusion of '
                   'subscriptions from results (i.e. \'$filter=children.childType ne Subscription\')')

    with self.argument_context('managementgroup management-group-subscription create') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('subscription_id', type=str, help='Subscription ID.')

    with self.argument_context('managementgroup management-group-subscription delete') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('subscription_id', type=str, help='Subscription ID.', id_part='subscription')

    with self.argument_context('managementgroup management-group-subscription show-subscription') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('subscription_id', type=str, help='Subscription ID.', id_part='subscription')

    with self.argument_context('managementgroup management-group-subscription show-subscription-under-management-group') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('skiptoken', type=str, help='Page continuation token is only used if a previous operation returned '
                   'a partial result.  If a previous response contains a nextLink element, the value of the nextLink '
                   'element will include a token parameter that specifies a starting point to use for subsequent '
                   'calls.')

    with self.argument_context('managementgroup hierarchy-setting list') as c:
        c.argument('group_id', type=str, help='Management Group ID.')

    with self.argument_context('managementgroup hierarchy-setting show') as c:
        c.argument('group_id', type=str, help='Management Group ID.')

    with self.argument_context('managementgroup hierarchy-setting create') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('require_authorization_for_group_creation', arg_type=get_three_state_flag(), help='Indicates '
                   'whether RBAC access is required upon group creation under the root Management Group. If set to '
                   'true, user will require Microsoft.Management/managementGroups/write action on the root Management '
                   'Group scope in order to create new Groups directly under the root. This will prevent new users '
                   'from creating new Management Groups, unless they are given access.')
        c.argument('default_management_group', type=str, help='Settings that sets the default Management Group under '
                   'which new subscriptions get added in this tenant. For example, /providers/Microsoft.Management/mana'
                   'gementGroups/defaultGroup')

    with self.argument_context('managementgroup hierarchy-setting update') as c:
        c.argument('group_id', type=str, help='Management Group ID.')
        c.argument('require_authorization_for_group_creation', arg_type=get_three_state_flag(), help='Indicates '
                   'whether RBAC access is required upon group creation under the root Management Group. If set to '
                   'true, user will require Microsoft.Management/managementGroups/write action on the root Management '
                   'Group scope in order to create new Groups directly under the root. This will prevent new users '
                   'from creating new Management Groups, unless they are given access.')
        c.argument('default_management_group', type=str, help='Settings that sets the default Management Group under '
                   'which new subscriptions get added in this tenant. For example, /providers/Microsoft.Management/mana'
                   'gementGroups/defaultGroup')

    with self.argument_context('managementgroup hierarchy-setting delete') as c:
        c.argument('group_id', type=str, help='Management Group ID.')

    with self.argument_context('managementgroup entity list') as c:
        c.argument('skiptoken', type=str, help='Page continuation token is only used if a previous operation returned '
                   'a partial result.  If a previous response contains a nextLink element, the value of the nextLink '
                   'element will include a token parameter that specifies a starting point to use for subsequent '
                   'calls.')
        c.argument('skip', type=int, help='Number of entities to skip over when retrieving results. Passing this in '
                   'will override $skipToken.')
        c.argument('top', type=int, help='Number of elements to return when retrieving results. Passing this in will '
                   'override $skipToken.')
        c.argument('select', type=str, help='This parameter specifies the fields to include in the response. Can '
                   'include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. '
                   '\'$select=Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain\'. When specified the '
                   '$select parameter can override select in $skipToken.')
        c.argument('search', arg_type=get_enum_type(['AllowedParents', 'AllowedChildren',
                                                     'ParentAndFirstLevelChildren', 'ParentOnly', 'ChildrenOnly']),
                   help='The $search parameter is used in conjunction with the $filter parameter to return three '
                   'different outputs depending on the parameter passed in.  With $search=AllowedParents the API will '
                   'return the entity info of all groups that the requested entity will be able to reparent to as '
                   'determined by the user\'s permissions. With $search=AllowedChildren the API will return the entity '
                   'info of all entities that can be added as children of the requested entity. With '
                   '$search=ParentAndFirstLevelChildren the API will return the parent and  first level of children '
                   'that the user has either direct access to or indirect access via one of their descendants. With '
                   '$search=ParentOnly the API will return only the group if the user has access to at least one of '
                   'the descendants of the group. With $search=ChildrenOnly the API will return only the first level '
                   'of children of the group entity info specified in $filter.  The user must have direct access to '
                   'the children entities or one of it\'s descendants for it to show up in the results.')
        c.argument('filter_', options_list=['--filter'], type=str, help='The filter parameter allows you to filter on '
                   'the the name or display name fields. You can check for equality on the name field (e.g. name eq '
                   '\'{entityName}\')  and you can check for substrings on either the name or display name fields(e.g. '
                   'contains(name, \'{substringToSearch}\'), contains(displayName, \'{substringToSearch\')). Note that '
                   'the \'{entityName}\' and \'{substringToSearch}\' fields are checked case insensitively.')
        c.argument('view', arg_type=get_enum_type(['FullHierarchy', 'GroupsOnly', 'SubscriptionsOnly', 'Audit']),
                   help='The view parameter allows clients to filter the type of data that is returned by the '
                   'getEntities call.')
        c.argument('group_name', type=str, help='A filter which allows the get entities call to focus on a particular '
                   'group (i.e. "$filter=name eq \'groupName\'")')
