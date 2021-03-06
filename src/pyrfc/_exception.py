# Copyright 2013 SAP AG.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an.
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific.
# language governing permissions and limitations under the License.

""" :mod:`pyrfc`-specific exception classes
"""

class RFCError(Exception):
    """ Exception base class

    Indicates that there was an error in the Python connector.
    """
    pass


class RFCLibError(RFCError):
    """ RFC library error

    Base class for exceptions raised by the local underlying C connector (sapnwrfc.c).
    """

    # Results as of: RfcGetRcAsString(RFC_RC rc)
    # cf. material/kjona_getRcAsString
    code2txt = {
        0: 'RFC_OK',
        1: 'RFC_COMMUNICATION_FAILURE',
        2: 'RFC_LOGON_FAILURE',
        3: 'RFC_ABAP_RUNTIME_FAILURE',
        4: 'RFC_ABAP_MESSAGE',
        5: 'RFC_ABAP_EXCEPTION',
        6: 'RFC_CLOSED',
        7: 'RFC_CANCELED',
        8: 'RFC_TIMEOUT',
        9: 'RFC_MEMORY_INSUFFICIENT',
        10: 'RFC_VERSION_MISMATCH',
        11: 'RFC_INVALID_PROTOCOL',
        12: 'RFC_SERIALIZATION_FAILURE',
        13: 'RFC_INVALID_HANDLE',
        14: 'RFC_RETRY',
        15: 'RFC_EXTERNAL_FAILURE',
        16: 'RFC_EXECUTED',
        17: 'RFC_NOT_FOUND',
        18: 'RFC_NOT_SUPPORTED',
        19: 'RFC_ILLEGAL_STATE',
        20: 'RFC_INVALID_PARAMETER',
        21: 'RFC_CODEPAGE_CONVERSION_FAILURE',
        22: 'RFC_CONVERSION_FAILURE',
        23: 'RFC_BUFFER_TOO_SMALL',
        24: 'RFC_TABLE_MOVE_BOF',
        25: 'RFC_TABLE_MOVE_EOF',
        26: 'RFC_START_SAPGUI_FAILURE',
        27: 'RFC_ABAP_CLASS_EXCEPTION',
        28: 'RFC_UNKNOWN_ERROR',
        29: 'RFC_AUTHORIZATION_FAILURE'
    }

    def __init__(self, message=None, code=None, key=None,
                 msg_class=None, msg_type=None, msg_number=None,
                 msg_v1=None, msg_v2=None, msg_v3=None, msg_v4=None):
        super(RFCLibError, self).__init__(message)
        self.message = message # Exception.message removed in Py3
        self.code = code
        self.key = key
        self.msg_class = msg_class
        self.msg_type = msg_type
        self.msg_number = msg_number
        self.msg_v1 = msg_v1
        self.msg_v2 = msg_v2
        self.msg_v3 = msg_v3
        self.msg_v4 = msg_v4

    def __str__(self):
        return '{} (rc={}): key={}, message={} [MSG: class={}, type={}, number={}, v1-4:={};{};{};{}]'.format(
            self.code2txt.get(self.code, '???'),
            self.code, self.key, self.message, self.msg_class,
            self.msg_type, self.msg_number,
            self.msg_v1, self.msg_v2, self.msg_v3, self.msg_v4
            )

class ABAPApplicationError(RFCLibError):
    """ ABAP application error

    This exception is raised if a RFC call returns an RC code greater than 0 and
    the error object has an RFC_ERROR_GROUP value of
    ABAP_APPLICATION_FAILURE.
    """
    pass


class ABAPRuntimeError(RFCLibError):
    """ ABAP runtime error

    This exception is raised if a RFC call returns an RC code greater than 0 and
    the error object has an RFC_ERROR_GROUP value of
    ABAP_RUNTIME_FAILURE.
    """
    pass

class LogonError(RFCLibError):
    """ Logon error

    This exception is raised if a RFC call returns an RC code greater than 0 and
    the error object has an RFC_ERROR_GROUP value of
    LOGON_FAILURE.
    """
    def __init__(self, message=None, code=2, key='RFC_LOGON_FAILURE',
                 msg_class=None, msg_type=None, msg_number=None,
                 msg_v1=None, msg_v2=None, msg_v3=None, msg_v4=None):
        # Setting default values allows for raising an error with one parameter.
        super(LogonError, self).__init__(message, code, key, msg_class, msg_type, msg_number,
            msg_v1, msg_v2, msg_v3, msg_v4)


class CommunicationError(RFCLibError):
    """ Communication error

    This exception is raised if a RFC call returns an RC code greater than 0 and
    the error object has an RFC_ERROR_GROUP value of
    COMMUNICATION_FAILURE.
    """
    pass

class ExternalRuntimeError(RFCLibError):
    """ External runtime error

    This exception is raised if a RFC call returns an RC code greater than 0 and
    the error object has an RFC_ERROR_GROUP value of
    EXTERNAL_RUNTIME_FAILURE.
    """
    pass

class ExternalApplicationError(RFCLibError):
    """ External application error

    This exception is raised if a RFC call returns an RC code greater than 0 and
    the error object has an RFC_ERROR_GROUP value of
    EXTERNAL_APPLICATION_FAILURE.
    """
    pass

class ExternalAuthorizationError(RFCLibError):
    """ External authorization error

    This exception is raised if a RFC call returns an RC code greater than 0 and
    the error object has an RFC_ERROR_GROUP value of
    EXTERNAL_AUTHORIZATION_FAILURE.
    """
    pass


