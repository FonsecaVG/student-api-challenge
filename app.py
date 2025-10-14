from flask import Flask, request, jsonify

# List to simulate the database
students_list = []

# Variables for sequencial IDs
next_student_id = 1


app = Flask(__name__)


# Logic Function: finds first non-repeating char
def get_unique_char(name):

    # Converts to lowercase and only alpha chars
    filtered_name = ''.join(c.lower() for c in name if c.isalpha())
    if not filtered_name:
        return '_'
    
    for char in filtered_name:
        if filtered_name.count(char) == 1:
            return char
    return "_"

# POST /students: Add a new student
@app.route('/students', methods=['POST'])
def register_student():
    global next_student_id

    data = request.get_json()
    # JSON data validation
    if not data:
        return jsonify({'error': 'Missin JSON data'}), 400

    student_name = data.get('name')
    student_grade = data.get('grade')

    # Fields validation
    if not student_name or student_grade is None:
        return jsonify({'error': 'Missing "name" or "grade"'}), 400
    
    # Ensures grade between 0 and 10.
    try:
        student_grade = float(student_grade)
        if not(0<= student_grade <=10):
            return jsonify({'error': 'Grade must be between 0 and 10'}), 400
    except (ValueError, TypeError):

        return jsonify({'error': 'Grade must be a valid number'})
    
    # Creates a new
    new_student = {
        'id': next_student_id,
        'name': student_name,
        'grade': student_grade,
        'unique_char': get_unique_char(student_name)
    }


    # Store new_student in the list.
    students_list.append(new_student)
    next_student_id += 1

    return jsonify(new_student), 201

# GET /student: Returns a list of all students
@app.route('/students', methods=['GET'])
def list_students():

    # Prepares de response list and recalculate the 'unique_char'
    response_list = [
        {
        'id': s['id'],
        'name': s['name'],
        'note': s['grade'],
        'unique_char': get_unique_char(s['name'])
    }
    for s in students_list ]

    # Returns the updated list as JSON with 200(OK) status 
    return jsonify(response_list), 200

# GET /students/<int:student_id>: Returns data for a specific student
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    
    id_found = None
    
    # Search for students ID
    for s in students_list:
        if s['id'] == student_id:
            id_found = s
            break
    
    # Verify if ID is not None.
    if id_found is None:
        return jsonify({'error': f'Student with ID {student_id} not found'}), 404

    # Response prep: Ensure the response includes all fields
    response_data = {
        'id': id_found['id'],
        'name': id_found['name'],
        'grade': id_found['grade'],
        'unique_char': get_unique_char(id_found['name'])
    }

    return jsonify(response_data), 200


if __name__ == '__main__':
# Starts the Flask development server
    app.run(debug=True)