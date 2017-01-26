y='Little Rock,Boise,Richmond,Denver,Olympia,Sacramento,Springfield,Baton Rouge,Tallahassee,Austin,Trenton,Lansing,Annapolis,Dover,Phoenix,Pierre,Charleston,Salt Lake City,Montpelier,Indianapolis,Concord,Providence,Madison,Oklahoma City,Santa Fe,Frankfort,Columbia,Atlanta,Boston,Salem,Juneau,Bismarck,Helena,Montgomery,Des Moines,Saint Paul,Jefferson,Lincoln,Hartford,Augusta,Carson City,Albany,Cheyenne,Columbus,Harrisburg,Honolulu,Raleigh,Nashville,Jackson,Topeka'.split(',')
z='Arkansas,Idaho,Virginia,Colorado,Washington,California,Illinois,Louisiana,Florida,Texas,New Jersey,Michigan,Maryland,Delaware,Arizona,South Dakota,West Virginia,Utah,Vermont,Indiana,New Hampshire,Rhode Island,Wisconsin,Oklahoma,New Mexico,Kentucky,South Carolina,Georgia,Massachusetts,Oregon,Alaska,North Dakota,Montana,Alabama,Iowa,Minnesota,Missouri,Nebraska,Connecticut,Maine,Nevada,New York,Wyoming,Ohio,Pennsylvania,Hawaii,North Carolina,Tennessee,Mississippi,Kansas'.split(',')
def a(b):
 m='Arstotzka'
 if b in y:m=z[y.index(b)]
 if b in z:m=y[z.index(b)]
 print m
