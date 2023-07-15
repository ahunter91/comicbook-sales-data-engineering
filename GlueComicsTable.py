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
        "dbtable": "comics",
        "connectionName": "comiverse_RDS-Glue",
    },
    transformation_ctx="MySQLtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=MySQLtable_node1,
    mappings=[
        ("unit_cost", "string", "unit_cost", "string"),
        ("comic_id", "int", "comic_id", "string"),
        ("title", "string", "title", "string"),
        ("binding", "string", "binding", "string"),
        ("publishing_format", "string", "publishing_format", "string"),
        ("year_published", "int", "year_published", "string"),
        ("publisher_id", "int", "publisher_id", "string"),
        ("publisher_name", "string", "publisher_name", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": "s3://capstone-comiverse/comics/", "partitionKeys": []},
    format_options={"compression": "gzip"},
    transformation_ctx="S3bucket_node3",
)

job.commit()
