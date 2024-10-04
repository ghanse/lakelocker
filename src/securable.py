"""This module defines the ``Securable`` class."""
from databricks.sdk.service.catalog import SecurableType
from dataclasses import dataclass


@dataclass(frozen=True)
class Securable:
    """ An object in Unity Catalog (e.g. table, share)."""
    name: str
    type: SecurableType
