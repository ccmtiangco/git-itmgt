def relationship_status(from_member, to_member, social_graph):
    
    # Check if from_member follows to_member
    from_follows_to = to_member in social_graph.get(from_member, {}).get("following", [])

    # Check if to_member follows from_member
    to_follows_from = from_member in social_graph.get(to_member, {}).get("following", [])

    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"
    
def tic_tac_toe(board):
    
    n = len(board)

    # Check for horizontal wins
    for row in board:
        if row[0] != '' and all(symbol == row[0] for symbol in row):
            return row[0]

    # Check for vertical wins
    for col in range(n):
        if board[0][col] != '' and all(board[row][col] == board[0][col] for row in range(1, n)):
            return board[0][col]

    # Check for diagonal win (top-left to bottom-right)
    if board[0][0] != '' and all(board[i][i] == board[0][0] for i in range(1, n)):
        return board[0][0]

    # Check for diagonal win (top-right to bottom-left)
    if board[0][n-1] != '' and all(board[i][n-1-i] == board[0][n-1] for i in range(1, n)):
        return board[0][n-1]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    
    # If the start and end stops are the same, travel time is 0.
    if first_stop == second_stop:
        return 0

    current_stop = first_stop
    total_travel_time = 0

    # Loop until the shuttle reaches the destination.
    while current_stop != second_stop:
        # Find the leg that starts at the current stop.
        for (start, end), time_info in route_map.items():
            if start == current_stop:
                # Add the travel time for this leg.
                total_travel_time += time_info["travel_time_mins"]
                # Move to the next stop.
                current_stop = end
                # Break the inner loop since we found the next leg.
                break
                
    return total_travel_time