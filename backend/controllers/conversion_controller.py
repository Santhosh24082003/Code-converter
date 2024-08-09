from flask import request, jsonify
from services.gemini_service import convert_code

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
