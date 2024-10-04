"""This module defines the ``Principal`` and ``PrincipalType`` classes."""
from dataclasses import dataclass
from principal_type import PrincipalType


@dataclass(frozen=True)
class Principal:
    """ A user, group, or service principal in Unity Catalog that
        accesses a securable."""
    name: str
    type: PrincipalType
