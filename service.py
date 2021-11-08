import lib.db_utils as utils


def extract():
    """Get data to be recorded
    """
    datasource = utils.get_df_from_query(
        query="SELECT * FROM source_students", table_name_cols=False)
    return datasource


def transform(raw_data):
    clean_df = raw_data.rename(columns={'student_id': 'source_student_id'})
    if clean_df.isnull().values.any():
        raise Exception("A value in datasource is null")
    return clean_df


def load(df):
    print(f"Loading {df.shape[0]} to warehouse")
    rows = utils.insert_df_into_db(df, 'warehouse_students', list(df.columns))
    print(str(rows)+' rows were inserted')


if __name__ == "__main__":

    # Extract
    data_raw = extract()
    print(f"Extracted {len(data_raw['student_id'])} registers")

    # Transform
    clean_df = transform(data_raw)
    print(f"{clean_df.shape[0]} registers after transform")

    # Load
    load(clean_df)
    print("Done")
