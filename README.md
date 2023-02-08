# pyapacheatlas_datamap
A python script to help work with the apache atlas REST APIs and create datamap and classification on Purview


**Prerequisites:**
- install python 3.8.x
- install azure-identity by running pip install azure-identity
- install openpyxl by running pip install openpyxl
- install pyapacheatlas by running pip install pyapacheatlas




**Using Excel to Accelerate Metadata Uploads**
- Bulk upload entities.
- Upload entities / assets for built-in or custom types.
- Supports adding glossary terms to entities.
- Supports adding classifications to entities.
- Supports creating relationships between entities (e.g. columns of a table).
- Creating custom lineage between existing entities.
- Defining Purview Column Mappings / Column Lineage.
- Bulk upload custom type definitions.
- Bulk upload of classification definitions (Purview Classification Rules not supported).


**Using Exel to create Datamap and Classification on Purview account:**
- Step 1: Downlod the file DataMap_lineage_Healthcare.xlsx
- Step 2: Save 'create_lineage_healthcare_domain' script in your local machine with '.py extension'
- Step 3: Update the Purview Account name (line 24 -account_name = "Purview-Instance-Name") and File location in the script (line 27 )
- Step 4: Goto command prompt and run the command "az login". This will open a web page to confirm your login on Azure
- Step 5: Goto command prompt and exceute the script - 'python ./create_lineage_healthcare_domain.py'

___________________________________________________________________________________________________________________________________________________________

- Additional Resources
Learn more about this package in the PyApacheAtlas docs.
The Apache Atlas REST API
The Purview CLI Package provides CLI support.
Purview REST API Official Docs
https://github.com/wjohnson/pyapacheatlas
