#!/usr/bin/env julia

function f(n)
    i = c = 1
    while c < n
        d = digits(i += 1)
        all(d .> 0) && i % sum(d) == i % prod(d) < 1 && (c += 1)
    end
    return i
end

print(f(int(readline())))