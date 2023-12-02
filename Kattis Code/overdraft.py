transactions = int(input())
balance = 0
minimumSeen = 0


for i in range(transactions):
    balance += int(input())
    minimumSeen = min(minimumSeen, balance)

print( 0 - minimumSeen )