f(x)::Int64 = (x + ceil(abs(tan(rad2deg(x))))*ceil(log2(x))) % 2^32

function floyd(start)
    a = start
    b = f(a)

    println("a = $a")
    println("b = $b")

    while a != b
        a = f(a)
        b = f(f(b))
    end

    b =[]
    push!(b, f(a))

    t = 1

    while a != b[t]
        push!(b, f(b[t]))
        t = t + 1
    end
    println(a)
    @show b[end]
    println(t)
end

@time floyd(2)
