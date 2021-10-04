# fixed_length_file_parser.py

# Note that start positions in the column data below assume the
# first character is at postion 1, rather than typical zero-indexed
# characters per line. We"ll subtract 1 from each start value in the
# code below

from decimal import Decimal


# Converts the column value to the column's type
def convert_type(column_value, column_datatype):

  length = len(column_value)

  # Convert "numeric" datatype to long
  if column_datatype == "numeric":
    column_value = long(column_value)

  # Convert "decimal" datatype to decimal with two decimal places
  elif column_datatype == "decimal":
    if column_value == "000000":
      column_value = Decimal("0.00")
    elif length == 1:
      column_value = Decimal("0.0" + column_value)
    elif length == 2:
      column_value = Decimal("0." + column_value)
    else:
      # insert decimal point before last two digits
      column_value = column_value[0 : length - 2] + "." + column_value[length - 2]
      # convert to decimal
      column_value = Decimal(column_value)

  return column_value


# Parses the given row using the given column definitions
def parse_row(row, columns):
  parsed_row = {}
  for column in columns:
    start_position = column["start-position"] - 1 # see comment above
    end_position = start_position + column["length"]
    if end_position <= len(row):
      column_value = row[ start_position : end_position ].strip()
      if not (column_value is None or column_value == '' or len(column_value) == 0):
        column_value = convert_type(column_value, column["datatype"])
        parsed_row[column["name"]] = column_value
  return parsed_row

# Parse header line
def parse_header_line(row, format):
  return parse_row(row, format.header_columns)

# Parse data line
def parse_data_line(row, format):
  return parse_row(row, format.data_columns)

# Parse footer line
def parse_footer_line(row, format):
  return parse_row(row, format.footer_columns)
