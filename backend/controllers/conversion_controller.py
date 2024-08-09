from flask import request, jsonify
from services.gemini_service import convert_code
import subprocess
import os

def convert():
    try:
        # Extract data from the request
        data = request.get_json()
        cobol_code = data.get('cobol_code')
        target_language = data.get('target_language')

        # Validate input data
        if not cobol_code or not target_language:
            return jsonify({"error": "COBOL code and target language are required."}), 400

        # Perform the code conversion using the service
        converted_code = convert_code(cobol_code, target_language)
        
        # Print the converted code for debugging
        print(f"Converted code:\n{converted_code}")

        return jsonify({"converted_code": converted_code})

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

def compile_code():
    try:
        data = request.get_json()
        code = data.get('code')
        language = data.get('language')

        if language == 'Python':
            output = run_python_code(code)
        elif language == '.NET':
            output = run_dotnet_code(code)
        else:
            return jsonify({"error": "Unsupported language"}), 400
        
        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def run_python_code(code):
    result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
    return result.stdout

import subprocess
import os

def run_dotnet_code(code):
    csproj_content = """<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>
</Project>"""

    with open('temp.csproj', 'w') as csproj_file:
        csproj_file.write(csproj_content)

    with open('temp.cs', 'w') as code_file:
        code_file.write(code)

    # Run dotnet restore to restore dependencies
    restore_result = subprocess.run(['dotnet', 'restore'], capture_output=True, text=True)
    if restore_result.returncode != 0:
        return f"Restore Error: {restore_result.stderr}"

    # Build the project
    build_result = subprocess.run(['dotnet', 'build', '--no-restore'], capture_output=True, text=True)
    if build_result.returncode != 0:
        return f"Build Error: {build_result.stderr}"

    # Run the project
    run_result = subprocess.run(['dotnet', 'run', '--project', 'temp.csproj'], capture_output=True, text=True)
    if run_result.returncode != 0:
        return f"Runtime Error: {run_result.stderr}"

    # Clean up temporary files
    os.remove('temp.cs')
    os.remove('temp.csproj')

    return run_result.stdout

