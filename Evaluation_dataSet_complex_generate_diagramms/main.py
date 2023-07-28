import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import math


def withoutOnes(item):
    for k, v in list(item.items()):
        if v <= 51:
            del item[k]


csv_data_anreu = 'path/to/csv'
ar = pd.read_csv(csv_data_anreu, encoding='utf-8', sep=',', header=None,
                 names=['Formula', '[MASK]-Token', 'Top 1 Token', 'Top 1 Probability', 'Top 2 Token',
                        'Top 2 Probability', 'Top 3 Token', 'Top 3 Probability', 'Token = Probability', 'Top k =',
                        'Token < Probability', 'Top k <', 'Token > Probability', 'Top k >', 'Position Hit'])

csv_data_bertbase = 'path/to/csv'
bb = pd.read_csv(csv_data_bertbase, encoding='utf-8', sep=',', header=None,
                 names=['Formula', '[MASK]-Token', 'Top 1 Token', 'Top 1 Probability', 'Top 2 Token',
                        'Top 2 Probability', 'Top 3 Token', 'Top 3 Probability', 'Token = Probability', 'Top k =',
                        'Token < Probability', 'Top k <', 'Token > Probability', 'Top k >', 'Position Hit'])

csv_data_mathbert = 'path/to/csv'
mb = pd.read_csv(csv_data_mathbert, encoding='utf-8', sep=',', header=None,
                 names=['Formula', '[MASK]-Token', 'Top 1 Token', 'Top 1 Probability', 'Top 2 Token',
                        'Top 2 Probability', 'Top 3 Token', 'Top 3 Probability', 'Token = Probability', 'Top k =',
                        'Token < Probability', 'Top k <', 'Token > Probability', 'Top k >', 'Position Hit'])

### die durchschnittliche WSK, dass BERT denkt das vorhergesagte Token ist korrekt ###
# Durschnitt für Model AnReu berechnen
sum_truthful_prob_gt = 0
count_gt = 0

sum_truthful_prob_lt = 0
count_lt = 0

sum_truthful_prob_eq = 0
count_eq = 0

for line in ar.values:
    if ">" in line[1]:
        sum_truthful_prob_gt += float(line[12]) * 100
        count_gt += 1
    if "<" in line[1]:
        sum_truthful_prob_lt += float(line[10]) * 100
        count_lt += 1
    if "=" in line[1]:
        sum_truthful_prob_eq += float(line[8]) * 100
        count_eq += 1

prob_truthful_gt = sum_truthful_prob_gt / count_gt
prob_truthful_lt = sum_truthful_prob_lt / count_lt
prob_truthful_eq = sum_truthful_prob_eq / count_eq

# Durschnitt für Model Bertbase berechnen
sum_truthful_prob_gt_bb = 0
count_gt_bb = 0

sum_truthful_prob_lt_bb = 0
count_lt_bb = 0

sum_truthful_prob_eq_bb = 0
count_eq_bb = 0

for line in bb.values:
    if ">" in line[1]:
        sum_truthful_prob_gt_bb += float(line[12]) * 100
        count_gt_bb += 1
    if "<" in line[1]:
        sum_truthful_prob_lt_bb += float(line[10]) * 100
        count_lt_bb += 1
    if "=" in line[1]:
        sum_truthful_prob_eq_bb += float(line[8]) * 100
        count_eq_bb += 1

prob_truthful_gt_bb = sum_truthful_prob_gt_bb / count_gt_bb
prob_truthful_lt_bb = sum_truthful_prob_lt_bb / count_lt_bb
prob_truthful_eq_bb = sum_truthful_prob_eq_bb / count_eq_bb

# Durchschnitt füt mathBERT berechnen
sum_truthful_prob_gt_mb = 0
count_gt_mb = 0

sum_truthful_prob_lt_mb = 0
count_lt_mb = 0

sum_truthful_prob_eq_mb = 0
count_eq_mb = 0

for line in mb.values:
    if ">" in line[1]:
        sum_truthful_prob_gt_mb += float(line[12]) * 100
        count_gt_mb += 1
    if "<" in line[1]:
        sum_truthful_prob_lt_mb += float(line[10]) * 100
        count_lt_mb += 1
    if "=" in line[1]:
        sum_truthful_prob_eq_mb += float(line[8]) * 100
        count_eq_mb += 1

prob_truthful_gt_mb = sum_truthful_prob_gt_mb / count_gt_mb
prob_truthful_lt_mb = sum_truthful_prob_lt_mb / count_lt_mb
prob_truthful_eq_mb = sum_truthful_prob_eq_mb / count_eq_mb

'''
plt.ylabel('Wahrscheinlichkeit in Prozent')
plt.xlabel('Vergleichsoperator')
plt.tight_layout()

print("> : " + str(prob_truthful_gt_mb))
print("< : " + str(prob_truthful_lt_mb))
print("= : " + str(prob_truthful_eq_mb))

#plt.bar([">", "<", "="], [prob_truthful_gt, prob_truthful_lt, prob_truthful_eq], color='#0b2a51')
#plt.bar([">", "<", "="], [prob_truthful_gt_bb, prob_truthful_lt_bb, prob_truthful_eq_bb], color='#a6cf00')
plt.bar([">", "<", "="], [prob_truthful_gt_mb, prob_truthful_lt_mb, prob_truthful_eq_mb], color='#009ca4')
'''

### durchschnitteliche WSK, welche Vergleichsoperatoren für jede Formelart vorhergesagt werden ###
# für AnReu Model
sum_gt_truthful_gt_predicted = 0
sum_gt_truthful_lt_predicted = 0
sum_gt_truthful_eq_predicted = 0

sum_lt_truthful_gt_predicted = 0
sum_lt_truthful_lt_predicted = 0
sum_lt_truthful_eq_predicted = 0

sum_eq_truthful_gt_predicted = 0
sum_eq_truthful_lt_predicted = 0
sum_eq_truthful_eq_predicted = 0

for line in ar.values:
    if ">" in line[1]:
        sum_gt_truthful_gt_predicted += float(line[12]) * 100
        sum_gt_truthful_lt_predicted += float(line[10]) * 100
        sum_gt_truthful_eq_predicted += float(line[8]) * 100
    if "<" in line[1]:
        sum_lt_truthful_gt_predicted += float(line[12]) * 100
        sum_lt_truthful_lt_predicted += float(line[10]) * 100
        sum_lt_truthful_eq_predicted += float(line[8]) * 100
    if "=" in line[1]:
        sum_eq_truthful_gt_predicted += float(line[12]) * 100
        sum_eq_truthful_lt_predicted += float(line[10]) * 100
        sum_eq_truthful_eq_predicted += float(line[8]) * 100

prob_gt_truthful_gt_predicted = sum_gt_truthful_gt_predicted / count_gt
prob_gt_truthful_lt_predicted = sum_gt_truthful_lt_predicted / count_gt
prob_gt_truthful_eq_predicted = sum_gt_truthful_eq_predicted / count_gt

prob_lt_truthful_gt_predicted = sum_lt_truthful_gt_predicted / count_lt
prob_lt_truthful_lt_predicted = sum_lt_truthful_lt_predicted / count_lt
prob_lt_truthful_eq_predicted = sum_lt_truthful_eq_predicted / count_lt

prob_eq_truthful_gt_predicted = sum_eq_truthful_gt_predicted / count_eq
prob_eq_truthful_lt_predicted = sum_eq_truthful_lt_predicted / count_eq
prob_eq_truthful_eq_predicted = sum_eq_truthful_eq_predicted / count_eq

'''
plt.bar(["Mask >,\nPredicted >", "Mask >,\nPredicted <", "Mask >,\nPredicted =",
         "Mask <,\nPredicted >", "Mask <,\nPredicted <", "Mask <,\nPredicted =",
         "Mask =,\nPredicted >", "Mask =,\nPredicted <", "Mask =,\nPredicted ="],
        [prob_gt_truthful_gt_predicted, prob_gt_truthful_lt_predicted, prob_gt_truthful_eq_predicted,
         prob_lt_truthful_gt_predicted, prob_lt_truthful_lt_predicted, prob_lt_truthful_eq_predicted,
         prob_eq_truthful_gt_predicted, prob_eq_truthful_lt_predicted, prob_eq_truthful_eq_predicted],
        color='#0b2a51')

print("Mask >, Predicted > : " + str(prob_gt_truthful_gt_predicted))
print("Mask >, Predicted < : " + str(prob_gt_truthful_lt_predicted))
print("Mask >, Predicted = : " + str(prob_gt_truthful_eq_predicted))

print("Mask <, Predicted > : " + str(prob_lt_truthful_gt_predicted))
print("Mask <, Predicted < : " + str(prob_lt_truthful_lt_predicted))
print("Mask <, Predicted = : " + str(prob_lt_truthful_eq_predicted))

print("Mask =, Predicted > : " + str(prob_eq_truthful_gt_predicted))
print("Mask =, Predicted < : " + str(prob_eq_truthful_lt_predicted))
print("Mask =, Predicted = : " + str(prob_eq_truthful_eq_predicted))
'''
# für Bertbase
sum_gt_truthful_gt_predicted_bb = 0
sum_gt_truthful_lt_predicted_bb = 0
sum_gt_truthful_eq_predicted_bb = 0

sum_lt_truthful_gt_predicted_bb = 0
sum_lt_truthful_lt_predicted_bb = 0
sum_lt_truthful_eq_predicted_bb = 0

sum_eq_truthful_gt_predicted_bb = 0
sum_eq_truthful_lt_predicted_bb = 0
sum_eq_truthful_eq_predicted_bb = 0

for line in bb.values:
    if ">" in line[1]:
        sum_gt_truthful_gt_predicted_bb += float(line[12]) * 100
        sum_gt_truthful_lt_predicted_bb += float(line[10]) * 100
        sum_gt_truthful_eq_predicted_bb += float(line[8]) * 100
    if "<" in line[1]:
        sum_lt_truthful_gt_predicted_bb += float(line[12]) * 100
        sum_lt_truthful_lt_predicted_bb += float(line[10]) * 100
        sum_lt_truthful_eq_predicted_bb += float(line[8]) * 100
    if "=" in line[1]:
        sum_eq_truthful_gt_predicted_bb += float(line[12]) * 100
        sum_eq_truthful_lt_predicted_bb += float(line[10]) * 100
        sum_eq_truthful_eq_predicted_bb += float(line[8]) * 100

prob_gt_truthful_gt_predicted_bb = sum_gt_truthful_gt_predicted_bb / count_gt_bb
prob_gt_truthful_lt_predicted_bb = sum_gt_truthful_lt_predicted_bb / count_gt_bb
prob_gt_truthful_eq_predicted_bb = sum_gt_truthful_eq_predicted_bb / count_gt_bb

prob_lt_truthful_gt_predicted_bb = sum_lt_truthful_gt_predicted_bb / count_lt_bb
prob_lt_truthful_lt_predicted_bb = sum_lt_truthful_lt_predicted_bb / count_lt_bb
prob_lt_truthful_eq_predicted_bb = sum_lt_truthful_eq_predicted_bb / count_lt_bb

prob_eq_truthful_gt_predicted_bb = sum_eq_truthful_gt_predicted_bb / count_eq_bb
prob_eq_truthful_lt_predicted_bb = sum_eq_truthful_lt_predicted_bb / count_eq_bb
prob_eq_truthful_eq_predicted_bb = sum_eq_truthful_eq_predicted_bb / count_eq_bb
'''
plt.bar(["Mask >,\nPredicted >", "Mask >,\nPredicted <", "Mask >,\nPredicted =",
         "Mask <,\nPredicted >", "Mask <,\nPredicted <", "Mask <,\nPredicted =",
         "Mask =,\nPredicted >", "Mask =,\nPredicted <", "Mask =,\nPredicted ="],
        [prob_gt_truthful_gt_predicted_bb, prob_gt_truthful_lt_predicted_bb, prob_gt_truthful_eq_predicted_bb,
         prob_lt_truthful_gt_predicted_bb, prob_lt_truthful_lt_predicted_bb, prob_lt_truthful_eq_predicted_bb,
         prob_eq_truthful_gt_predicted_bb, prob_eq_truthful_lt_predicted_bb, prob_eq_truthful_eq_predicted_bb],
        color='#a6cf00')

print("Mask >, Predicted > : " + str(prob_gt_truthful_gt_predicted_bb))
print("Mask >, Predicted < : " + str(prob_gt_truthful_lt_predicted_bb))
print("Mask >, Predicted = : " + str(prob_gt_truthful_eq_predicted_bb))

print("Mask <, Predicted > : " + str(prob_lt_truthful_gt_predicted_bb))
print("Mask <, Predicted < : " + str(prob_lt_truthful_lt_predicted_bb))
print("Mask <, Predicted = : " + str(prob_lt_truthful_eq_predicted_bb))

print("Mask =, Predicted > : " + str(prob_eq_truthful_gt_predicted_bb))
print("Mask =, Predicted < : " + str(prob_eq_truthful_lt_predicted_bb))
print("Mask =, Predicted = : " + str(prob_eq_truthful_eq_predicted_bb))
'''
# für Mathbert
sum_gt_truthful_gt_predicted_mb = 0
sum_gt_truthful_lt_predicted_mb = 0
sum_gt_truthful_eq_predicted_mb = 0

sum_lt_truthful_gt_predicted_mb = 0
sum_lt_truthful_lt_predicted_mb = 0
sum_lt_truthful_eq_predicted_mb = 0

sum_eq_truthful_gt_predicted_mb = 0
sum_eq_truthful_lt_predicted_mb = 0
sum_eq_truthful_eq_predicted_mb = 0

for line in mb.values:
    if ">" in line[1]:
        sum_gt_truthful_gt_predicted_mb += float(line[12]) * 100
        sum_gt_truthful_lt_predicted_mb += float(line[10]) * 100
        sum_gt_truthful_eq_predicted_mb += float(line[8]) * 100
    if "<" in line[1]:
        sum_lt_truthful_gt_predicted_mb += float(line[12]) * 100
        sum_lt_truthful_lt_predicted_mb += float(line[10]) * 100
        sum_lt_truthful_eq_predicted_mb += float(line[8]) * 100
    if "=" in line[1]:
        sum_eq_truthful_gt_predicted_mb += float(line[12]) * 100
        sum_eq_truthful_lt_predicted_mb += float(line[10]) * 100
        sum_eq_truthful_eq_predicted_mb += float(line[8]) * 100

prob_gt_truthful_gt_predicted_mb = sum_gt_truthful_gt_predicted_mb / count_gt_mb
prob_gt_truthful_lt_predicted_mb = sum_gt_truthful_lt_predicted_mb / count_gt_mb
prob_gt_truthful_eq_predicted_mb = sum_gt_truthful_eq_predicted_mb / count_gt_mb

prob_lt_truthful_gt_predicted_mb = sum_lt_truthful_gt_predicted_mb / count_lt_mb
prob_lt_truthful_lt_predicted_mb = sum_lt_truthful_lt_predicted_mb / count_lt_mb
prob_lt_truthful_eq_predicted_mb = sum_lt_truthful_eq_predicted_mb / count_lt_mb

prob_eq_truthful_gt_predicted_mb = sum_eq_truthful_gt_predicted_mb / count_eq_mb
prob_eq_truthful_lt_predicted_mb = sum_eq_truthful_lt_predicted_mb / count_eq_mb
prob_eq_truthful_eq_predicted_mb = sum_eq_truthful_eq_predicted_mb / count_eq_mb

'''
plt.bar(["Mask >,\nPredicted >", "Mask >,\nPredicted <", "Mask >,\nPredicted =",
         "Mask <,\nPredicted >", "Mask <,\nPredicted <", "Mask <,\nPredicted =",
         "Mask =,\nPredicted >", "Mask =,\nPredicted <", "Mask =,\nPredicted ="],
        [prob_gt_truthful_gt_predicted_mb, prob_gt_truthful_lt_predicted_mb, prob_gt_truthful_eq_predicted_mb,
         prob_lt_truthful_gt_predicted_mb, prob_lt_truthful_lt_predicted_mb, prob_lt_truthful_eq_predicted_mb,
         prob_eq_truthful_gt_predicted_mb, prob_eq_truthful_lt_predicted_mb, prob_eq_truthful_eq_predicted_mb],
        color='#009ca4')


plt.ylabel('Wahrscheinlichkeit in Prozent')
plt.xlabel('erwartete, vorhergesagte Vergleichsoperatoren')
plt.tight_layout()

print("Mask >, Predicted > : " + str(prob_gt_truthful_gt_predicted_mb))
print("Mask >, Predicted < : " + str(prob_gt_truthful_lt_predicted_mb))
print("Mask >, Predicted = : " + str(prob_gt_truthful_eq_predicted_mb))

print("Mask <, Predicted > : " + str(prob_lt_truthful_gt_predicted_mb))
print("Mask <, Predicted < : " + str(prob_lt_truthful_lt_predicted_mb))
print("Mask <, Predicted = : " + str(prob_lt_truthful_eq_predicted_mb))

print("Mask =, Predicted > : " + str(prob_eq_truthful_gt_predicted_mb))
print("Mask =, Predicted < : " + str(prob_eq_truthful_lt_predicted_mb))
print("Mask =, Predicted = : " + str(prob_eq_truthful_eq_predicted_mb))
'''

def withoutOnes(item):
    for k, v in list(item.items()):
        if  v<60:
            del item[k]

# Top 1 vorhergesagte Token für gt, lt,eq
# Top 1 Token Model AnReu
top_1_predictions_gt = {}
top_1_predictions_lt = {}
top_1_predictions_eq = {}

for line in ar.values:
    if ">" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_gt):
            value = float(top_1_predictions_gt.get(tk)) + 1
        top_1_predictions_gt.update({tk: value})
    if "<" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_lt):
            value = int(top_1_predictions_lt.get(tk)) + 1
        top_1_predictions_lt.update({tk: value})
    if "=" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_eq):
            value = int(top_1_predictions_eq.get(tk)) + 1
        top_1_predictions_eq.update({tk: value})

sorted_top_1_predictions_gt = dict(sorted(top_1_predictions_gt.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_gt)
sorted_top_1_predictions_lt = dict(sorted(top_1_predictions_lt.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_lt)
sorted_top_1_predictions_eq = dict(sorted(top_1_predictions_eq.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_eq)

#plt.bar(sorted_top_1_predictions_gt.keys(), sorted_top_1_predictions_gt.values(), color='#0b2a51')
#plt.bar(sorted_top_1_predictions_lt.keys(),sorted_top_1_predictions_lt.values(), color='#0b2a51')
#plt.bar(sorted_top_1_predictions_eq.keys(),sorted_top_1_predictions_eq.values(), color='#0b2a51')
'''
plt.xticks(rotation=90)
plt.ylabel('Anzahl der vorhergesagten Token')
plt.xlabel('vorhergesagte Token')
plt.tight_layout()
'''
# Top 1 vorhergesagte Token für gt, lt,eq
# Top 1 Token Model BB
top_1_predictions_gt_bb = {}
top_1_predictions_lt_bb = {}
top_1_predictions_eq_bb = {}

for line in bb.values:
    if ">" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_gt_bb):
            value = float(top_1_predictions_gt_bb.get(tk)) + 1
        top_1_predictions_gt_bb.update({tk: value})
    if "<" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_lt_bb):
            value = int(top_1_predictions_lt_bb.get(tk)) + 1
        top_1_predictions_lt_bb.update({tk: value})
    if "=" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_eq_bb):
            value = int(top_1_predictions_eq_bb.get(tk)) + 1
        top_1_predictions_eq_bb.update({tk: value})

sorted_top_1_predictions_gt_bb = dict(sorted(top_1_predictions_gt_bb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_gt_bb)
sorted_top_1_predictions_lt_bb = dict(sorted(top_1_predictions_lt_bb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_lt_bb)
sorted_top_1_predictions_eq_bb = dict(sorted(top_1_predictions_eq_bb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_eq_bb)

#plt.bar(sorted_top_1_predictions_gt_bb.keys(), sorted_top_1_predictions_gt_bb.values(), color='#a6cf00')
#plt.bar(sorted_top_1_predictions_lt_bb.keys(),sorted_top_1_predictions_lt_bb.values(), color='#a6cf00')
#plt.bar(sorted_top_1_predictions_eq_bb.keys(),sorted_top_1_predictions_eq_bb.values(), color='#a6cf00')

#print(sorted_top_1_predictions_eq_bb)

# Top 1 vorhergesagte Token für gt, lt,eq
# Top 1 Token Model MB
top_1_predictions_gt_mb = {}
top_1_predictions_lt_mb = {}
top_1_predictions_eq_mb = {}

for line in mb.values:
    if ">" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_gt_mb):
            value = float(top_1_predictions_gt_mb.get(tk)) + 1
        top_1_predictions_gt_mb.update({tk: value})
    if "<" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_lt_mb):
            value = int(top_1_predictions_lt_mb.get(tk)) + 1
        top_1_predictions_lt_mb.update({tk: value})
    if "=" in line[1]:
        tk = line[2]
        value = 1
        if (tk in top_1_predictions_eq_mb):
            value = int(top_1_predictions_eq_mb.get(tk)) + 1
        top_1_predictions_eq_mb.update({tk: value})

sorted_top_1_predictions_gt_mb = dict(sorted(top_1_predictions_gt_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_gt_mb)
sorted_top_1_predictions_lt_mb = dict(sorted(top_1_predictions_lt_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_lt_mb)
sorted_top_1_predictions_eq_mb = dict(sorted(top_1_predictions_eq_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_eq_mb)

#plt.bar(sorted_top_1_predictions_gt_mb.keys(), sorted_top_1_predictions_gt_mb.values(), color='#009ca4')
#plt.bar(sorted_top_1_predictions_lt_mb.keys(),sorted_top_1_predictions_lt_mb.values(), color='#009ca4')
#plt.bar(sorted_top_1_predictions_eq_mb.keys(),sorted_top_1_predictions_eq_mb.values(), color='#009ca4')

#print(sorted_top_1_predictions_eq_mb)


# Durchschnittliche Wahrscheinlichkeit der Vorhergesage, LaTeX-Ausdruck "boxed “
# AR
equationType = "\\boxed"
#equationType = "\\frac"
#equationType = "\\sqrt"
#equationType = "\\mod"
sum_truthful_prob_gt = 0
count_gt = 0

sum_truthful_prob_lt = 0
count_lt = 0

sum_truthful_prob_eq = 0
count_eq = 0

for line in ar.values:
    if equationType not in line[0]:
        continue
    if ">" in line[1]:
        sum_truthful_prob_gt += float(line[12]) * 100
        count_gt += 1
    if "<" in line[1]:
        sum_truthful_prob_lt += float(line[10]) * 100
        count_lt += 1
    if "=" in line[1]:
        sum_truthful_prob_eq += float(line[8]) * 100
        count_eq += 1
prob_truthful_gt = sum_truthful_prob_gt / count_gt
prob_truthful_lt = sum_truthful_prob_lt / count_lt
prob_truthful_eq = sum_truthful_prob_eq / count_eq

##BB
sum_truthful_prob_gt_bb = 0
count_gt_bb = 0

sum_truthful_prob_lt_bb = 0
count_lt = 0

sum_truthful_prob_eq_bb = 0
count_eq_bb = 0

for line in bb.values:
    if equationType not in line[0]:
        continue
    if ">" in line[1]:
        sum_truthful_prob_gt_bb += float(line[12]) * 100
        count_gt_bb += 1
    if "<" in line[1]:
        sum_truthful_prob_lt_bb += float(line[10]) * 100
        count_lt += 1
    if "=" in line[1]:
        sum_truthful_prob_eq_bb += float(line[8]) * 100
        count_eq_bb += 1

prob_truthful_gt_bb = sum_truthful_prob_gt_bb / count_gt_bb
prob_truthful_lt_bb = sum_truthful_prob_lt_bb / count_lt_bb
prob_truthful_eq_bb = sum_truthful_prob_eq_bb / count_eq_bb

##MB
sum_truthful_prob_gt_mb = 0
count_gt_mb = 0

sum_truthful_prob_lt_mb = 0
count_lt_mb = 0

sum_truthful_prob_eq_mb = 0
count_eq_mb = 0

for line in mb.values:
    if equationType not in line[0]:
        continue
    if ">" in line[1]:
        sum_truthful_prob_gt_mb += float(line[12]) * 100
        count_gt_mb += 1
    if "<" in line[1]:
        sum_truthful_prob_lt_mb += float(line[10]) * 100
        count_lt_mb += 1
    if "=" in line[1]:
        sum_truthful_prob_eq_mb += float(line[8]) * 100
        count_eq_mb += 1

prob_truthful_gt_mb = sum_truthful_prob_gt_mb / count_gt_mb
prob_truthful_lt_mb = sum_truthful_prob_lt_mb / count_lt_mb
prob_truthful_eq_mb = sum_truthful_prob_eq_mb / count_eq_mb

plt.ylabel('Wahrscheinlichkeit in Prozent')
plt.xlabel('Vergleichsoperator, LaTeX-Ausdruck '+equationType)
plt.tight_layout()
#plt.bar([">", "<", "="], [prob_truthful_gt, prob_truthful_lt, prob_truthful_eq], color='#0b2a51')
#plt.bar([">", "<", "="], [prob_truthful_gt_bb, prob_truthful_lt_bb, prob_truthful_eq_bb], color='#a6cf00')
plt.bar([">", "<", "="], [prob_truthful_gt_mb, prob_truthful_lt_mb, prob_truthful_eq_mb], color='#009ca4')

print(prob_truthful_gt_mb)
print(prob_truthful_lt_mb)
print(prob_truthful_eq_mb)

#WSK wenn kein Latex-Ausdruck enthalten ist
sum_truthful_prob_gt = 0
count_gt = 0

sum_truthful_prob_lt = 0
count_lt = 0

sum_truthful_prob_eq = 0
count_eq = 0

for line in ar.values:
    if "\\" in line[0]:
        continue
    if ">" in line[1]:
        sum_truthful_prob_gt += float(line[12]) * 100
        count_gt += 1
    if "<" in line[1]:
        sum_truthful_prob_lt += float(line[10]) * 100
        count_lt += 1
    if "=" in line[1]:
        sum_truthful_prob_eq += float(line[8]) * 100
        count_eq += 1
prob_truthful_gt = sum_truthful_prob_gt / count_gt
prob_truthful_lt = sum_truthful_prob_lt / count_lt
prob_truthful_eq = sum_truthful_prob_eq / count_eq

#WSK wenn kein Latex-Ausdruck enthalten ist MB
sum_truthful_prob_gt_bb = 0
count_gt_bb = 0

sum_truthful_prob_lt_bb = 0
count_lt_bb = 0

sum_truthful_prob_eq_bb = 0
count_eq_bb = 0

for line in bb.values:
    if "\\" in line[0]:
        continue
    if ">" in line[1]:
        sum_truthful_prob_gt_bb += float(line[12]) * 100
        count_gt_bb += 1
    if "<" in line[1]:
        sum_truthful_prob_lt_bb += float(line[10]) * 100
        count_lt_bb += 1
    if "=" in line[1]:
        sum_truthful_prob_eq_bb += float(line[8]) * 100
        count_eq_bb += 1
prob_truthful_gt_bb = sum_truthful_prob_gt_bb / count_gt_bb
prob_truthful_lt_bb = sum_truthful_prob_lt_bb / count_lt_bb
prob_truthful_eq_bb = sum_truthful_prob_eq_bb / count_eq_bb

#plt.ylabel('Wahrscheinlichkeit in Prozent')
#plt.xlabel('Vergleichsoperator, kein LaTeX-Ausdruck in Formel enthalten')
#plt.tight_layout()
#plt.bar([">", "<", "="], [prob_truthful_gt, prob_truthful_lt, prob_truthful_eq], color='#0b2a51')
#plt.bar([">", "<", "="], [prob_truthful_gt_bb, prob_truthful_lt_bb, prob_truthful_eq_bb], color='#a6cf00')
#plt.bar([">", "<", "="], [prob_truthful_gt_mb, prob_truthful_lt_mb, prob_truthful_eq_mb], color='#009ca4')

print(prob_truthful_gt_bb)
print(prob_truthful_lt_bb)
print(prob_truthful_eq_bb)


# CM Matrix für erwartete und vorhergesagte Token
# BB
'''
conf_matrix = np.array([[0.2673, 0.5108, 0.3998],
                        [0.4621, 0.5462, 0.5680],
                        [3.9669, 7.7809, 5.8850]])

#AR
conf_matrix = np.array([[0.7499, 0.6600, 0.6601],
                        [0.5712, 0.4420, 0.4313],
                        [66.9390, 54.7085, 58.3998]])
'''
'''
#MB
conf_matrix = np.array([[0.3055, 0.3453, 0.3278],
                        [1.0978, 0.3409, 0.5925],
                        [10.2462, 8.3192, 12.2814]])

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center')

plt.yticks(range(3), [">", "<", "="])
#plt.yticks(range(3), ["0", "1", "2"])
#plt.yticks(range(5), ["0", "1", "2", "3", "4"])

plt.xticks(range(3), [">", "<", "="])

plt.xlabel('Predicted')
plt.ylabel('Actual')
'''
plt.show()
