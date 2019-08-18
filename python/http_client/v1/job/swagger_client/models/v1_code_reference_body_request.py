#!/usr/bin/python
#
# Copyright 2019 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys


def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv)
# coding: utf-8

"""
    Job service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: contact@polyaxon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.v1_code_reference import V1CodeReference  # noqa: F401,E501
from swagger_client.models.v1_owned_entity_id_request import V1OwnedEntityIdRequest  # noqa: F401,E501


class V1CodeReferenceBodyRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity': 'V1OwnedEntityIdRequest',
        'code_reference': 'V1CodeReference'
    }

    attribute_map = {
        'entity': 'entity',
        'code_reference': 'CodeReference'
    }

    def __init__(self, entity=None, code_reference=None):  # noqa: E501
        """V1CodeReferenceBodyRequest - a model defined in Swagger"""  # noqa: E501

        self._entity = None
        self._code_reference = None
        self.discriminator = None

        if entity is not None:
            self.entity = entity
        if code_reference is not None:
            self.code_reference = code_reference

    @property
    def entity(self):
        """Gets the entity of this V1CodeReferenceBodyRequest.  # noqa: E501


        :return: The entity of this V1CodeReferenceBodyRequest.  # noqa: E501
        :rtype: V1OwnedEntityIdRequest
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this V1CodeReferenceBodyRequest.


        :param entity: The entity of this V1CodeReferenceBodyRequest.  # noqa: E501
        :type: V1OwnedEntityIdRequest
        """

        self._entity = entity

    @property
    def code_reference(self):
        """Gets the code_reference of this V1CodeReferenceBodyRequest.  # noqa: E501


        :return: The code_reference of this V1CodeReferenceBodyRequest.  # noqa: E501
        :rtype: V1CodeReference
        """
        return self._code_reference

    @code_reference.setter
    def code_reference(self, code_reference):
        """Sets the code_reference of this V1CodeReferenceBodyRequest.


        :param code_reference: The code_reference of this V1CodeReferenceBodyRequest.  # noqa: E501
        :type: V1CodeReference
        """

        self._code_reference = code_reference

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1CodeReferenceBodyRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1CodeReferenceBodyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
