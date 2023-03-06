from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import sqlite3

# Initialize Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create the uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Database Functions
def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Makes the query results accessible by column name
    return conn

def init_db():
    """Initialize the database with the required tables."""
    db = get_db_connection()
    db.execute('''CREATE TABLE IF NOT EXISTS annotations (
                      id INTEGER PRIMARY KEY, 
                      image_path TEXT, 
                      annotation_data TEXT)''')
    db.commit()
    db.close()

# Initialize the database
init_db()

# Routes
@app.route('/')
def index():
    """Render the main page of the web app."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    """Handle image uploads."""
    file = request.files['image']
    if file:
        filename = secure_filename(file.filename)  # Ensure a secure filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)  # Save the file

        # Insert file information into the database
        db = get_db_connection()
        db.execute('INSERT INTO annotations (image_path, annotation_data) VALUES (?, ?)',
                   (file_path, ''))
        db.commit()
        db.close()
        return jsonify({'message': 'Image uploaded successfully', 'path': file_path})
    return jsonify({'message': 'No file uploaded'})

@app.route('/annotations', methods=['GET', 'POST'])
def annotations():
    """Handle fetching and updating annotations."""
    if request.method == 'GET':
        # Get all annotations from the database
        db = get_db_connection()
        annotations = db.execute('SELECT * FROM annotations').fetchall()
        db.close()
        return jsonify([dict(row) for row in annotations])
    elif request.method == 'POST':
        # Update an existing annotation
        data = request.json
        db = get_db_connection()
        db.execute('UPDATE annotations SET annotation_data = ? WHERE id = ?',
                   (data['annotation_data'], data['id']))
        db.commit()
        db.close()
        return jsonify({'message': 'Annotation updated'})



@app.route('/save-annotations', methods=['POST'])
def save_annotations():
    data = request.json
    canvas_json = data['canvasJson']
    canvas_image = data['canvasImage']

    # Process and save the JSON and Image data
    # For example, save to a file or a database
    with open('canvas_data.json', 'w') as file:
        file.write(canvas_json)

    # Save the canvas image
    # The image is in Base64, so it needs to be decoded
    import base64
    image_data = base64.b64decode(canvas_image.split(',')[1])
    with open('canvas_image.png', 'wb') as file:
        file.write(image_data)

    return jsonify({'message': 'Annotations saved successfully'})




# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
