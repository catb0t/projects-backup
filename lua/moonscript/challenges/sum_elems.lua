local elems = io.read()
local x = { }
for i = 0, elems - 1 do
  table.insert(x, tonumber(io.read()))
end
local sum
sum = function(args)
  local y = 0
  for _index_0 = 1, #args do
    local elem = args[_index_0]
    y = y + elem
  end
  return y
end
return print(sum(x))
