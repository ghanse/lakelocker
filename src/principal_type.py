"""This module defines the ``PrincipalType`` enum."""
from enum import Enum


class PrincipalType(Enum):
    """ The type of Unity Catalog principal."""
    USER = 'User'
    GROUP = 'Group'
    SERVICE_PRINCIPAL = 'ServicePrincipal'
