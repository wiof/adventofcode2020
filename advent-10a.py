from functools import lru_cache
m= [0,
1,
2,
3,
4,
7,
8,
9,
10,
11,
14,
15,
18,
19,
20,
21,
22,
25,
26,
27,
30,
31,
32,
33,
36,
39,
40,
41,
42,
45,
46,
49,
52,
53,
54,
55,
56,
59,
60,
61,
64,
65,
66,
69,
70,
71,
72,
73,
76,
77,
78,
81,
82,
83,
84,
87,
88,
89,
92,
93,
94,
95,
98,
99,
100,
101,
104,
107,
108,
109,
110,
113,
114,
115,
116,
119,
122,
123,
124,
127,
128,
129,
130,
131,
134,
137,
140,
141,
142,
143,
146,
149,
150,
151,
152,
155,
156,
157,
158,
161,
164,
165,
166,
167
]
'''
m=[0,
1,
2,
3,
4,
7,
8,
9,
10,
11,
14,
17,
18,
19,
20,
23,
24,
25,
28,
31,
32,
33,
34,
35,
38,
39,
42,
45,
46,
47,
48,
49]
'''
one = 0
three = 0
for i in range(1,len(m)):
  if m[i] - m[i-1] == 1:
    one+=1
  elif m[i] - m[i-1] ==3:
    three+=1
  else:
    print("FAIL")

print(one,three)

@lru_cache(None)
def comb(n):
  if n == len(m)-1:
    return(1)
  ret = 0
  for i in range(3,0,-1):
    if n+i < len(m) and m[n+i] <= m[n] + 3:
      ret += comb(n+i)
  return(ret)
  
print(comb(0))
