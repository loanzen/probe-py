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


class CompanyBrief(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CompanyBrief - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'legal_name': 'str',
            'cin': 'str'
        }

        self.attribute_map = {
            'legal_name': 'legal_name',
            'cin': 'cin'
        }

        self._legal_name = None
        self._cin = None

    @property
    def legal_name(self):
        """
        Gets the legal_name of this CompanyBrief.
        Legal name of the company

        :return: The legal_name of this CompanyBrief.
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """
        Sets the legal_name of this CompanyBrief.
        Legal name of the company

        :param legal_name: The legal_name of this CompanyBrief.
        :type: str
        """
        self._legal_name = legal_name

    @property
    def cin(self):
        """
        Gets the cin of this CompanyBrief.
        Unique identifier representing the company - Company Identification number

        :return: The cin of this CompanyBrief.
        :rtype: str
        """
        return self._cin

    @cin.setter
    def cin(self, cin):
        """
        Sets the cin of this CompanyBrief.
        Unique identifier representing the company - Company Identification number

        :param cin: The cin of this CompanyBrief.
        :type: str
        """
        self._cin = cin

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

