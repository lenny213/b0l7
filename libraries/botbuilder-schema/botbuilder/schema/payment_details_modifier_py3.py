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


class PaymentDetailsModifier(Model):
    """Provides details that modify the PaymentDetails based on payment method
    identifier.

    :param supported_methods: Contains a sequence of payment method
     identifiers
    :type supported_methods: list[str]
    :param total: This value overrides the total field in the PaymentDetails
     dictionary for the payment method identifiers in the supportedMethods
     field
    :type total: ~botframework.connector.models.PaymentItem
    :param additional_display_items: Provides additional display items that
     are appended to the displayItems field in the PaymentDetails dictionary
     for the payment method identifiers in the supportedMethods field
    :type additional_display_items:
     list[~botframework.connector.models.PaymentItem]
    :param data: A JSON-serializable object that provides optional information
     that might be needed by the supported payment methods
    :type data: object
    """

    _attribute_map = {
        'supported_methods': {'key': 'supportedMethods', 'type': '[str]'},
        'total': {'key': 'total', 'type': 'PaymentItem'},
        'additional_display_items': {'key': 'additionalDisplayItems', 'type': '[PaymentItem]'},
        'data': {'key': 'data', 'type': 'object'},
    }

    def __init__(self, *, supported_methods=None, total=None, additional_display_items=None, data=None, **kwargs) -> None:
        super(PaymentDetailsModifier, self).__init__(**kwargs)
        self.supported_methods = supported_methods
        self.total = total
        self.additional_display_items = additional_display_items
        self.data = data
