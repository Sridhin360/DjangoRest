from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# In-memory list to store student data
students = [{"name":"sam", "email":"sam@gmail.com"}]

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_list(request):
    # GET - Retrieve all students
    if request.method == 'GET':
        return Response(students)
    
    # POST - Add a new student
    elif request.method == 'POST':
        student = request.data
        students.append(student)
        return Response({"message": "Student added successfully"})
    
    # PUT - Update a specific student by name
    elif request.method == 'PUT':
        student_data = request.data
        name_to_update = student_data.get('name')

        for student in students:
            if student['name'] == name_to_update:
                student.update(student_data)
                return Response({"message": "Student updated successfully"}, status=status.HTTP_200_OK)
        
            else:
                return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # DELETE - Remove a specific student by name
    elif request.method == 'DELETE':
        name_to_delete = request.GET.get('name')
        print('name',name_to_delete)
        
        for student in students:
            if student['name'] == name_to_delete:
                students.remove(student)
                return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
