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

    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    total_time = 0

    while current_stop != second_stop:
        for (start, end), travel_time in route_map.items():
            if start == current_stop:
                total_time += travel_time
                current_stop = end
                break

    return total_time