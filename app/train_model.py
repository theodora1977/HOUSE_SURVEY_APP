import pandas as pd
import joblib
from app.database import engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def train():
    print("Fetching data from database...")
    # 1. Fetch data directly from SQLite using pandas
    query = "SELECT * FROM houses"
    df = pd.read_sql(query, engine)

    if df.empty:
        print("No data found in 'houses' table. Please run 'python -m app.seed' first.")
        return

    print(f"Training on {len(df)} records...")

    # 2. Define Features (X) and Target (y)
    # We use the exact columns that the user inputs in the API
    X = df[['state', 'town', 'house_type', 'bedrooms', 'bathrooms', 'toilets', 'parking_space']]
    y = df['price']

    # 3. Create a Preprocessing Pipeline
    # We treat 'bedrooms' as a number, and everything else (including '5+' bathrooms) as categories
    categorical_features = ['state', 'town', 'house_type', 'bathrooms', 'toilets', 'parking_space']
    numeric_features = ['bedrooms']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', SimpleImputer(strategy='median'), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    # 4. Create the Model Pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # 5. Train the model
    model.fit(X, y)

    # 6. Save the trained model
    joblib.dump(model, "house_price_model.pkl")
    print("Success! Model saved to 'house_price_model.pkl'")

if __name__ == "__main__":
    train()