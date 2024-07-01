import io
# import pandas as pd
import os
import requests
import zipfile
from google.cloud import storage

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

year = 2024
quarter = 1

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Reading data from Indego CSV
    """
 
    headers = {'User-Agent':'student-application'}
    
    url = f'https://www.rideindego.com/wp-content/uploads/2024/04/indego-trips-{year}-q{quarter}.zip' 
 
    response = requests.get(url, headers=headers)    
    return response.status_code

    # return pd.read_csv(io.StringIO(response.text), sep=',', nrows = 100, compression='zip')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
