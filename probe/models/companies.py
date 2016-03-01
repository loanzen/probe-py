# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Companies(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Companies - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'list[CompanyBrief]',
            'has_more': 'bool',
            'total_count': 'int'
        }

        self.attribute_map = {
            'data': 'data',
            'has_more': 'hasMore',
            'total_count': 'totalCount'
        }

        self._data = None
        self._has_more = None
        self._total_count = None

    @property
    def data(self):
        """
        Gets the data of this Companies.
        Array of Companies

        :return: The data of this Companies.
        :rtype: list[CompanyBrief]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this Companies.
        Array of Companies

        :param data: The data of this Companies.
        :type: list[CompanyBrief]
        """
        self._data = data

    @property
    def has_more(self):
        """
        Gets the has_more of this Companies.
        The search result has more elements

        :return: The has_more of this Companies.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this Companies.
        The search result has more elements

        :param has_more: The has_more of this Companies.
        :type: bool
        """
        self._has_more = has_more

    @property
    def total_count(self):
        """
        Gets the total_count of this Companies.
        Search results total

        :return: The total_count of this Companies.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this Companies.
        Search results total

        :param total_count: The total_count of this Companies.
        :type: int
        """
        self._total_count = total_count

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other
