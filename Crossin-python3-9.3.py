# 读取raw成绩
with open('report.txt', encoding='utf-8') as f:
    score_rawli1 = f.readlines()
print(score_rawli1)
# 统计总分、平均分，并从高到低进行排序
score_finli = [score_rawli1[0].split()]
for i in score_rawli1[1:]:
    sum1 = 0
    score_personli = i.split()
    for j in score_personli[1:]:
        sum1 += int(j)
    avg1 = round(sum1 / 9, 1)
    score_personli.append(str(sum1))
    score_personli.append(str(avg1))
    score_finli.append(score_personli)
score_finli = sorted(score_finli, key=lambda a: a[-1], reverse=True)
print(score_finli)

# 汇总每一科目的平均分和总平均分
score_avgli = ['平均']
sum3 = 0
for i in range(len(score_finli[1]) - 3):
    avg2 = 0
    for j in score_finli[1:]:
        avg2 += int(j[i + 1])
    avg2 //= len(score_finli[1:])
    sum3 += avg2
    score_avgli.append(str(avg2))
avg3 = round(sum3 / 9, 1)
score_avgli.append(str(sum3))
score_avgli.append(str(avg3))
score_finli.insert(1, score_avgli)

# 添加名次，替换不及格（平均分不替换）
score_finli[0].insert(0, '名次')
ranking = 0
for i in score_finli[1:]:
    for j in range(1, 10):
        if float(i[j]) < 60:
            i[j] = '不及格'
    i.insert(0, str(ranking))
    ranking += 1

# 存为一个新文件(result.txt)
score_finli = [' '.join(i) + '\n' for i in score_finli]
with open('result.txt', 'w', encoding='utf-8') as f:
    f.writelines(score_finli)
