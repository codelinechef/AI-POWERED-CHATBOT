import os
import google.generativeai as genai

print("--- Starting Final Test ---")

try:
    # Step 1: Load the API Key directly.
    # Ensure you have set this in your terminal for the final time.
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("CRITICAL ERROR: GOOGLE_API_KEY environment variable is not set in this terminal!")
    
    print("Successfully loaded API Key from environment.")

    # Step 2: Configure the client.
    genai.configure(api_key=api_key)
    print("Client configured successfully.")

    # Step 3: Attempt to list models. This is the simplest read-only operation.
    print("\nAttempting to list available models...")
    
    model_found = False
    for m in genai.list_models():
        # Check if a model that supports 'generateContent' exists.
        if 'generateContent' in m.supported_generation_methods:
            print(f"Found usable model: {m.name}")
            model_found = True
    
    if not model_found:
         print("\n!!! Could not find any models that support content generation. This points to a permissions issue. !!!")
    else:
         print("\nSUCCESS: Your API key and project setup are working correctly!")

except Exception as e:
    print(f"\n--- AN ERROR OCCURRED ---")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Details: {e}")
    print("--------------------------")
    print("If you see a 404 error here, the problem is 100% with the Google Cloud Project permissions, not your code.")