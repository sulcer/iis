import pandas as pd


def main():
    current_data = pd.read_csv("data/processed/current_data.csv")
    reference_data = pd.read_csv("data/processed/reference_dataset.csv")

    validate_data(reference_data, current_data)


def validate_data(reference_data, data_to_validate):
    # column length
    if len(data_to_validate.columns) != len(reference_data.columns):
        print("Error: Column length does not match.")
        return False

    # column names
    if not data_to_validate.columns.equals(reference_data.columns):
        print("Error: Column names do not match.")
        return False

    # data types
    try:
        for column in data_to_validate.columns:
            ref_dtype = reference_data[column].dtype
            validate_dtype = data_to_validate[column].dtype
            if validate_dtype != ref_dtype:
                print(f"Error: data type for '{column}' not correct.")
                return False
    except KeyError:
        print("Error: Column names do not match.")
        return False

    print("Data validation successful!")
    return True


if __name__ == "__main__":
    main()
