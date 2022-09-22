# 要求：如果输入的成绩在90分以上（含90分）输出A；
# 80分-90分（不含90分）输出B；
# 70分-80分（不含80分）输出C；
# 60分-70分（不含70分）输出D；
# 60分以下输出E。

# 定义成绩和等级变量
scores = int(input("请输入成绩："))
grade = 0

# 判断输入的成绩的评分。
if scores >= 90:
    grade = "A"
elif 80 <= scores < 90:
    grade = "B"
elif 70 <= scores < 80:
    grade = "C"
elif 60 <= scores < 70:
    grade = "D"
else:
    grade = "E"
print(grade)
