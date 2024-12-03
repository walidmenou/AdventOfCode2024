import re
import os
import heapq

def execute_code():
    # Get input file content
    current_dir = os.getcwd()
    input_path = os.path.join(current_dir, "day3", "input3.txt")
    with open(input_path, "r") as f:
        content = f.read()

    # Define our patterns
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'

    # Get all matches with their positions
    # We create a priority queue of (position, instruction_type, values)
    instruction_queue = []
    
    # Add "do" instructions to our queue
    for match in re.finditer(do_pattern, content):
        heapq.heappush(instruction_queue, (match.start(), "do", None))
    
    # Add "dont" instructions to our queue
    for match in re.finditer(dont_pattern, content):
        heapq.heappush(instruction_queue, (match.start(), "dont", None))
    
    # Add multiplication instructions with their values
    for match in re.finditer(mul_pattern, content):
        num1, num2 = match.groups()  # Get the captured numbers
        heapq.heappush(instruction_queue, (match.start(), "mul", (int(num1), int(num2))))

    # Process instructions in order
    result = 0
    should_execute = False  # Tracks whether we should execute multiplications
    
    # Process each instruction in order of appearance
    while instruction_queue:
        position, instruction_type, values = heapq.heappop(instruction_queue)
        
        if instruction_type == "do":
            should_execute = True
        elif instruction_type == "dont":
            should_execute = False
        elif instruction_type == "mul" and should_execute:
            # Only execute multiplication if we've seen a "do" and no "dont" since
            num1, num2 = values
            result += num1 * num2

    return result

print(execute_code())