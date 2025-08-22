# A list of commands that are generally safe and do not modify the file system.
# We can be more lenient with these.
READ_ONLY_COMMANDS = [
    'ls', 'dir',  # List files
    'echo',       # Print text
    'ping',       # Check network
    'curl',       # Transfer data (can be abused, but often used for reading)
    'get-help',   # PowerShell help
    'man',        # Linux/macOS help
    'pwd',        # Print working directory
    'mkdir', 'md',
]

# A list of commands that can modify files, install software, or run applications.
# These require a strong warning and explicit user confirmation.
POTENTIALLY_DANGEROUS_COMMANDS = [
    'mkdir', 'md', # Make directory
    'cd',           # Change directory (low risk, but changes state)
    'python',       # Run python scripts
    'git',          # Version control
    'pip',          # Install packages
    'start',        # Windows command to open files/apps/URLs
    'open',         # macOS command to open files/apps/URLs
    'xdg-open',     # Linux command to open files/apps/URLs
    'touch',        # Create file
    'cp', 'copy',   # Copy files
    'mv', 'move',   # Move/rename files
    'rm', 'del',    # !!! VERY DANGEROUS: Delete files !!!
    'npm', 'npx',   # Node.js package manager
    'terraform',    # Infrastructure as code
    'kubectl',      # Kubernetes control
]

def check_command_safety(command: str) -> str:
    """
    Checks the command against tiered safety lists.
    Returns 'SAFE', 'DANGEROUS', or 'UNKNOWN'.
    """
    if not command:
        return 'UNKNOWN'
        
    command_word = command.split()[0].lower()

    if command_word in READ_ONLY_COMMANDS:
        return 'SAFE'
    
    if command_word in POTENTIALLY_DANGEROUS_COMMANDS:
        return 'DANGEROUS'
        
    return 'UNKNOWN'