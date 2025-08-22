# core/planner.py
import google.generativeai as genai
from config import GOOGLE_API_KEY
import platform  # Import the platform module to detect the OS

# Configure the library with your API key
try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    print(f"Error configuring Google AI: {e}")
    print("Please ensure the GOOGLE_API_KEY is set correctly.")
    exit()

# Create the Generative Model instance
model = genai.GenerativeModel('gemini-1.0-pro')

# Define safety settings to be less restrictive
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

def get_command_from_prompt(prompt: str) -> str:
    # *** NEW: Detect the user's operating system ***
    os_name = platform.system()

    # *** NEW: Create a more specific prompt that includes the OS ***
    system_prompt = (
        f"You are a command line expert for the '{os_name}' operating system. "
        f"What is the single, executable system command to: {prompt}? "
        "Only return the command itself, with no explanation, code blocks, or any other text."
    )

    response = model.generate_content(
        system_prompt,
        safety_settings=safety_settings
    )
    
    try:
        command = response.text.strip()
    except ValueError:
        print("Warning: The AI response was blocked by its internal safety filters.")
        print("Details:", response.prompt_feedback)
        return "echo 'AI response was blocked.'"

    if command.startswith("```") and command.endswith("```"):
        command_lines = command.splitlines()
        if len(command_lines) > 1:
            # Extract command from markdown block (e.g., ```bash\ncommand\n```)
            command = ''.join(line for line in command_lines if not line.startswith("```"))
        else:
            command = ""

    return command.strip().replace("`", "")