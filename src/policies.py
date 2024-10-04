from databricks.sdk.service.catalog import GrantsAPI
from policies.policy import Policy

def create(policy: Policy) -> Policy:
    """ Creates a privilege policy in Unity Catalog."""

    GrantsAPI.update()