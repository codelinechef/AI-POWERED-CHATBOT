# main.py
from core.planner import get_command_from_prompt
from core.executor import execute_command
from utils.safety import check_command_safety # Import the new function

def main():
    print("AI Command Assistant Initialized. What can I do for you?")
    while True:
        task = input("> What do you want me to do? Type 'exit' to quit: ").strip()
        if task.lower() == "exit":
            print("Exiting. Goodbye!")
            break

        if not task:
            continue

        try:
            command = get_command_from_prompt(task)
            print(f"Suggested command: {command}")

            # 1. Get the safety level of the command
            safety_level = check_command_safety(command)

            # 2. Handle the command based on its safety level
            if safety_level == 'SAFE':
                print("Executing safe command...")
                execute_command(command)

            elif safety_level == 'DANGEROUS':
                # *** NEW: Provide a stronger warning for dangerous commands ***
                print("\n!!! WARNING: THIS COMMAND IS POTENTIALLY DANGEROUS !!!")
                print("It can modify files, run programs, or change your system configuration.")
                confirm = input(f"Do you want to execute '{command}'? (y/n): ").lower()
                
                if confirm == 'y':
                    print("Executing...")
                    execute_command(command)
                else:
                    print("Execution cancelled.")
            
            else: # This handles 'UNKNOWN'
                print(f"Safety check failed. The command '{command}' is not in any of the recognized command lists and will not be executed.")

        except Exception as e:
            print(f"An error occurred while processing your request: {e}")
        
        print("-" * 40) # Add a separator for clarity

if __name__ == "__main__":
    main()