df = spark.table('skit.raw_table')
raw_defs = {}
curated_defs = {}
presentation_defs = {}

for row in df.collect():

    raw_table = row['RawTableName']
    raw_col = f"{row['RawTableColumn']} {row['RawTableColDatatype']}"
    if raw_table in raw_defs:
        raw_defs[raw_table].append(raw_col)
    else:
        raw_defs[raw_table] = [raw_col]

    curated_table = row['CuratedTableName']
    curated_col = f"{row['CuratedTableColumn']} {row['CuratedTableColumnDatatype']}"
    if curated_table in curated_defs:
        curated_defs[curated_table].append(curated_col)
    else:
        curated_defs[curated_table] = [curated_col]

    presentation_table = row['PresntationLayTableName']
    presentation_col = f"{row['PresentationLayercolumn']} {row['PresentationLayerColDataType']}"
    if presentation_table in presentation_defs:
        presentation_defs[presentation_table].append(presentation_col)
    else:
        presentation_defs[presentation_table] = [presentation_col]


def create_tables(layer_dict):
    for table_name, columns in layer_dict.items():
        column_list = ", ".join(columns)
        spark.sql(f"DROP TABLE IF EXISTS {table_name}")
        spark.sql(f"CREATE TABLE {table_name} ({column_list})")
        print(f" Table created: {table_name}")


create_tables(raw_defs)
create_tables(curated_defs)
create_tables(presentation_defs)
