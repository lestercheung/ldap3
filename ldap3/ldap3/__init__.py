"""
"""

# Created on 2013.05.15
#
# Author: Giovanni Cannata
#
# Copyright 2015 Giovanni Cannata
#
# This file is part of ldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

# authentication
AUTH_ANONYMOUS = 'ANONYMOUS'
ANONYMOUS = 'ANONYMOUS'

AUTH_SIMPLE = 'SIMPLE'
SIMPLE = 'SIMPLE'

AUTH_SASL = 'SASL'
SASL = 'SASL'

SASL_AVAILABLE_MECHANISMS = ['EXTERNAL', 'DIGEST-MD5']

AUTO_BIND_NONE = 'NONE'
AUTO_BIND_NO_TLS = 'NO_TLS'
AUTO_BIND_TLS_BEFORE_BIND = 'TLS_BEFORE_BIND'
AUTO_BIND_TLS_AFTER_BIND = 'TLS_AFTER_BIND'

AUTHZ_STATE_CLOSED = 0
AUTHZ_STATE_ANONYMOUS = 1
AUTHZ_STATE_UNAUTHENTICATED = 2

# server IP dual stack mode
IP_SYSTEM_DEFAULT = 'SYSTEM_DEFAULT'
IP_V4_ONLY = 'V4_ONLY'
IP_V6_ONLY = 'V6_ONLY'
IP_V4_PREFERRED = 'V4_PREFERRED'
IP_V6_PREFERRED = 'V6_PREFERRED'
ADDRESS_INFO_REFRESH_TIME = 300  # seconds to wait before refreshing address info from dns

# search scope
SEARCH_SCOPE_BASE_OBJECT = 'BASE'
BASE = 'BASE'

SEARCH_SCOPE_SINGLE_LEVEL = 'LEVEL'
LEVEL = 'LEVEL'

SEARCH_SCOPE_WHOLE_SUBTREE = 'SUBTREE'
SUBTREE = 'SUBTREE'

# search alias
SEARCH_NEVER_DEREFERENCE_ALIASES = 'NONE'
DEREF_NONE = 'NONE'

SEARCH_DEREFERENCE_IN_SEARCHING = 'SEARCH'
DEREF_SEARCH = 'SEARCH'

SEARCH_DEREFERENCE_FINDING_BASE_OBJECT = 'FINDING_BASE'
DEREF_BASE = 'FINDING_BASE'

SEARCH_DEREFERENCE_ALWAYS = 'ALWAYS'
DEREF_ALWAYS = 'ALWAYS'


# search attributes
ALL_ATTRIBUTES = '*'
NO_ATTRIBUTES = '1.1'  # as per RFC 4511
ALL_OPERATIONAL_ATTRIBUTES = '+'  # as per RFC 3673

CASE_INSENSITIVE_ATTRIBUTE_NAMES = True
CASE_INSENSITIVE_SCHEMA_NAMES = True

# checks
ATTRIBUTES_EXCLUDED_FROM_CHECK = [ALL_ATTRIBUTES,
                                  ALL_OPERATIONAL_ATTRIBUTES,
                                  NO_ATTRIBUTES,
                                  'ldapSyntaxes',
                                  'matchingRules',
                                  'matchingRuleUse',
                                  'dITContentRules',
                                  'dITStructureRules',
                                  'nameForms',
                                  'altServer',
                                  'namingContexts',
                                  'supportedControl',
                                  'supportedExtension',
                                  'supportedFeatures',
                                  'supportedCapabilities',
                                  'supportedLdapVersion',
                                  'supportedSASLMechanisms',
                                  'vendorName',
                                  'vendorVersion',
                                  'subschemaSubentry']


# modify type
MODIFY_ADD = 'MODIFY_ADD'
MODIFY_DELETE = 'MODIFY_DELETE'
MODIFY_REPLACE = 'MODIFY_REPLACE'
MODIFY_INCREMENT = 'MODIFY_INCREMENT'

# client strategies
STRATEGY_SYNC = 'SYNC'
SYNC = 'SYNC'

STRATEGY_ASYNC_THREADED = 'ASYNC'
ASYNC = 'ASYNC'

STRATEGY_LDIF_PRODUCER = 'LDIF'
LDIF = 'LDIF'

STRATEGY_SYNC_RESTARTABLE = 'RESTARTABLE'
RESTARTABLE = 'RESTARTABLE'

STRATEGY_REUSABLE_THREADED = 'REUSABLE'
REUSABLE = 'REUSABLE'

STRATEGY_MOCK_SYNC = 'MOCK_SYNC'
STRATEGY_MOCK_ASYNC = 'MOCK_ASYNC'

CLIENT_STRATEGIES = [STRATEGY_SYNC,
                     STRATEGY_ASYNC_THREADED,
                     STRATEGY_LDIF_PRODUCER,
                     STRATEGY_SYNC_RESTARTABLE,
                     STRATEGY_REUSABLE_THREADED]

# communication
SESSION_TERMINATED_BY_SERVER = -2
RESPONSE_COMPLETE = -1
RESPONSE_SLEEPTIME = 0.05  # seconds to wait while waiting for a response in asynchronous strategies
RESPONSE_WAITING_TIMEOUT = 20  # waiting timeout for receiving a response in asynchronous strategies
SOCKET_SIZE = 4096  # socket byte size
CHECK_AVAILABILITY_TIMEOUT = 2.5  # default timeout for socket connect when checking availability

# restartable strategy
RESTARTABLE_SLEEPTIME = 2  # time to wait in a restartable strategy before retrying the request
RESTARTABLE_TRIES = 30  # number of times to retry in a restartable strategy before giving up. Set to True for unlimited retries

# reusable strategies (Threaded)
TERMINATE_REUSABLE = -9
REUSABLE_THREADED_POOL_SIZE = 10
REUSABLE_THREADED_LIFETIME = 3600  # 1 hour
DEFAULT_THREADED_POOL_NAME = 'reusable_default_pool'

# LDAP protocol
LDAP_MAX_INT = 2147483647

# LDIF
LDIF_LINE_LENGTH = 78

# result codes
RESULT_SUCCESS = 0
RESULT_OPERATIONS_ERROR = 1
RESULT_PROTOCOL_ERROR = 2
RESULT_TIME_LIMIT_EXCEEDED = 3
RESULT_SIZE_LIMIT_EXCEEDED = 4
RESULT_COMPARE_FALSE = 5
RESULT_COMPARE_TRUE = 6
RESULT_AUTH_METHOD_NOT_SUPPORTED = 7
RESULT_STRONGER_AUTH_REQUIRED = 8
RESULT_REFERRAL = 10
RESULT_ADMIN_LIMIT_EXCEEDED = 11
RESULT_UNAVAILABLE_CRITICAL_EXTENSION = 12
RESULT_CONFIDENTIALITY_REQUIRED = 13
RESULT_SASL_BIND_IN_PROGRESS = 14
RESULT_NO_SUCH_ATTRIBUTE = 16
RESULT_UNDEFINED_ATTRIBUTE_TYPE = 17
RESULT_INAPPROPRIATE_MATCHING = 18
RESULT_CONSTRAINT_VIOLATION = 19
RESULT_ATTRIBUTE_OR_VALUE_EXISTS = 20
RESULT_INVALID_ATTRIBUTE_SYNTAX = 21
RESULT_NO_SUCH_OBJECT = 32
RESULT_ALIAS_PROBLEM = 33
RESULT_INVALID_DN_SYNTAX = 34
RESULT_ALIAS_DEREFERENCING_PROBLEM = 36
RESULT_INAPPROPRIATE_AUTHENTICATION = 48
RESULT_INVALID_CREDENTIALS = 49
RESULT_INSUFFICIENT_ACCESS_RIGHTS = 50
RESULT_BUSY = 51
RESULT_UNAVAILABLE = 52
RESULT_UNWILLING_TO_PERFORM = 53
RESULT_LOOP_DETECTED = 54
RESULT_NAMING_VIOLATION = 64
RESULT_OBJECT_CLASS_VIOLATION = 65
RESULT_NOT_ALLOWED_ON_NON_LEAF = 66
RESULT_NOT_ALLOWED_ON_RDN = 67
RESULT_ENTRY_ALREADY_EXISTS = 68
RESULT_OBJECT_CLASS_MODS_PROHIBITED = 69
RESULT_AFFECT_MULTIPLE_DSAS = 71
RESULT_OTHER = 80
RESULT_LCUP_RESOURCES_EXHAUSTED = 113
RESULT_LCUP_SECURITY_VIOLATION = 114
RESULT_LCUP_INVALID_DATA = 115
RESULT_LCUP_UNSUPPORTED_SCHEME = 116
RESULT_LCUP_RELOAD_REQUIRED = 117
RESULT_CANCELED = 118
RESULT_NO_SUCH_OPERATION = 119
RESULT_TOO_LATE = 120
RESULT_CANNOT_CANCEL = 121
RESULT_ASSERTION_FAILED = 122
RESULT_AUTHORIZATION_DENIED = 123
RESULT_E_SYNC_REFRESH_REQUIRED = 4096

# do not raise exception for (in raise_exceptions connection mode)
DO_NOT_RAISE_EXCEPTIONS = [RESULT_SUCCESS, RESULT_COMPARE_FALSE, RESULT_COMPARE_TRUE, RESULT_REFERRAL]

# get rootDSE info
GET_NO_INFO = 'NO_INFO'
NONE = 'NO_INFO'

GET_DSA_INFO = 'DSA'
DSA = 'DSA'

GET_SCHEMA_INFO = 'SCHEMA'
SCHEMA = 'SCHEMA'

GET_ALL_INFO = 'ALL'
ALL = 'ALL'

OFFLINE_EDIR_8_8_8 = 'EDIR_8_8_8'
OFFLINE_AD_2012_R2 = 'AD_2012_R2'
OFFLINE_SLAPD_2_4 = 'SLAPD_2_4'
OFFLINE_DS389_1_3_3 = 'DS389_1_3_3'

# OID database definition
OID_CONTROL = 'CONTROL'
OID_EXTENSION = 'EXTENSION'
OID_FEATURE = 'FEATURE'
OID_UNSOLICITED_NOTICE = 'UNSOLICITED_NOTICE'
OID_ATTRIBUTE_TYPE = 'ATTRIBUTE_TYPE'
OID_DIT_CONTENT_RULE = 'DIT_CONTENT_RULE'
OID_LDAP_URL_EXTENSION = 'LDAP_URL_EXTENSION'
OID_FAMILY = 'FAMILY'
OID_MATCHING_RULE = 'MATCHING_RULE'
OID_NAME_FORM = 'NAME_FORM'
OID_OBJECT_CLASS = 'OBJECT_CLASS'
OID_ADMINISTRATIVE_ROLE = 'ADMINISTRATIVE_ROLE'
OID_LDAP_SYNTAX = 'LDAP_SYNTAX'

# class kind
CLASS_STRUCTURAL = 'STRUCTURAL'
CLASS_ABSTRACT = 'ABSTRACT'
CLASS_AUXILIARY = 'AUXILIARY'

# attribute kind
ATTRIBUTE_USER_APPLICATION = 'USER_APPLICATION'
ATTRIBUTE_DIRECTORY_OPERATION = 'DIRECTORY_OPERATION'
ATTRIBUTE_DISTRIBUTED_OPERATION = 'DISTRIBUTED_OPERATION'
ATTRIBUTE_DSA_OPERATION = 'DSA_OPERATION'

# abstraction layer
ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX = 'OP_'

# server pooling
POOLING_STRATEGY_FIRST = 'FIRST'
FIRST = 'FIRST'

POOLING_STRATEGY_ROUND_ROBIN = 'ROUND_ROBIN'
ROUND_ROBIN = 'ROUND_ROBIN'

POOLING_STRATEGY_RANDOM = 'RANDOM'
RANDOM = 'RANDOM'

POOLING_STRATEGIES = [POOLING_STRATEGY_FIRST, POOLING_STRATEGY_ROUND_ROBIN, POOLING_STRATEGY_RANDOM]

# types for string and sequence
if str != bytes:
    STRING_TYPES = (str, )
else:
    STRING_TYPES = (str, unicode)

SEQUENCE_TYPES = (list, tuple)

# centralized imports
from .version import __author__, __version__, __email__, __description__, __status__, __license__, __url__
from .core.server import Server
from .core.connection import Connection
from .core.tls import Tls
from .core.pooling import ServerPool
from .abstract import ObjectDef, AttrDef, Attribute, Entry, Reader, OperationalAttribute
from .protocol.rfc4512 import DsaInfo, SchemaInfo
from .core.exceptions import LDAPException, LDAPExceptionError, LDAPSocketCloseError, LDAPReferralError, \
    LDAPAttributeError, LDAPBindError, LDAPCertificateError, LDAPChangesError, LDAPCommunicationError, LDAPConnectionIsReadOnlyError, \
    LDAPConnectionPoolNameIsMandatoryError, LDAPConnectionPoolNotStartedError, LDAPControlsError, LDAPEntryError, \
    LDAPInvalidDereferenceAliasesError, LDAPInvalidFilterError, LDAPInvalidScopeError, LDAPInvalidServerError, LDAPKeyError,\
    LDAPLDIFError, LDAPMetricsError, LDAPObjectClassError, LDAPObjectError, LDAPPasswordIsMandatoryError, LDAPReaderError,\
    LDAPSASLBindInProgressError, LDAPSASLMechanismNotSupportedError, LDAPSASLPrepError, LDAPSchemaError, LDAPServerPoolError, \
    LDAPServerPoolExhaustedError, LDAPSocketOpenError, LDAPSocketReceiveError, LDAPSocketSendError, LDAPSSLConfigurationError,\
    LDAPSSLNotSupportedError, LDAPStartTLSError, LDAPTypeError, LDAPUnknownAuthenticationMethodError, LDAPUnknownRequestError, \
    LDAPUnknownResponseError, LDAPUnknownStrategyError, LDAPDefinitionError, LDAPResponseTimeoutError

from .core.exceptions import LDAPAdminLimitExceededResult, LDAPAffectMultipleDSASResult, LDAPAliasDereferencingProblemResult,\
    LDAPAliasProblemResult, LDAPAssertionFailedResult, LDAPAttributeOrValueExistsResult, LDAPAuthMethodNotSupportedResult, \
    LDAPAuthorizationDeniedResult, LDAPBusyResult, LDAPCanceledResult, LDAPCannotCancelResult, LDAPConfidentialityRequiredResult,\
    LDAPConstraintViolationResult, LDAPEntryAlreadyExistsResult, LDAPESyncRefreshRequiredResult, \
    LDAPInappropriateAuthenticationResult, LDAPInappropriateMatchingResult, LDAPInsufficientAccessRightsResult, \
    LDAPInvalidAttributeSyntaxResult, LDAPInvalidCredentialsResult, LDAPInvalidDNSyntaxResult, LDAPLCUPInvalidDataResult, \
    LDAPLCUPReloadRequiredResult, LDAPLCUPResourcesExhaustedResult, LDAPLCUPSecurityViolationResult, LDAPLCUPUnsupportedSchemeResult, \
    LDAPLoopDetectedResult, LDAPNamingViolationResult, LDAPNoSuchAttributeResult, LDAPNoSuchObjectResult, \
    LDAPNoSuchOperationResult, LDAPNotAllowedOnNotLeafResult, LDAPNotAllowedOnRDNResult, LDAPObjectClassModsProhibitedResult, \
    LDAPObjectClassViolationResult, LDAPOperationResult, LDAPOperationsErrorResult, LDAPOtherResult, LDAPProtocolErrorResult, \
    LDAPReferralResult, LDAPSASLBindInProgressResult, LDAPSizeLimitExceededResult, LDAPStrongerAuthRequiredResult, \
    LDAPTimeLimitExceededResult, LDAPTooLateResult, LDAPUnavailableCriticalExtensionResult, LDAPUnavailableResult, \
    LDAPUndefinedAttributeTypeResult, LDAPUnwillingToPerformResult, LDAPMaximumRetriesError, LDAPExtensionError, LDAPInvalidDnError
