import time


with open('data.txt') as f:
    diagnostic = [line.rstrip() for line in f]


if __name__ == "__main__":
  replit_start_time = time.perf_counter()
  
  
  one = 0
  two = 0
  three = 0
  four = 0
  five = 0
  six = 0
  seven = 0
  eight = 0
  nine = 0
  ten = 0
  eleven = 0
  twelve = 0


for i in diagnostic:
  # print(i)
  
  if i[0] == '1':
    one += 1
for i in diagnostic:
  if int(i[1]) == 1:
    two += 1
for i in diagnostic:
  if i[2] == '1':
    three += 1
for i in diagnostic:
  if i[3] == '1':
    four += 1
for i in diagnostic:
  if i[4] == '1':
    five += 1
for i in diagnostic:
  if i[5] == '1':
    six += 1
for i in diagnostic:
  if i[6] == '1':
    seven += 1
for i in diagnostic:
  if i[7] == '1':
    eight += 1
for i in diagnostic:
  if i[8] == '1':
    nine += 1
for i in diagnostic:
  if i[9] == '1':
    ten += 1
for i in diagnostic:
  if i[10] == '1':
    eleven += 1
for i in diagnostic:
  if i[11] == '1':
    twelve += 1


  # i[0].append(one)
  # i[1].append(two)
  # i[2].append(three)
  # i[3].append(four)
  # i[4].append(five)
  # i[5].append(six)

gamma = []

if one > 500:
  gamma.append('1')
else:
  gamma.append('0')
if two > 500:
  gamma.append('1')
else:
  gamma.append('0')
if three > 500:
  gamma.append('1')
else:
  gamma.append('0')
if four > 500:
  gamma.append('1')
else:
  gamma.append('0')
if five > 500:
  gamma.append('1')
else:
  gamma.append('0')

if six > 500:
  gamma.append('1')
else:
  gamma.append('0')
if seven > 500:
  gamma.append('1')
else:
  gamma.append('0')
if eight > 500:
  gamma.append('1')
else:
  gamma.append('0')
if nine > 500:
  gamma.append('1')
else:
  gamma.append('0')
if ten > 500:
  gamma.append('1')
else:
  gamma.append('0')
if eleven > 500:
  gamma.append('1')
else:
  gamma.append('0')
if twelve > 500:
  gamma.append('1')
else:
  gamma.append('0')

print('Gamma', gamma)

gamma1 = ''.join(gamma)
print(gamma1)

gam = int(gamma1, 2)
print(gam)

# epsilon = gam.replace()
epsilon = []

if one > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if two > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if three > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if four > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if five > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if six > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if seven > 500:
  epsilon.append('0')
else:
  epsilon.append('1')

if eight > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if nine > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if ten > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if eleven > 500:
  epsilon.append('0')
else:
  epsilon.append('1')
if twelve > 500:
  epsilon.append('0')
else:
  epsilon.append('1')

epsilon1 = ''.join(epsilon)
print('Epsilon?', epsilon1)

eps = int(epsilon1, 2)
print(eps)

power = gam * eps
print(power)

ox1 = []
ox2 = []
ox3 = []
ox4 = []
ox5 = []
ox6 = []
ox7 = []
ox8 = []
ox9 = []
ox10 = []
ox11 = []
ox12 = []

for a in diagnostic:
  if a[0] == gamma[0]:
    ox1.append(a)
for a in ox1:
  if a[1] == gamma[1]:
    ox2.append(a)
for a in ox2:
  if a[2] == gamma[2]:
    ox3.append(a)
for a in ox3:
  if a[3] == gamma[3]:
    ox4.append(a)
for a in ox4:
  if a[4] == gamma[4]:
    ox5.append(a)
for a in ox5:
  if a[5] == gamma[5]:
    ox6.append(a)
for a in ox6:
  if a[6] == gamma[6]:
    ox7.append(a)
for a in ox7:
  if a[7] == gamma[7]:
    ox8.append(a)
for a in ox8:
  if a[8] == gamma[8]:
    ox9.append(a)
for a in ox9:
  if a[9] == gamma[9]:
    ox10.append(a)
for a in ox10:
  if a[10] == gamma[10]:
    ox11.append(a)
for a in ox11:
  if a[11] == gamma[11]:
    ox12.append(a)

oxyg = ''.join(ox12)
print(oxyg)

oxygen = int(oxyg, 2)
print(oxygen)

# now for co2

co1 = []
co2 = []
co3 = []
co4 = []
co5 = []
co6 = []
co7 = []
co8 = []
co9 = []
co10 = []
co11 = []

for a in diagnostic:
  if a[0] == epsilon1[0]:
    co1.append(a)
for a in co1:
  if a[1] == epsilon1[1]:
    co2.append(a)
for a in co2:
  if a[2] == epsilon1[2]:
    co3.append(a)
for a in co3:
  if a[3] == epsilon1[3]:
    co4.append(a)
for a in co4:
  if a[4] == epsilon1[4]:
    co5.append(a)
for a in co5:
  if a[5] == epsilon1[5]:
    co6.append(a)
for a in co6:
  if a[6] == epsilon1[6]:
    co7.append(a)
for a in co7:
  if a[7] == epsilon1[7]:
    co8.append(a)
for a in co8:
  if a[8] == epsilon1[8]:
    co9.append(a)
for a in co9:
  if a[9] == epsilon1[9]:
    co10.append(a)
for a in co10:
  if a[10] == epsilon1[10]:
    co11.append(a)
  # elif a[10] == 0:
  #   co11.append(a)

print(co10[0])
# co = ''.join(co11)
# print('what is this', co)
print('co10', co10)
cotwo = int(co10[0], 2)
cotwo1 = int('101101101001', 2)
print('co2', cotwo)
print(oxygen * cotwo)




 
  
replit_end_time = time.perf_counter()
print("Elapsed time:", replit_end_time - replit_start_time)