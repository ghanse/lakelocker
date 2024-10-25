""" This module defines utilities for interacting with the Databricks workspace."""
from typing import Optional
from pyspark.sql import DataFrame, SparkSession


class MetastoreOps:
    """ This class handles background operations in the UC metastore."""
    spark: SparkSession

    def __init__(self, spark: Optional[SparkSession]) -> None:
        if spark is None:
            self.spark = SparkSession.builder.appName('lakelocker-session').getOrCreate()
        else:
            self.spark = spark

    def exec_sql(self, sql: str) -> DataFrame:
        return self.spark.sql(sql)

    def create_catalog(self, catalog: str) -> DataFrame:
        return self.spark.sql(f'CREATE CATALOG IF NOT EXISTS {catalog}')

    def create_schema(self, schema: str) -> DataFrame:
        return self.spark.sql(f'CREATE SCHEMA IF NOT EXISTS {schema}')

    def create_table(self, table, schema: str) -> DataFrame:
        return self.spark.sql(f'CREATE TABLE IF NOT EXISTS {table}')
