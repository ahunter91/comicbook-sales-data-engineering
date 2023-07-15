import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node MySQL table
MySQLtable_node1 = glueContext.create_dynamic_frame.from_options(
    connection_type="mysql",
    connection_options={
        "useConnectionProperties": "true",
        "dbtable": "transactions",
        "connectionName": "comiverse_RDS-Glue",
    },
    transformation_ctx="MySQLtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=MySQLtable_node1,
    mappings=[
        ("customer_id", "bigint", "customer_id", "string"),
        ("comic_id", "bigint", "comic_id", "string"),
        ("unit_cost", "double", "unit_cost", "string"),
        ("binding", "string", "binding", "string"),
        ("transaction_date", "string", "transaction_date", "string"),
        ("quantity", "bigint", "quantity", "int"),
        ("transaction_id", "bigint", "transaction_id", "int"),
        ("total_amount", "double", "total_amount", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://capstone-comiverse/transactions/",
        "partitionKeys": [],
    },
    format_options={"compression": "gzip"},
    transformation_ctx="S3bucket_node3",
)

job.commit()
