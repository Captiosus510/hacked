import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Create Flask app
app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle file upload
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Call your algorithm here to get the movie name
            movie_name = analyze_file(filepath)
            
            # Pass the result to the template
            return render_template('index.html', movie_name=movie_name)
    
    return render_template('index.html')

# Example function to analyze the file
def analyze_file(filepath):
    return "Inception"  # Replace with actual result from your algorithm

if __name__ == '__main__':
    app.run(debug=True)
