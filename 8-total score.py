'''Celculate total score:
Our football team has finished the championship.
Our team's match results are recorded in a collection of strings.
Each match is represented by a string in the format x:y, where x is our team and y is our opponents score.
The rules to calculate score is: 
If x > y: 3 points
If x < y: 0 point
If x = y: 1 point
We need to write a function that takes this collection and returns the number of points our team (x)
got in the championship by the rules given above.'''

def score(matches):
    total = 0
    for i in matches:
        x,y =map(int, i.split(':'))
        if x>y:
            total = total +3
        elif x==y:
            total = total + 1
    return total

matches = ['3:4','2:0','3:3','6:4']
print(score(matches))