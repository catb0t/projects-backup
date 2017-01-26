(lambda A:
    all(
        [F(A) for F in [
            lambda r: all(
                map(
                    lambda s:
                        not(
                            lambda i, b:
                                lambda n:
                                    list(filter(
                                        lambda i: not n % i, range(2, n)))
                            )(int(i, b))(r, s),
                            range(2, 11))),
            lambda r: 0 != len(filter(lambda d: d not in "01", r)),
            lambda r: 0 < len(r) < 6
            ]
        ]
    )
)

(lambda A:all([F(A)for F in[lambda r:all(map(lambda s:not(lambda i,b:lambda n:list(filter(lambda i:not n%i,range(2,n)))(int(i,b))(r,s),range(2,11))),lambda r:0!= len(filter(lambda d:d not in"01",r)),lambda r:0<len(r)<6]]))