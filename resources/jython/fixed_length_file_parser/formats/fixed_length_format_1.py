# fixed_length_file_parser.py

# Note that start positions in the column data below assume the
# first character is at postion 1, rather than typical zero-indexed
# characters per line. 


# header columns
header_columns = []
header_columns.append({"name": "MMED-IO-PREFIX", "start-position": 1, "length": 3, "datatype": "alpha"})
header_columns.append({"name": "MMED-IO-DATA-LENGTH", "start-position": 4, "length": 4, "datatype": "alpha"})
header_columns.append({"name": "filler", "start-position": 8, "length": 18, "datatype": "alpha"})
header_columns.append({"name": "Subscriber-ID", "start-position": 26, "length": 5, "datatype": "alpha"})
header_columns.append({"name": "Subscriber-ID Type", "start-position": 31, "length": 5, "datatype": "alpha"})
header_columns.append({"name": "Subscriber-ID Domain", "start-position": 36, "length": 4, "datatype": "alpha"})
header_columns.append({"name": "Subscriber-ID Source", "start-position": 40, "length": 4, "datatype": "alpha"})
header_columns.append({"name": "Create-Date", "start-position": 44, "length": 8, "datatype": "alpha"})
header_columns.append({"name": "Create-Time", "start-position": 52, "length": 8, "datatype": "alpha"})
header_columns.append({"name": "Batch-Number", "start-position": 60, "length": 7, "datatype": "alpha"})
header_columns.append({"name": "OOSEQ-IND", "start-position": 67, "length": 1, "datatype": "alpha"})
header_columns.append({"name": "RECORDS-IN-BATCH", "start-position": 68, "length": 8, "datatype": "alpha"})

# data columns: column name, start position, length
data_columns = []
data_columns.append({"name": "ERPO-JOB", "start-position": 8, "length": 4, "datatype": "alpha"})
data_columns.append({"name": "ERPO-DISTRIBUTION-CENTER", "start-position": 12, "length": 2, "datatype": "numeric"})
data_columns.append({"name": "ERPO-WAREHOUSE", "start-position": 14, "length": 2, "datatype": "numeric"})
data_columns.append({"name": "ERPO-DATE-CREATED", "start-position": 16, "length": 10, "datatype": "alpha"})
data_columns.append({"name": "ERPO-TIME-CREATED", "start-position": 26, "length": 8, "datatype": "alpha"})
data_columns.append({"name": "ERPO-PURCHASE-ORDER", "start-position": 34, "length": 18, "datatype": "alpha"})
data_columns.append({"name": "ERPO-RECEIPT", "start-position": 52, "length": 5, "datatype": "numeric"})
data_columns.append({"name": "ERPO-PRODUCT-ID", "start-position": 57, "length": 18, "datatype": "alpha"})
data_columns.append({"name": "ERPO-QTY-RECEIVED", "start-position": 75, "length": 7, "datatype": "numeric"})
data_columns.append({"name": "ERPO-QTY-DAMAGED", "start-position": 82, "length": 7, "datatype": "numeric"})
data_columns.append({"name": "ERPO-QTY-OVER-SHORT", "start-position": 89, "length": 8, "datatype": "alpha"})
data_columns.append({"name": "ERPO-CATCH-WEIGHT", "start-position": 97, "length": 9, "datatype": "decimal"})
data_columns.append({"name": "ERPO-CODE-DATE", "start-position": 106, "length": 10, "datatype": "alpha"})
data_columns.append({"name": "ERPO-NEW-COST", "start-position": 116, "length": 7, "datatype": "decimal"})
data_columns.append({"name": "ERPO-OFF-INVOICE", "start-position": 123, "length": 5, "datatype": "decimal"})
data_columns.append({"name": "ERPO-SYSTEM-FLAG", "start-position": 128, "length": 1, "datatype": "alpha"})
data_columns.append({"name": "ERPO-FT-RECV-QTY", "start-position": 130, "length": 7, "datatype": "numeric"})
data_columns.append({"name": "ERPO-FT-RECV-FLAG", "start-position": 137, "length": 1, "datatype": "alpha"})
data_columns.append({"name": "ERPO-WHSE-GEN-FT-DEMAND-FLAG", "start-position": 138, "length": 1, "datatype": "alpha"})
data_columns.append({"name": "ERPO-VENDOR", "start-position": 139, "length": 8, "datatype": "numeric"})
data_columns.append({"name": "ERPO-SOURCE", "start-position": 147, "length": 1, "datatype": "alpha"})
data_columns.append({"name": "ERPO-PO-TYPE", "start-position": 148, "length": 2, "datatype": "alpha"})
data_columns.append({"name": "ERPO_UNIT_SHIP_CASE", "start-position": 150, "length": 5, "datatype": "numeric"})
data_columns.append({"name": "ERPO_PALLET_ID", "start-position": 155, "length": 18, "datatype": "numeric"})

# footer columns: column name, start position, length
footer_columns = []
footer_columns.append({"name": "MMED-IO-PREFIX", "start-position": 1, "length": 3, "datatype": "alpha"})
footer_columns.append({"name": "MMED-IO-DATA-LENGTH", "start-position": 4, "length": 4, "datatype": "alpha"})
footer_columns.append({"name": "MMED-IO-DATA", "start-position": 8, "length": 8, "datatype": "alpha"})
