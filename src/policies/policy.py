"""This module defines the abstract ``Policy`` class."""
from abc import ABC
from typing import Any
from databricks.sdk.service.catalog import Privilege
from src.securable import Securable
from src.principal import Principal


class Policy(ABC):
    """ An enforceable rule governing permission management."""
    securables: list[Securable]
    principals: list[Principal]
    privileges: list[Privilege]
