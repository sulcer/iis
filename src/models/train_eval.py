import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

if __name__ == "__main__":
    df = pd.read_csv("data/processed/current_data.csv")

    target_column = 'Dropout'
    y = df[target_column]
    X = df.drop(target_column, axis=1)

    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    print(numeric_features)
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_features = X.select_dtypes(include=['object']).columns
    print(categorical_features)
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', RandomForestClassifier())
    ])

    X_train = X[1:]
    y_train = y[1:]
    X_test = X[:1]
    y_test = y[:1]

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    print(predictions)

    joblib.dump(pipeline, 'models/model.joblib')
