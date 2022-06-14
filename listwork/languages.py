frameworks=[
    ["django","python",4],
    ["flask","python",3],
    ["spring","java",5],
    ["express","javascript",4],
    ["angular","typescript",4],
]
# for fw in frameworks:
#     if fw[1]=="python":
#         print(fw)

python_fw=[fw for fw in frameworks if fw[1]=="python"]
print(python_fw)

popular_fw=[fw for fw in frameworks if fw[-1]>3 ]
print(popular_fw)