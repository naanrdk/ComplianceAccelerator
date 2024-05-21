from flask import Flask, request, jsonify
import pandas as pd
import os
import hashlib

app = Flask(__name__)

# Sample sensitive data patterns
sensitive_data_patterns = {
    "email": r"[^@]+@[^@]+\.[^@]+",
    "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
    "ssn": r"\b\d{3}[-.]?\d{2}[-.]?\d{4}\b"
}

def classify_data(dataframe):
    classifications = {}
    for column in dataframe.columns:
        classifications[column] = []
        for pattern_name, pattern in sensitive_data_patterns.items():
            if dataframe[column].astype(str).str.contains(pattern, regex=True).any():
                classifications[column].append(pattern_name)
    return classifications

def anonymize_data(dataframe, classifications):
    for column, patterns in classifications.items():
        if 'email' in patterns:
            dataframe[column] = dataframe[column].apply(lambda x: hashlib.md5(x.encode()).hexdigest() if pd.notnull(x) else x)
        elif 'phone' in patterns or 'ssn' in patterns:
            dataframe[column] = dataframe[column].apply(lambda x: 'XXX-XX-XXXX' if pd.notnull(x) else x)
    return dataframe

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filename = os.path.join("/tmp", file.filename)
        file.save(filename)
        df = pd.read_csv(filename)
        classifications = classify_data(df)
        anonymized_df = anonymize_data(df, classifications)
        anonymized_filename = os.path.join("/tmp", "anonymized_" + file.filename)
        anonymized_df.to_csv(anonymized_filename, index=False)
        return jsonify({
            "classifications": classifications,
            "anonymized_file": anonymized_filename
        })

if __name__ == "__main__":
    app.run(debug=True)
