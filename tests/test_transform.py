from src.transform import *
import pandas as pd
from src.make_parquet import (index, get_parquet)
import pytest
import os
from moto import (mock_secretsmanager, mock_s3)
import boto3


# check no duplicates
# check not null
# check datatype and convert to the star schema datatype (perhaps to be done at a later date - check with tutors)


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""

    os.environ['AWS_ACCESS_KEY_ID'] = 'test'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
    os.environ['AWS_SECURITY_TOKEN'] = 'test'
    os.environ['AWS_SESSION_TOKEN'] = 'test'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'


@pytest.fixture(scope='function')
def premock_s3(aws_credentials):
    with mock_s3():
        yield boto3.client('s3', region_name='us-east-1')


@pytest.fixture
def mock_bucket_and_parquet_files(premock_s3):
    premock_s3.create_bucket(
        Bucket='scrumptious-squad-in-data-testmock',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'}
    )
    
    index('config/.env.test')
    # The parquet files should be generated in the mock bucket.


def test_your_test(mock_bucket_and_parquet_files, premock_s3):
    premock_s3.list_objects(
        Bucket='scrumptious-squad-in-data-testmock'
    )
    address_table = get_parquet('address')
    print(address_table)


def test_dim_date():
    start_date = '2023-03-26'
    end_date = '2023-03-27'
    dim_date = create_dim_date(start_date, end_date)
    assert dim_date.shape[1] == 8
    assert dim_date['year'][1] == 2023
    assert dim_date['month'][1] == 3
    assert dim_date['day'][1] == 27
    assert dim_date['day_of_week'][1] == 1
    assert dim_date['day_name'][1] == 'Monday'
    assert dim_date['month_name'][1] == 'March'
    assert dim_date['quarter'][1] == 1


def test_dim_location():
    dim_location = create_dim_location()
    assert dim_location.shape[1] == 8

def test_dim_design():
    dim_design = create_dim_design()
    assert dim_design.shape[1] == 4

def test_dim_currency():
    dim_currency = create_dim_currency()
    assert dim_currency.shape[1] == 3

def test_dim_counterparty():
    dim_counterparty = create_dim_counterparty()
    assert dim_counterparty.shape[1] == 9

def test_dim_staff():
    dim_staff = create_dim_staff()
    assert dim_staff.shape[1] == 6


def test_fact_sales_order_table_has_the_right_number_of_columns():

    sales_order_table = create_facts_sales_order_table()
    actual_output = sales_order_table.shape[1]
    expected_output = 15

    assert expected_output == actual_output

def test_sales_record_id_column_is_int_and_it_is_increasing_by_1_each_row():
    
    sales_order_table = create_facts_sales_order_table()

    assert sales_order_table['sales_record_id'][0] == 1
    assert sales_order_table['sales_record_id'][1] == 2
    assert sales_order_table['sales_record_id'][100] == 101
    assert sales_order_table['sales_record_id'][147] == 148
    assert sales_order_table['sales_record_id'][927] == 928

