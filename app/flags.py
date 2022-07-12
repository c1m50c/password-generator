from typing import Dict, List


def get_flags(args: List[str]) -> Dict[str, List[str]]:
    """
        Returns a dictionary containing the flags within the passed through command line arguments.
        
        # Example
        ```py
        # $ py ./src/main.py normal_argument -flag1 Hello, World -flag2 -flag3 This is the third flag.
        flags = get_flags(sys.argv[1::])
        expected_flags = {
            "-flag1": ["Hello,", "World"],
            "-flag2": [  ],
            "-flag3": ["This", "is", "the", "third", "flag."],
        }
        
        assert flags == expected_flags
        ```
    """
    
    result: Dict[str, List[str]] = {  }
    
    while args:
        current = args.pop(0)
        
        if current[0] == "-":
            result[current] = [  ] # Flag Parameters
            
            while args:
                if args[0][0] == "-": break
                result[current].append(args.pop(0))
    
    return result