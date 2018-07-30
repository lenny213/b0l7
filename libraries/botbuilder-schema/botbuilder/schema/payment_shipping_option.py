# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PaymentShippingOption(Model):
    """Describes a shipping option.

    :param id: String identifier used to reference this PaymentShippingOption
    :type id: str
    :param label: Human-readable description of the item
    :type label: str
    :param amount: Contains the monetary amount for the item
    :type amount: ~botframework.connector.models.PaymentCurrencyAmount
    :param selected: Indicates whether this is the default selected
     PaymentShippingOption
    :type selected: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'amount': {'key': 'amount', 'type': 'PaymentCurrencyAmount'},
        'selected': {'key': 'selected', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PaymentShippingOption, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.label = kwargs.get('label', None)
        self.amount = kwargs.get('amount', None)
        self.selected = kwargs.get('selected', None)
