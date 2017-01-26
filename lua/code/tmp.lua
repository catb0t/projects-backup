-- TMP
-- CCode Projects
local Parser = {Code = "3a1.3b0.1;4+a>T8%a>xFFF14+b>a8%b>xFFF11~5<b>164|b>a2$b$", Args = {"asdasd"}, Index = 1, Env = {}, Temp = 0, Marker = -1, Iterations = 0, ForIndex = 0}
function Parser.value(v)
	if v == "E" then return Parser.Temp end
	if v == "T" then return Parser.Args[Parser.ForIndex] end
	if v:sub(1,1) == "x" then
		return tonumber(v:sub(2), 16)
	else
		return tonumber(v) or Parser.Env[v]
	end
end
function Parser.eval(o,f,s)
	local a = Parser.value(f)
	local b = Parser.value(s)
	if o == "+" then return a + b end
	if o == "-" then return a - b end
	if o == "/" then return a / b end
	if o == "*" then return a * b end
	if o == "%" then return a % b end
	if o == "|" then return bit32.bor(a, b) end
	if o == "&" then return bit32.band(a, b) end
	if o == "^" then return bit32.bnot(a, b) end
	if o == "<" then return bit32.lshift(a, b) end
	if o == ">" then return bit32.rshift(a, b) end
	return math.floor((a + b) / 2)
end
function Parser.next()
	local r = Parser.Code:sub(Parser.Index,Parser.Index)
	Parser.Index = Parser.Index + 1
	return r
end
function Parser.nextLine()
	local length = Parser.next()
	if length ~= "$" then
		local line = ""
		for i = 1, tonumber(length) do
			line = line .. Parser.next()
		end
		Parser.runLine(line)
		Parser.nextLine()
	end
end
function Parser.runLine(line)
	if line:sub(#line) == "." then Parser.Env[line:sub(1,1)] = Parser.value(line:sub(2)) return end
	if line:sub(1,1) == "$" then print(Parser.value(line:sub(2))) end
	local d = line:find(">", 2, true)
	local temp = false
	if d == nil then temp = true d = line:find("&", 2, true) end
	if d ~= nil then
		local result = Parser.eval(line:sub(1, 1), line:sub(2, d - 1), line:sub(d + 1))
		if temp then
			Parser.Temp = result
		else
			if Parser.Env[line:sub(2, d - 1)] ~= nil then
				Parser.Env[line:sub(2, d - 1)] = result
			end
		end
	elseif line == ";" then
		Parser.Marker = Parser.Index
		Parser.Iterations = #Parser.Args - 1
		Parser.ForIndex = 1
	elseif line == "~" then
		if Parser.Iterations > 0 then
			Parser.Index = Parser.Marker
			Parser.Iterations = Parser.Iterations - 1
			Parser.ForIndex = Parser.ForIndex + 1
		end
	end
end
Parser.nextLine()