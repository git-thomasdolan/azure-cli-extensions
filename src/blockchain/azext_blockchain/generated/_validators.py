# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def process_blockchain_member_sku(namespace):
    if namespace.sku == "Basic":
        namespace.sku = {
            'name': 'B0',
            'tier': 'Basic'
        }
    else:
        namespace.sku = {
            'name': 'S0',
            'tier': 'Standard'
        }