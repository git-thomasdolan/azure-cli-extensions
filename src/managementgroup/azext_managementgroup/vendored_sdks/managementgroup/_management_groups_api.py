# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import ManagementGroupsAPIConfiguration
from .operations import ManagementGroupsOperations
from .operations import ManagementGroupSubscriptionsOperations
from .operations import HierarchySettingsOperations
from .operations import Operations
from .operations import ManagementGroupsAPIOperationsMixin
from .operations import EntitiesOperations
from . import models


class ManagementGroupsAPI(ManagementGroupsAPIOperationsMixin):
    """The Azure Management Groups API enables consolidation of multiple 
subscriptions/resources into an organizational hierarchy and centrally 
manage access control, policies, alerting and reporting for those resources.

    :ivar management_groups: ManagementGroupsOperations operations
    :vartype management_groups: azure.mgmt.managementgroups.operations.ManagementGroupsOperations
    :ivar management_group_subscriptions: ManagementGroupSubscriptionsOperations operations
    :vartype management_group_subscriptions: azure.mgmt.managementgroups.operations.ManagementGroupSubscriptionsOperations
    :ivar hierarchy_settings: HierarchySettingsOperations operations
    :vartype hierarchy_settings: azure.mgmt.managementgroups.operations.HierarchySettingsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.managementgroups.operations.Operations
    :ivar entities: EntitiesOperations operations
    :vartype entities: azure.mgmt.managementgroups.operations.EntitiesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ManagementGroupsAPIConfiguration(credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.management_groups = ManagementGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_group_subscriptions = ManagementGroupSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.hierarchy_settings = HierarchySettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.entities = EntitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ManagementGroupsAPI
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
