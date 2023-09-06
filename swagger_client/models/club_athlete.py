# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ClubAthlete(object):
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
        'resource_state': 'int',
        'firstname': 'str',
        'lastname': 'str',
        'member': 'str',
        'admin': 'bool',
        'owner': 'bool'
    }

    attribute_map = {
        'resource_state': 'resource_state',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'member': 'member',
        'admin': 'admin',
        'owner': 'owner'
    }

    def __init__(self, resource_state=None, firstname=None, lastname=None, member=None, admin=None, owner=None, _configuration=None):  # noqa: E501
        """ClubAthlete - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_state = None
        self._firstname = None
        self._lastname = None
        self._member = None
        self._admin = None
        self._owner = None
        self.discriminator = None

        if resource_state is not None:
            self.resource_state = resource_state
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if member is not None:
            self.member = member
        if admin is not None:
            self.admin = admin
        if owner is not None:
            self.owner = owner

    @property
    def resource_state(self):
        """Gets the resource_state of this ClubAthlete.  # noqa: E501

        Resource state, indicates level of detail. Possible values: 1 -> \"meta\", 2 -> \"summary\", 3 -> \"detail\"  # noqa: E501

        :return: The resource_state of this ClubAthlete.  # noqa: E501
        :rtype: int
        """
        return self._resource_state

    @resource_state.setter
    def resource_state(self, resource_state):
        """Sets the resource_state of this ClubAthlete.

        Resource state, indicates level of detail. Possible values: 1 -> \"meta\", 2 -> \"summary\", 3 -> \"detail\"  # noqa: E501

        :param resource_state: The resource_state of this ClubAthlete.  # noqa: E501
        :type: int
        """

        self._resource_state = resource_state

    @property
    def firstname(self):
        """Gets the firstname of this ClubAthlete.  # noqa: E501

        The athlete's first name.  # noqa: E501

        :return: The firstname of this ClubAthlete.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this ClubAthlete.

        The athlete's first name.  # noqa: E501

        :param firstname: The firstname of this ClubAthlete.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this ClubAthlete.  # noqa: E501

        The athlete's last initial.  # noqa: E501

        :return: The lastname of this ClubAthlete.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this ClubAthlete.

        The athlete's last initial.  # noqa: E501

        :param lastname: The lastname of this ClubAthlete.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def member(self):
        """Gets the member of this ClubAthlete.  # noqa: E501

        The athlete's member status.  # noqa: E501

        :return: The member of this ClubAthlete.  # noqa: E501
        :rtype: str
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this ClubAthlete.

        The athlete's member status.  # noqa: E501

        :param member: The member of this ClubAthlete.  # noqa: E501
        :type: str
        """

        self._member = member

    @property
    def admin(self):
        """Gets the admin of this ClubAthlete.  # noqa: E501

        Whether the athlete is a club admin.  # noqa: E501

        :return: The admin of this ClubAthlete.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this ClubAthlete.

        Whether the athlete is a club admin.  # noqa: E501

        :param admin: The admin of this ClubAthlete.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def owner(self):
        """Gets the owner of this ClubAthlete.  # noqa: E501

        Whether the athlete is club owner.  # noqa: E501

        :return: The owner of this ClubAthlete.  # noqa: E501
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ClubAthlete.

        Whether the athlete is club owner.  # noqa: E501

        :param owner: The owner of this ClubAthlete.  # noqa: E501
        :type: bool
        """

        self._owner = owner

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
        if issubclass(ClubAthlete, dict):
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
        if not isinstance(other, ClubAthlete):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClubAthlete):
            return True

        return self.to_dict() != other.to_dict()
