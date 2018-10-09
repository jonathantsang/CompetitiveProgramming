import sys

n = int(sys.stdin.readline())

queen = sys.stdin.readline().split()
queen = map(int, queen)
queenX = queen[0]-1
queenY = queen[1]-1

king = sys.stdin.readline().split()
king = map(int, king)

kingX = king[0]-1
kingY = king[1]-1

end = sys.stdin.readline().split()
end = map(int, end)

endX = end[0]-1
endY = end[1]-1

## Easy checks
if kingX <= queenX and queenX <= endX:
  print "NO"
elif endX <= queenX and queenX <= kingX:
  print "NO"
elif kingY <= queenY and queenY <= endY:
  print "NO"
elif endY <= queenY and queenY <= kingY:
  print "NO"
else:
  print "YES"