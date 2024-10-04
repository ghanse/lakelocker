""" This module defines the ``CalendarPolicy`` class."""
from databricks.sdk.service.catalog import Privilege
from dataclasses import dataclass
from datetime import datetime
from policy import Policy
from src.principal import Principal
from src.securable import Securable


@dataclass
class CalendarPolicy(Policy):
    """ An enforceable rule that grants access based on start and end dates."""
    securables: list[Securable]
    principals: list[Principal]
    privileges: list[Privilege]
    start_date: datetime
    end_date: datetime
