def findMinMoves(machines):
    total_dresses=sum(machines)
    n=len(machines)
    if total_dresses%n!=0:
        return -1
    average_dresses=total_dresses//n
    moves=0
    balance=0
    for dresses in machines:
        balance+=dresses-average_dresses
        moves=max(moves,abs(balance),dresses-average_dresses)
    return moves
machines=[1,0,5]
print("\nMinimum number of moves = ",findMinMoves(machines))