""" This module defines the ``ElapsedTimePolicy`` class."""
from databricks.sdk.service.catalog import Privilege
from dataclasses import dataclass
from datetime import datetime, timedelta
from policy import Policy
from src.principal import Principal
from src.securable import Securable
from typing import Optional


@dataclass
class ElapsedTimePolicy(Policy):
    """ An enforceable rule that grants access for a specified duration."""
    securables: list[Securable]
    principals: list[Principal]
    privileges: list[Privilege]
    start_date: datetime
    duration: timedelta
    end_date: Optional[datetime]

    def __post_init__(self) -> None:
        self.end_date = self.start_date + self.duration
