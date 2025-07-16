# app.py
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, session
import os
from werkzeug.utils import secure_filename
from ocr import perform_ocr
from logic_solver import solve_logic_problem # Assuming this function exists and takes text input

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(24) # A secret key for session management
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Create the uploads directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
    print(f"Created upload directory: {app.config['UPLOAD_FOLDER']}")

def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Renders the main upload form page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles file upload, performs OCR, solves logic, and redirects to results."""
    if 'questionImage' not in request.files:
        # Handle case where no file part in the request
        print("No file part in request.")
        return render_template('result.html', error="कोई फ़ाइल अपलोड नहीं की गई।")

    file = request.files['questionImage']

    if file.filename == '':
        # Handle case where no file was selected
        print("No selected file.")
        return render_template('result.html', error="कोई फ़ाइल नहीं चुनी गई।")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            file.save(filepath)
            print(f"File saved successfully: {filepath}")

            # Perform OCR on the uploaded image
            extracted_text = perform_ocr(filepath)
            print(f"OCR Extracted Text: {extracted_text}")

            if not extracted_text.strip():
                # If OCR extracts no meaningful text
                return render_template('result.html', error="तस्वीर से कोई पाठ नहीं निकाला जा सका। कृपया एक स्पष्ट तस्वीर अपलोड करें।", extracted_text=extracted_text)

            # Solve the logic problem based on the extracted text
            # Assuming logic_solver.py has a function like solve_logic_problem(text)
            # This is where you would integrate your logic to fetch answers from GitHub or apply rules.
            # For this example, we'll pass the extracted text directly.
            # In a real scenario, logic_solver.py would parse this text and find the answer.
            answer = solve_logic_problem(extracted_text)
            print(f"Logic Solver Answer: {answer}")

            # Store results in session to pass to result.html
            session['extracted_text'] = extracted_text
            session['answer'] = answer

            return redirect(url_for('show_result'))
        except Exception as e:
            print(f"Error processing file: {e}")
            return render_template('result.html', error=f"फ़ाइल संसाधित करते समय त्रुटि हुई: {e}")
    else:
        # Handle disallowed file types
        print("File type not allowed.")
        return render_template('result.html', error="अमान्य फ़ाइल प्रकार। केवल JPG, PNG, GIF, WebP छवियाँ ही अनुमति हैं।")

@app.route('/result')
def show_result():
    """Renders the result page with extracted text and answer."""
    extracted_text = session.pop('extracted_text', 'कोई पाठ नहीं मिला।')
    answer = session.pop('answer', 'कोई उत्तर नहीं मिला।')
    return render_template('result.html', extracted_text=extracted_text, answer=answer)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serves uploaded files (e.g., for debugging or display if needed)."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

