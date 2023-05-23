# Problem: 
# Book club members meet regularly for coffee at a round cafe table. Only a few members turn up randomly each time. It is a good thing that they keep records of who comes to each meeting, because one of them has been diagnosed with contagious book fever. It is very likely that if you sit next to someone with book fever, you will catch book fever.
# The file meetings1.txt contains the first names of all the attendees at each meeting, in the order they sat around the table. It contains:
# 1	Chuck Trevor
# 2	Zack Olive Xander Ephraim
# 3	Ralph Wendy Ephraim Grace Leslie Phil Kathy
# 4	Binh Harry Ralph Xander Zack Chuck Uma Suzy Phil Kathy
# 5	Neville Leslie Kathy
# 6	Neville Harry* Binh Vince Xander Zack Quisha Olive Phil
# 7	Yvonne Uma Trevor Fran Olive Phil Kathy
# 8	Harry Ralph Ephraim Denise Quisha Grace Phil
# 9	Binh Mandy Xander Ephraim Leslie Olive Fran
# 10	John Olive Chuck Mandy
# Poor Harry, at meeting number 6, is marked with an asterisk because we know he was infected with book fever then.
# Write a program that reports the names and number of club members infected up to each meeting from the first meeting where anyone was infected, like this:
# Enter file name: meetings1.txt
# 6	Harry Neville Binh 3
# 7	Harry Neville Binh 3
# 8	Harry Neville Binh Ralph Phil 5
# 9	Harry Neville Binh Ralph Phil Mandy Fran 7
# 10	Harry Neville Binh Ralph Phil Mandy Fran John Chuck 9 
# The program should work in general for any such file with exactly one name marked with an asterisk. The file meetings2.txt should produce this output.





