junk  = io.read!
nums  = io.read!
split = string.gmatch nums, "%S+"
x = {}
for item in *split!
  print tonumber( item)
  table.insert x, tonumber item

sum = (args) ->
  y = 0
  for elem in *args
    y = y + elem
  return y

print sum x