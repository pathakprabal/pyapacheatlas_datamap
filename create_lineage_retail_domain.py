#
# NOTE - Run the command "az login" first so that your CLI is set up to connect to Purview as YOU.
#

import argparse
import excel_upload_all

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-PurviewAccount', required=True, dest='acctName', type=str, help='Name of the Purview account')
    args = parser.parse_args()

    excel_upload_all.UploadToPurview('./Data_Map_Lineage_Retail.xlsx', args.acctName)

