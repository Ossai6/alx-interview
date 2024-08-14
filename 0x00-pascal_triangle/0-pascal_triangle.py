#!/usr/bin/python3
'''A module for working with Pascals triangle
'''


def pascal_triangle(n):
    '''Implementation'''
    try:
        # Validate that the input is a positive integer
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Input must be a positive integer greater than 0.")
                                                
        # Initialize the triangle with the first row
        triangle = [[1]]
                                                                
        # Construct the Pascal's triangle row by row
        for i in range(1, n):
            # Start each row with a '1'
            row = [1]
            # Calculate the values in between using the previous row
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # End each row with a '1'
            row.append(1)
            triangle.append(row)
        
        return triangle

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
