import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

from mlxtend.plotting import plot_confusion_matrix


def withoutOnes(item):
    for k, v in list(item.items()):
        if  v<14:
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
#Durschnitt für Model AnReu berechnen
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

#Durschnitt für Model Bertbase berechnen
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

#Durchschnitt füt mathBERT berechnen
sum_truthful_prob_gt_mb = 0
count_gt_mb = 0

sum_truthful_prob_lt_mb = 0
count_lt_mb = 0

sum_truthful_prob_eq_mb = 0
count_eq_mb = 0

for line in mb.values:
    if ">" in line[1]:
        sum_truthful_prob_gt_mb += float(line[12]) *100
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

#plt.ylabel('Wahrscheinlichkeit in Prozent')
#plt.xlabel('Vergleichsoperator')

#plt.bar([">", "<", "="], [prob_truthful_gt, prob_truthful_lt, prob_truthful_eq], color='#0b2a51')
#plt.bar([">", "<", "="], [prob_truthful_gt_bb, prob_truthful_lt_bb, prob_truthful_eq_bb], color='#a6cf00')
#plt.bar([">", "<", "="], [prob_truthful_gt_mb, prob_truthful_lt_mb, prob_truthful_eq_mb], color='#009ca4')
#plt.tight_layout()


### durchschnitteliche WSK, welche Vergleichsoperatoren für jede Formelart vorhergesagt werden ###
#für AnReu Model
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

''''
plt.bar(["Mask >,\nPredicted >", "Mask >,\nPredicted <", "Mask >,\nPredicted =",
         "Mask <,\nPredicted >", "Mask <,\nPredicted <", "Mask <,\nPredicted =",
         "Mask =,\nPredicted >", "Mask =,\nPredicted <", "Mask =,\nPredicted ="],
        [prob_gt_truthful_gt_predicted, prob_gt_truthful_lt_predicted, prob_gt_truthful_eq_predicted,
         prob_lt_truthful_gt_predicted, prob_lt_truthful_lt_predicted, prob_lt_truthful_eq_predicted,
         prob_eq_truthful_gt_predicted, prob_eq_truthful_lt_predicted, prob_eq_truthful_eq_predicted],
        color='#0b2a51')
'''
#für Bertbase
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
''''
plt.bar(["Mask >,\nPredicted >", "Mask >,\nPredicted <", "Mask >,\nPredicted =",
         "Mask <,\nPredicted >", "Mask <,\nPredicted <", "Mask <,\nPredicted =",
         "Mask =,\nPredicted >", "Mask =,\nPredicted <", "Mask =,\nPredicted ="],
        [prob_gt_truthful_gt_predicted_bb, prob_gt_truthful_lt_predicted_bb, prob_gt_truthful_eq_predicted_bb,
         prob_lt_truthful_gt_predicted_bb, prob_lt_truthful_lt_predicted_bb, prob_lt_truthful_eq_predicted_bb,
         prob_eq_truthful_gt_predicted_bb, prob_eq_truthful_lt_predicted_bb, prob_eq_truthful_eq_predicted_bb],
        color='#a6cf00')
'''
#für Mathbert
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
print("Mask <,Predicted < : " + str(prob_lt_truthful_lt_predicted_mb))
print("Mask <, Predicted = : " + str(prob_lt_truthful_eq_predicted_mb))

print("Mask =, Predicted > : " + str(prob_eq_truthful_gt_predicted_mb))
print("Mask =, Predicted < : " + str(prob_eq_truthful_lt_predicted_mb))
print("Mask =, Predicted = : " + str(prob_eq_truthful_eq_predicted_mb))
'''
### Vorkommen der Top 1 vorhergesagten Token, wenn das MASK-Token <,>,= ist ###
#Top 1 Token Model AnReu
top_1_predictions_gt = {}
top_1_predictions_lt = {}
top_1_predictions_eq = {}

for line in ar.values:
    if ">" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_gt):
            value = float(top_1_predictions_gt.get(tk)) + 1
        top_1_predictions_gt.update({tk: value})
    if "<" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_lt):
            value = int(top_1_predictions_lt.get(tk)) + 1
        top_1_predictions_lt.update({tk: value})
    if "=" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_eq):
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

#print(sorted_top_1_predictions_eq.values())

#Top 1 Token Model Bertbase
top_1_predictions_gt_bb = {}
top_1_predictions_lt_bb = {}
top_1_predictions_eq_bb = {}

for line in bb.values:
    if ">" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_gt_bb):
            value = float(top_1_predictions_gt_bb.get(tk)) + 1
        top_1_predictions_gt_bb.update({tk: value})
    if "<" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_lt_bb):
            value = int(top_1_predictions_lt_bb.get(tk)) + 1
        top_1_predictions_lt_bb.update({tk: value})
    if "=" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_eq_bb):
            value = int(top_1_predictions_eq_bb.get(tk)) + 1
        top_1_predictions_eq_bb.update({tk: value})

sorted_top_1_predictions_gt_bb = dict(sorted(top_1_predictions_gt_bb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_gt_bb)
sorted_top_1_predictions_lt_bb = dict(sorted(top_1_predictions_lt_bb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_lt_bb)
sorted_top_1_predictions_eq_bb = dict(sorted(top_1_predictions_eq_bb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_eq_bb)

plt.xticks(rotation=90)
plt.ylabel('Anzahl der vorhergesagten Token')
plt.xlabel('vorhergesagte Token')
plt.tight_layout()

plt.bar(sorted_top_1_predictions_gt_bb.keys(), sorted_top_1_predictions_gt_bb.values(), color='#a6cf00')
#plt.bar(sorted_top_1_predictions_lt_bb.keys(),sorted_top_1_predictions_lt_bb.values(), color='#a6cf00')
#plt.bar(sorted_top_1_predictions_eq_bb.keys(),sorted_top_1_predictions_eq_bb.values(), color='#a6cf00')

#print(sorted_top_1_predictions_eq_bb.values())

#Top 1 Token Model mathBert
top_1_predictions_gt_mb = {}
top_1_predictions_lt_mb = {}
top_1_predictions_eq_mb = {}

for line in mb.values:
    if ">" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_gt_mb):
            value = int(top_1_predictions_gt_mb.get(tk)) + 1
        top_1_predictions_gt_mb.update({tk: value})
    if "<" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_lt_mb):
            value = int(top_1_predictions_lt_mb.get(tk)) + 1
        top_1_predictions_lt_mb.update({tk: value})
    if "=" in line[1]:
        tk = line[2]
        value = 1
        if(tk in top_1_predictions_eq_mb):
            value = int(top_1_predictions_eq_mb.get(tk)) + 1
        top_1_predictions_eq_mb.update({tk: value})

'''
plt.xticks(rotation=90)
plt.ylabel('Wahrscheinlichkeit der vorhergesagten Token')
plt.xlabel('vorhergesagte Token')
plt.tight_layout()
'''
sorted_top_1_predictions_gt_mb = dict(sorted(top_1_predictions_gt_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_gt_mb)
sorted_top_1_predictions_lt_mb = dict(sorted(top_1_predictions_lt_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_lt_mb)
sorted_top_1_predictions_eq_mb = dict(sorted(top_1_predictions_eq_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_eq_mb)

#plt.bar(sorted_top_1_predictions_gt_mb.keys(), sorted_top_1_predictions_gt_mb.values(), color='#009ca4')
#plt.bar(sorted_top_1_predictions_lt_mb.keys(),sorted_top_1_predictions_lt_mb.values(), color='#009ca4')
#plt.bar(sorted_top_1_predictions_eq_mb.keys(),sorted_top_1_predictions_eq_mb.values(), color='#009ca4')

#print(sorted_top_1_predictions_eq.values())

#zeigt die WSK bei 0,1,2 negative Zahlen, die richtigen Token vorhergesagt werden
# negative Zahlen Model AnReu
sum_0_neg_gt_prob = 0
sum_0_neg_lt_prob = 0
sum_0_neg_eq_prob = 0

sum_1_neg_gt_prob = 0
sum_1_neg_lt_prob = 0
sum_1_neg_eq_prob = 0

sum_2_neg_gt_prob = 0
sum_2_neg_lt_prob = 0
sum_2_neg_eq_prob = 0

count_0_neg_gt_prob = 0
count_0_neg_lt_prob = 0
count_0_neg_eq_prob = 0

count_1_neg_gt_prob = 0
count_1_neg_lt_prob = 0
count_1_neg_eq_prob = 0

count_2_neg_gt_prob = 0
count_2_neg_lt_prob = 0
count_2_neg_eq_prob = 0

for line in ar.values:
    if ">" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_gt_prob += float(line[12]) * 100
            count_0_neg_gt_prob +=1
        if(line[0].count("-") == 1):
            sum_1_neg_gt_prob += float(line[12]) * 100
            count_1_neg_gt_prob +=1
        if(line[0].count("-") == 2):
            sum_2_neg_gt_prob += float(line[12]) * 100
            count_2_neg_gt_prob +=1
    if "<" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_lt_prob += float(line[10]) * 100
            count_0_neg_lt_prob +=1
        if(line[0].count("-") == 1):
            sum_1_neg_lt_prob += float(line[10]) * 100
            count_1_neg_lt_prob +=1
        if(line[0].count("-") == 2):
            sum_2_neg_lt_prob += float(line[10]) * 100
            count_2_neg_lt_prob+=1
    if "=" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_eq_prob += float(line[8]) * 100
            count_0_neg_eq_prob +=1
        if(line[0].count("-") == 1):
            sum_1_neg_eq_prob += float(line[8]) * 100
            count_1_neg_eq_prob +=1
        if(line[0].count("-") == 2):
            sum_2_neg_eq_prob += float(line[8]) * 100
            count_2_neg_eq_prob+=1

prob_0_neg_gt = sum_0_neg_gt_prob / count_0_neg_gt_prob
prob_1_neg_gt = sum_1_neg_gt_prob / count_1_neg_gt_prob
prob_2_neg_gt = sum_2_neg_gt_prob / count_2_neg_gt_prob

prob_0_neg_lt = sum_0_neg_lt_prob / count_0_neg_lt_prob
prob_1_neg_lt = sum_1_neg_lt_prob / count_1_neg_lt_prob
prob_2_neg_lt = sum_2_neg_lt_prob / count_2_neg_lt_prob

prob_0_neg_eq = sum_0_neg_eq_prob / count_0_neg_eq_prob
prob_2_neg_eq = sum_2_neg_eq_prob / count_2_neg_eq_prob
''''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ"],
        [prob_0_neg_gt, prob_1_neg_gt, prob_2_neg_gt,
        prob_0_neg_lt, prob_1_neg_lt, prob_2_neg_lt,
        prob_0_neg_eq, prob_2_neg_eq],
        color='#0b2a51')
'''
# negative Zahlen Model Bertbase
sum_0_neg_gt_prob_bb = 0
sum_0_neg_lt_prob_bb = 0
sum_0_neg_eq_prob_bb = 0

sum_1_neg_gt_prob_bb = 0
sum_1_neg_lt_prob_bb = 0
sum_1_neg_eq_prob_bb = 0

sum_2_neg_gt_prob_bb = 0
sum_2_neg_lt_prob_bb = 0
sum_2_neg_eq_prob_bb = 0

count_0_neg_gt_prob_bb = 0
count_0_neg_lt_prob_bb = 0
count_0_neg_eq_prob_bb = 0

count_1_neg_gt_prob_bb = 0
count_1_neg_lt_prob_bb = 0
count_1_neg_eq_prob_bb = 0

count_2_neg_gt_prob_bb = 0
count_2_neg_lt_prob_bb = 0
count_2_neg_eq_prob_bb = 0

for line in bb.values:
    if ">" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_gt_prob_bb += float(line[12]) * 100
            count_0_neg_gt_prob_bb +=1
        if(line[0].count("-") == 1):
            sum_1_neg_gt_prob_bb += float(line[12]) * 100
            count_1_neg_gt_prob_bb +=1
        if(line[0].count("-") == 2):
            sum_2_neg_gt_prob_bb += float(line[12]) * 100
            count_2_neg_gt_prob_bb +=1
    if "<" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_lt_prob_bb += float(line[10]) * 100
            count_0_neg_lt_prob_bb +=1
        if(line[0].count("-") == 1):
            sum_1_neg_lt_prob_bb += float(line[10]) * 100
            count_1_neg_lt_prob_bb +=1
        if(line[0].count("-") == 2):
            sum_2_neg_lt_prob_bb += float(line[10]) * 100
            count_2_neg_lt_prob_bb +=1
    if "=" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_eq_prob_bb += float(line[8]) * 100
            count_0_neg_eq_prob_bb +=1
        if(line[0].count("-") == 1):
            sum_1_neg_eq_prob_bb += float(line[8]) * 100
            count_1_neg_eq_prob_bb +=1
        if(line[0].count("-") == 2):
            sum_2_neg_eq_prob_bb += float(line[8]) * 100
            count_2_neg_eq_prob_bb +=1

prob_0_neg_gt_bb = sum_0_neg_gt_prob_bb / count_0_neg_gt_prob_bb
prob_1_neg_gt_bb = sum_1_neg_gt_prob_bb / count_1_neg_gt_prob_bb
prob_2_neg_gt_bb = sum_2_neg_gt_prob_bb / count_2_neg_gt_prob_bb

prob_0_neg_lt_bb = sum_0_neg_lt_prob_bb / count_0_neg_lt_prob_bb
prob_1_neg_lt_bb = sum_1_neg_lt_prob_bb / count_1_neg_lt_prob_bb
prob_2_neg_lt_bb = sum_2_neg_lt_prob_bb / count_2_neg_lt_prob_bb

prob_0_neg_eq_bb = sum_0_neg_eq_prob_bb / count_0_neg_eq_prob_bb
prob_2_neg_eq_bb = sum_2_neg_eq_prob_bb / count_2_neg_eq_prob_bb
''''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ"],
        [prob_0_neg_gt_bb, prob_1_neg_gt_bb, prob_2_neg_gt_bb,
        prob_0_neg_lt_bb, prob_1_neg_lt_bb, prob_2_neg_lt_bb,
        prob_0_neg_eq_bb, prob_2_neg_eq_bb],
        color='#a6cf00')
'''
# negative Zahlen Model mathBert
sum_0_neg_gt_prob_mb = 0
sum_0_neg_lt_prob_mb = 0
sum_0_neg_eq_prob_mb = 0

sum_1_neg_gt_prob_mb = 0
sum_1_neg_lt_prob_mb = 0
sum_1_neg_eq_prob_mb = 0

sum_2_neg_gt_prob_mb = 0
sum_2_neg_lt_prob_mb = 0
sum_2_neg_eq_prob_mb = 0

count_0_neg_gt_prob_mb = 0
count_0_neg_lt_prob_mb = 0
count_0_neg_eq_prob_mb = 0

count_1_neg_gt_prob_mb = 0
count_1_neg_lt_prob_mb = 0
count_1_neg_eq_prob_mb = 0

count_2_neg_gt_prob_mb = 0
count_2_neg_lt_prob_mb = 0
count_2_neg_eq_prob_mb = 0

for line in mb.values:
    if ">" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_gt_prob_mb += float(line[12]) * 100
            count_0_neg_gt_prob_mb +=1
        if(line[0].count("-") == 1):
            sum_1_neg_gt_prob_mb += float(line[12]) * 100
            count_1_neg_gt_prob_mb +=1
        if(line[0].count("-") == 2):
            sum_2_neg_gt_prob_mb += float(line[12]) * 100
            count_2_neg_gt_prob_mb +=1
    if "<" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_lt_prob_mb += float(line[10]) * 100
            count_0_neg_lt_prob_mb +=1
        if(line[0].count("-") == 1):
            sum_1_neg_lt_prob_mb += float(line[10]) * 100
            count_1_neg_lt_prob_mb +=1
        if(line[0].count("-") == 2):
            sum_2_neg_lt_prob_mb += float(line[10]) * 100
            count_2_neg_lt_prob_mb +=1
    if "=" in line[1]:
        if(line[0].count("-") == 0):
            sum_0_neg_eq_prob_mb += float(line[8]) * 100
            count_0_neg_eq_prob_mb +=1
        if(line[0].count("-") == 1):
            sum_1_neg_eq_prob_mb += float(line[8]) * 100
            count_1_neg_eq_prob_mb +=1
        if(line[0].count("-") == 2):
            sum_2_neg_eq_prob_mb += float(line[8]) * 100
            count_2_neg_eq_prob_mb +=1

prob_0_neg_gt_mb = sum_0_neg_gt_prob_mb / count_0_neg_gt_prob_mb
prob_1_neg_gt_mb = sum_1_neg_gt_prob_mb / count_1_neg_gt_prob_mb
prob_2_neg_gt_mb = sum_2_neg_gt_prob_mb / count_2_neg_gt_prob_mb

prob_0_neg_lt_mb = sum_0_neg_lt_prob_mb / count_0_neg_lt_prob_mb
prob_1_neg_lt_mb = sum_1_neg_lt_prob_mb / count_1_neg_lt_prob_mb
prob_2_neg_lt_mb = sum_2_neg_lt_prob_mb / count_2_neg_lt_prob_mb

prob_0_neg_eq_mb = sum_0_neg_eq_prob_mb / count_0_neg_eq_prob_mb
prob_2_neg_eq_mb = sum_2_neg_eq_prob_mb / count_2_neg_eq_prob_mb
'''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ"],
        [prob_0_neg_gt_mb, prob_1_neg_gt_mb, prob_2_neg_gt_mb,
        prob_0_neg_lt_mb, prob_1_neg_lt_mb, prob_2_neg_lt_mb,
        prob_0_neg_eq_mb, prob_2_neg_eq_mb],
        color='#009ca4')
'''
'''
plt.ylabel('Wahrscheinlichkeit in Prozent')
plt.xlabel('[Mask]-Token, Anzahl Vorkommen negativer Zahlen')
plt.tight_layout()
'''

### Confusionsmatrix erwartet, vorhergesagte Token

class_dict = {1: '>', 2: '<', 3: '='}
#Modell BB
'''
conf_matrix = np.array([[0.0084, 0.0135, 0.0738],
                        [0.0303, 0.0064, 0.0227],
                        [0.0195, 0.1564, 0.2613]])

conf_matrix = np.array([[0.0448, 0.0710, 0.6825],
                        [0.8899, 0.2347, 0.8700],
                        [0.0563, 0.6482, 0.6138]])

# Modell AR
conf_matrix = np.array([[0.6567, 0.5373, 0.6825],
                        [0.7323, 0.9159, 0.7858],
                        [5.7318, 19.0637, 12.7400]])
'''
#Matrix für negative Vorzeichen
#BB
'''
conf_matrix = np.array([[0.0023, 0.0010, 0.4433],
                        [0.0110, 0.0083, 0],
                        [0.0092, 0.0081, 0.071]])
#MB
conf_matrix = np.array([[0.0659, 0.0754, 1.1452],
                        [0.0552, 0.0278, 0],
                        [0.0049, 0.8669, 0.0584]])

conf_matrix = np.array([[2.3970, 1.3796, 8.1184],
                        [0.1164, 0.9266, 0],
                        [0.0627, 0.3766, 17.5695]])

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center')

#plt.yticks(range(3), [">", "<", "="])
plt.yticks(range(3), ["0", "1", "2"])

plt.xticks(range(3), [">", "<", "="])

plt.xlabel('Predicted')
plt.ylabel('Actual')
'''
plt.show()

