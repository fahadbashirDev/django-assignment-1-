"""
Train a simple Machine Learning model (Iris flower species classifier)
and save it to disk so Django can load and use it for real-time predictions.

Run this once before starting the server:
    python core/ml/train_model.py
"""
import os
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

MODEL_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(MODEL_DIR, 'iris_model.pkl')


def train_and_save_model():
    data = load_iris()
    X, y = data.data, data.target
    target_names = data.target_names

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f'Model trained. Test accuracy: {acc:.2f}')

    joblib.dump({'model': model, 'target_names': list(target_names)}, MODEL_PATH)
    print(f'Model saved to {MODEL_PATH}')


if __name__ == '__main__':
    train_and_save_model()
