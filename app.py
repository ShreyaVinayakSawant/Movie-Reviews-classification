from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('movie_review_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    prediction = model.predict([review])[0]
    sentiment = 'positive' if prediction == 1 else 'negative'
    return render_template('index.html', prediction_text=f'The sentiment of the review is: {sentiment}')

if __name__ == '__main__':
    app.run(debug=True)
