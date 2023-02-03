#
# NOTE - Run the command "az login" first so that your CLI is set up to connect to Purview as YOU.
#

import json
import os
import argparse

from openpyxl import Workbook
from openpyxl import load_workbook

# PyApacheAtlas packages
# Connect to Atlas via a Service Principal
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient, AtlasEntity
from pyapacheatlas.readers import ExcelConfiguration, ExcelReader

# Connect to Atlas via Windows credentials
from azure.identity import AzureCliCredential

cred = AzureCliCredential()

def UploadToPurview(xls, instance):

    # Connect to Purview using Windows Auth
    client = PurviewClient( account_name = instance, authentication = cred)

    # SETUP: This is just setting up the excel file to use
    excel_config = ExcelConfiguration()
    excel_reader = ExcelReader(excel_config)
    file_path = xls

    # ACTUAL WORK:
    # Parse your custom type defs
    typedefs = excel_reader.parse_entity_defs(file_path)
    # Upload the typedefs. Set force_update to True so it's easier to repeat this step
    _ = client.upload_typedefs(typedefs, force_update=True)
    
    print("Finished uploading typedefs.")

    # Parse the bulk entities from excel
    tables_cols = excel_reader.parse_bulk_entities(file_path)
    # Upload the entities
    table_col_results = client.upload_entities(tables_cols)

    print("Finished uploading entities.")

    # Parse the lineage information from excel
    lineage_with_mapping_processes = excel_reader.parse_update_lineage_with_mappings(file_path)

    # Upload the lineage data
    lineage_results = client.upload_entities(lineage_with_mapping_processes)

    print("Finished uploading lineage information.")

    print(json.dumps([table_col_results, lineage_results], indent=2))

    print("Search for 'Data Map and Classification Created Succesfully' to see your results.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-excel', required=True, dest='excel_path', type=str, help='Specify full path to an excel file')
    parser.add_argument('-PurviewAccount', required=True, dest='acctName', type=str, help='Name of the Purview account')
    args = parser.parse_args()

    UploadToPurview(args.excel, args.acctName)