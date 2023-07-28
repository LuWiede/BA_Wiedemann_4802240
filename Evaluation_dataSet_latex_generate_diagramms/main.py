import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
'''------------------------------------------------------------------------------------------------------------------'''

def withoutOnes(item):
    for k, v in list(item.items()):
        if  v<103:
            del item[k]

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

#plt.ylabel('Wahrscheinlichkeit in Prozent')
#plt.xlabel('Vergleichsoperator')
#plt.tight_layout()
#plt.bar([">", "<", "="], [prob_truthful_gt, prob_truthful_lt, prob_truthful_eq], color='#0b2a51')
#plt.bar([">", "<", "="], [prob_truthful_gt_bb, prob_truthful_lt_bb, prob_truthful_eq_bb], color='#a6cf00')
#plt.bar([">", "<", "="], [prob_truthful_gt_mb, prob_truthful_lt_mb, prob_truthful_eq_mb], color='#009ca4')

'''------------------------------------------------------------------------------------------------------------------'''
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
print("Mask <, Predicted < : " + str(prob_lt_truthful_lt_predicted_mb))
print("Mask <, Predicted = : " + str(prob_lt_truthful_eq_predicted_mb))

print("Mask =, Predicted > : " + str(prob_eq_truthful_gt_predicted_mb))
print("Mask =, Predicted < : " + str(prob_eq_truthful_lt_predicted_mb))
print("Mask =, Predicted = : " + str(prob_eq_truthful_eq_predicted_mb))
'''
'''------------------------------------------------------------------------------------------------------------------'''
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
sorted_top_1_predictions_lt = dict(sorted(top_1_predictions_lt.items(), key=lambda x: x[1]))
sorted_top_1_predictions_eq = dict(sorted(top_1_predictions_eq.items(), key=lambda x: x[1]))

#plt.bar(sorted_top_1_predictions_gt.keys(), sorted_top_1_predictions_gt.values(), color='#0b2a51')
#plt.bar(sorted_top_1_predictions_lt.keys(),sorted_top_1_predictions_lt.values(), color='#0b2a51')
#plt.bar(sorted_top_1_predictions_eq.keys(),sorted_top_1_predictions_eq.values(), color='#0b2a51')

plt.xticks(rotation=90)
plt.ylabel('Anzahl der vorhergesagten Token')
plt.xlabel('vorhergesagte Token')
plt.tight_layout()

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


#plt.xticks(rotation=90)
#plt.ylabel('Wahrscheinlichkeit der vorhergesagten Token')
#plt.xlabel('vorhergesagte Token')
#plt.tight_layout()

#plt.bar(sorted_top_1_predictions_gt_bb.keys(), sorted_top_1_predictions_gt_bb.values(), color='#a6cf00')
#plt.bar(sorted_top_1_predictions_lt_bb.keys(),sorted_top_1_predictions_lt_bb.values(), color='#a6cf00')
#plt.bar(sorted_top_1_predictions_eq_bb.keys(),sorted_top_1_predictions_eq_bb.values(), color='#a6cf00')


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

sorted_top_1_predictions_gt_mb = dict(sorted(top_1_predictions_gt_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_gt_mb)
sorted_top_1_predictions_lt_mb = dict(sorted(top_1_predictions_lt_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_lt_mb)
sorted_top_1_predictions_eq_mb = dict(sorted(top_1_predictions_eq_mb.items(), key=lambda x: x[1]))
withoutOnes(sorted_top_1_predictions_eq_mb)

print(sorted_top_1_predictions_eq_mb.values())

#plt.bar(sorted_top_1_predictions_gt_mb.keys(), sorted_top_1_predictions_gt_mb.values(), color='#009ca4')
#plt.bar(sorted_top_1_predictions_lt_mb.keys(),sorted_top_1_predictions_lt_mb.values(), color='#009ca4')
plt.bar(sorted_top_1_predictions_eq_mb.keys(),sorted_top_1_predictions_eq_mb.values(), color='#009ca4')

'''------------------------------------------------------------------------------------------------------------------'''

#Wkt für bestimmte formel art
#Durschnitt für Model AnReu berechnen
#equationType = "\\boxed"
#equationType = "\\frac"
equationType = "\\sqrt"
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

#Durschnitt für Model Bertbase berechnen
sum_truthful_prob_gt_bb = 0
count_gt_bb = 0

sum_truthful_prob_lt_bb = 0
count_lt_bb = 0

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
'''
plt.ylabel('Wahrscheinlichkeit in Prozent')
plt.xlabel('Vergleichsoperator, LaTeX-Ausdruck '+equationType)
plt.tight_layout()
plt.bar([">", "<", "="], [prob_truthful_gt, prob_truthful_lt, prob_truthful_eq], color='#0b2a51')
#plt.bar([">", "<", "="], [prob_truthful_gt_bb, prob_truthful_lt_bb, prob_truthful_eq_bb], color='#a6cf00')
#plt.bar([">", "<", "="], [prob_truthful_gt_mb, prob_truthful_lt_mb, prob_truthful_eq_mb], color='#009ca4')

print(prob_truthful_gt)
print(prob_truthful_lt)
print(prob_truthful_eq)
'''
#Wkt für ein oder zwei frac
#Durschnitt für Model AnReu berechnen
equationType = "\\frac"
occurences = 2

sum_truthful_prob_gt = 0
count_gt = 0

sum_truthful_prob_lt = 0
count_lt = 0

sum_truthful_prob_eq = 0
count_eq = 0

for line in ar.values:
    if line[0].count(equationType) is not occurences:
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

#Durschnitt für Model Bertbase berechnen
sum_truthful_prob_gt_bb = 0
count_gt_bb = 0

sum_truthful_prob_lt_bb = 0
count_lt_bb = 0

sum_truthful_prob_eq_bb = 0
count_eq_bb = 0

for line in bb.values:
    if line[0].count(equationType) is not occurences:
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

#Durchschnitt füt mathBERT berechnen
sum_truthful_prob_gt_mb = 0
count_gt_mb = 0

sum_truthful_prob_lt_mb = 0
count_lt_mb = 0

sum_truthful_prob_eq_mb = 0
count_eq_mb = 0

for line in mb.values:
    if line[0].count(equationType) is not occurences:
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

#plt.ylabel('Wahrscheinlichkeit in Prozent')
#plt.xlabel('Vergleichsoperator und LaTeX-Ausdruck '+equationType + ' mit '+str(occurences == 1)+' Vorkommnissen')
#plt.tight_layout()
#plt.bar([">", "<", "="], [prob_truthful_gt, prob_truthful_lt, prob_truthful_eq], color='#0b2a51')
#plt.bar([">", "<", "="], [prob_truthful_gt_bb, prob_truthful_lt_bb, prob_truthful_eq_bb], color='#a6cf00')
#plt.bar([">", "<", "="], [prob_truthful_gt_mb, prob_truthful_lt_mb, prob_truthful_eq_mb], color='#009ca4')


#zeigt die WSK bei 0,1,2 negative Zahlen, die richtigen Token vorhergesagt werden mit \boxed
# negative Zahlen Model AnReu
#equationType = "\\boxed"
#equationType = "\\mod"
equationType = "\\frac"

sum_0_neg_gt_prob = 0
sum_0_neg_lt_prob = 0
sum_0_neg_eq_prob = 0

sum_1_neg_gt_prob = 0
sum_1_neg_lt_prob = 0
sum_1_neg_eq_prob = 0

sum_2_neg_gt_prob = 0
sum_2_neg_lt_prob = 0
sum_2_neg_eq_prob = 0

sum_3_neg_gt_prob = 0
sum_3_neg_lt_prob = 0
sum_3_neg_eq_prob = 0

sum_4_neg_gt_prob = 0
sum_4_neg_lt_prob = 0
sum_4_neg_eq_prob = 0

count_0_neg_gt_prob = 0
count_0_neg_lt_prob = 0
count_0_neg_eq_prob = 0

count_1_neg_gt_prob = 0
count_1_neg_lt_prob = 0
count_1_neg_eq_prob = 0

count_2_neg_gt_prob = 0
count_2_neg_lt_prob = 0
count_2_neg_eq_prob = 0

count_3_neg_gt_prob = 0
count_3_neg_lt_prob = 0
count_3_neg_eq_prob = 0

count_4_neg_gt_prob = 0
count_4_neg_lt_prob = 0
count_4_neg_eq_prob = 0

for line in ar.values:
    if equationType not in line[0]:
        continue
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
        if(line[0].count("-") == 3):
            sum_3_neg_gt_prob += float(line[12]) * 100
            count_3_neg_gt_prob +=1
        if(line[0].count("-") == 4):
            sum_4_neg_gt_prob += float(line[12]) * 100
            count_4_neg_gt_prob +=1
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
        if(line[0].count("-") == 3):
            sum_3_neg_lt_prob += float(line[10]) * 100
            count_3_neg_lt_prob+=1
        if(line[0].count("-") == 4):
            sum_4_neg_lt_prob += float(line[10]) * 100
            count_4_neg_lt_prob+=1
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
        if(line[0].count("-") == 3):
            sum_3_neg_eq_prob += float(line[8]) * 100
            count_3_neg_eq_prob+=1
        if(line[0].count("-") == 4):
            sum_4_neg_eq_prob += float(line[8]) * 100
            count_4_neg_eq_prob+=1

prob_0_neg_gt = sum_0_neg_gt_prob / count_0_neg_gt_prob
prob_1_neg_gt = sum_1_neg_gt_prob / count_1_neg_gt_prob
prob_2_neg_gt = sum_2_neg_gt_prob / count_2_neg_gt_prob
prob_3_neg_gt = sum_3_neg_gt_prob / count_3_neg_gt_prob
prob_4_neg_gt = sum_4_neg_gt_prob / count_4_neg_gt_prob

prob_0_neg_lt = sum_0_neg_lt_prob / count_0_neg_lt_prob
prob_1_neg_lt = sum_1_neg_lt_prob / count_1_neg_lt_prob
prob_2_neg_lt = sum_2_neg_lt_prob / count_2_neg_lt_prob
prob_3_neg_lt = sum_3_neg_lt_prob / count_3_neg_lt_prob
prob_4_neg_lt = sum_4_neg_lt_prob / count_4_neg_lt_prob

prob_0_neg_eq = sum_0_neg_eq_prob / count_0_neg_eq_prob
prob_2_neg_eq = sum_2_neg_eq_prob / count_2_neg_eq_prob
prob_4_neg_eq = sum_4_neg_eq_prob / count_4_neg_eq_prob
'''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ"],
        [prob_0_neg_gt, prob_1_neg_gt, prob_2_neg_gt,
        prob_0_neg_lt, prob_1_neg_lt, prob_2_neg_lt,
        prob_0_neg_eq, prob_2_neg_eq],
        color='#0b2a51')

print("Mask >, 0 negativ : " + str(prob_0_neg_gt))
print("Mask >, 1 negativ : " + str(prob_1_neg_gt))
print("Mask <, 2 negativ : " + str(prob_2_neg_gt))

print("Mask <, 0 negativ : " + str(prob_0_neg_lt))
print("Mask <, 1 negativ : " + str(prob_1_neg_lt))
print("Mask <, 2 negativ : " + str(prob_2_neg_lt))

print("Mask =, 0 negativ : " + str(prob_0_neg_eq))
print("Mask =, 2 negativ : " + str(prob_2_neg_eq))
'''
'''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ","Mask >,\n 3 negativ","Mask >,\n 4 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ","Mask <,\n 3 negativ","Mask <,\n 4 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ", "Mask =,\n 4 negativ"],
        [prob_0_neg_gt, prob_1_neg_gt, prob_2_neg_gt,prob_3_neg_gt,prob_4_neg_gt,
        prob_0_neg_lt, prob_1_neg_lt, prob_2_neg_lt,prob_3_neg_lt,prob_4_neg_lt,
        prob_0_neg_eq, prob_2_neg_eq, prob_4_neg_eq],
        color='#0b2a51')

print("Mask >, 0 negativ : " +str(prob_0_neg_gt))
print("Mask >, 1 negativ : " +str(prob_1_neg_gt))
print("Mask >, 2 negativ : " +str(prob_2_neg_gt))
print("Mask >, 3 negativ : " +str(prob_3_neg_gt))
print("Mask >,  4 negativ : " +str(prob_4_neg_gt))

print("Mask <, 0 negativ : " +str(prob_0_neg_lt))
print("Mask <, 1 negativ : " +str(prob_1_neg_lt))
print("Mask <, 2 negativ : " +str(prob_2_neg_lt))
print("Mask <, 3 negativ : " +str(prob_3_neg_lt))
print("Mask <, 4 negativ : " +str(prob_4_neg_lt))

print("Mask =, 0 negativ : " +str(prob_0_neg_eq))
print("Mask =, 2 negativ : " +str(prob_2_neg_eq))
print("Mask =, 4 negativ : " +str(prob_4_neg_eq))
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

sum_3_neg_gt_prob_bb = 0
sum_3_neg_lt_prob_bb = 0
sum_3_neg_eq_prob_bb = 0

sum_4_neg_gt_prob_bb = 0
sum_4_neg_lt_prob_bb = 0
sum_4_neg_eq_prob_bb = 0

count_0_neg_gt_prob_bb = 0
count_0_neg_lt_prob_bb = 0
count_0_neg_eq_prob_bb = 0

count_1_neg_gt_prob_bb = 0
count_1_neg_lt_prob_bb = 0
count_1_neg_eq_prob_bb = 0

count_2_neg_gt_prob_bb = 0
count_2_neg_lt_prob_bb = 0
count_2_neg_eq_prob_bb = 0

count_3_neg_gt_prob_bb = 0
count_3_neg_lt_prob_bb = 0
count_3_neg_eq_prob_bb = 0

count_4_neg_gt_prob_bb = 0
count_4_neg_lt_prob_bb = 0
count_4_neg_eq_prob_bb = 0

for line in bb.values:
    if equationType not in line[0]:
        continue
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
        if(line[0].count("-") == 3):
            sum_3_neg_gt_prob_bb += float(line[12]) * 100
            count_3_neg_gt_prob_bb +=1
        if(line[0].count("-") == 4):
            sum_4_neg_gt_prob_bb += float(line[12]) * 100
            count_4_neg_gt_prob_bb +=1
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
        if(line[0].count("-") == 3):
            sum_3_neg_lt_prob_bb += float(line[10]) * 100
            count_3_neg_lt_prob_bb +=1
        if(line[0].count("-") == 4):
            sum_4_neg_lt_prob_bb += float(line[10]) * 100
            count_4_neg_lt_prob_bb +=1
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
        if(line[0].count("-") == 3):
            sum_3_neg_eq_prob_bb += float(line[8]) * 100
            count_3_neg_eq_prob_bb +=1
        if(line[0].count("-") == 4):
            sum_4_neg_eq_prob_bb += float(line[8]) * 100
            count_4_neg_eq_prob_bb +=1

prob_0_neg_gt_bb = sum_0_neg_gt_prob_bb / count_0_neg_gt_prob_bb
prob_1_neg_gt_bb = sum_1_neg_gt_prob_bb / count_1_neg_gt_prob_bb
prob_2_neg_gt_bb = sum_2_neg_gt_prob_bb / count_2_neg_gt_prob_bb
prob_3_neg_gt_bb = sum_3_neg_gt_prob_bb / count_3_neg_gt_prob_bb
prob_4_neg_gt_bb = sum_4_neg_gt_prob_bb / count_4_neg_gt_prob_bb

prob_0_neg_lt_bb = sum_0_neg_lt_prob_bb / count_0_neg_lt_prob_bb
prob_1_neg_lt_bb = sum_1_neg_lt_prob_bb / count_1_neg_lt_prob_bb
prob_2_neg_lt_bb = sum_2_neg_lt_prob_bb / count_2_neg_lt_prob_bb
prob_3_neg_lt_bb = sum_3_neg_lt_prob_bb / count_3_neg_lt_prob_bb
prob_4_neg_lt_bb = sum_4_neg_lt_prob_bb / count_4_neg_lt_prob_bb

prob_0_neg_eq_bb = sum_0_neg_eq_prob_bb / count_0_neg_eq_prob_bb
prob_2_neg_eq_bb = sum_2_neg_eq_prob_bb / count_2_neg_eq_prob_bb
prob_4_neg_eq_bb = sum_4_neg_eq_prob_bb / count_4_neg_eq_prob_bb
'''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ"],
        [prob_0_neg_gt_bb, prob_1_neg_gt_bb, prob_2_neg_gt_bb,
        prob_0_neg_lt_bb, prob_1_neg_lt_bb, prob_2_neg_lt_bb,
        prob_0_neg_eq_bb, prob_2_neg_eq_bb],
        color='#a6cf00')
        
print("Mask >, 0 negativ : " + str(prob_0_neg_gt_bb))
print("Mask >, 1 negativ : " + str(prob_1_neg_gt_bb))
print("Mask <, 2 negativ : " + str(prob_2_neg_gt_bb))

print("Mask <, 0 negativ : " + str(prob_0_neg_lt_bb))
print("Mask <, 1 negativ : " + str(prob_1_neg_lt_bb))
print("Mask <, 2 negativ : " + str(prob_2_neg_lt_bb))

print("Mask =, 0 negativ : " + str(prob_0_neg_eq_bb))
print("Mask =, 2 negativ : " + str(prob_2_neg_eq_bb))
'''
'''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ","Mask >,\n 3 negativ","Mask >,\n 4 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ","Mask <,\n 3 negativ","Mask <,\n 4 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ", "Mask =,\n 4 negativ"],
        [prob_0_neg_gt_bb, prob_1_neg_gt_bb, prob_2_neg_gt_bb,prob_3_neg_gt_bb,prob_4_neg_gt_bb,
        prob_0_neg_lt_bb, prob_1_neg_lt_bb, prob_2_neg_lt_bb,prob_3_neg_lt_bb,prob_4_neg_lt_bb,
        prob_0_neg_eq_bb, prob_2_neg_eq_bb, prob_4_neg_eq_bb],
        color='#a6cf00')

print("Mask >, 0 negativ : " +str(prob_0_neg_gt_bb))
print("Mask >, 1 negativ : " +str(prob_1_neg_gt_bb))
print("Mask >, 2 negativ : " +str(prob_2_neg_gt_bb))
print("Mask >, 3 negativ : " +str(prob_3_neg_gt_bb))
print("Mask >,  4 negativ : " +str(prob_4_neg_gt_bb))

print("Mask <, 0 negativ : " +str(prob_0_neg_lt_bb))
print("Mask <, 1 negativ : " +str(prob_1_neg_lt_bb))
print("Mask <, 2 negativ : " +str(prob_2_neg_lt_bb))
print("Mask <, 3 negativ : " +str(prob_3_neg_lt_bb))
print("Mask <, 4 negativ : " +str(prob_4_neg_lt_bb))

print("Mask =, 0 negativ : " +str(prob_0_neg_eq_bb))
print("Mask =, 2 negativ : " +str(prob_2_neg_eq_bb))
print("Mask =, 4 negativ : " +str(prob_4_neg_eq_bb))
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

sum_3_neg_gt_prob_mb = 0
sum_3_neg_lt_prob_mb = 0
sum_3_neg_eq_prob_mb = 0

sum_4_neg_gt_prob_mb = 0
sum_4_neg_lt_prob_mb = 0
sum_4_neg_eq_prob_mb = 0

count_0_neg_gt_prob_mb = 0
count_0_neg_lt_prob_mb = 0
count_0_neg_eq_prob_mb = 0

count_1_neg_gt_prob_mb = 0
count_1_neg_lt_prob_mb = 0
count_1_neg_eq_prob_mb = 0

count_2_neg_gt_prob_mb = 0
count_2_neg_lt_prob_mb = 0
count_2_neg_eq_prob_mb = 0

count_3_neg_gt_prob_mb = 0
count_3_neg_lt_prob_mb = 0
count_3_neg_eq_prob_mb = 0

count_4_neg_gt_prob_mb = 0
count_4_neg_lt_prob_mb = 0
count_4_neg_eq_prob_mb = 0

for line in mb.values:
    if equationType not in line[0]:
        continue
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
        if(line[0].count("-") == 3):
            sum_3_neg_gt_prob_mb += float(line[12]) * 100
            count_3_neg_gt_prob_mb +=1
        if(line[0].count("-") == 4):
            sum_4_neg_gt_prob_mb += float(line[12]) * 100
            count_4_neg_gt_prob_mb +=1
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
        if(line[0].count("-") == 3):
            sum_3_neg_lt_prob_mb += float(line[10]) * 100
            count_3_neg_lt_prob_mb +=1
        if(line[0].count("-") == 4):
            sum_4_neg_lt_prob_mb += float(line[10]) * 100
            count_4_neg_lt_prob_mb +=1
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
        if(line[0].count("-") == 3):
            sum_3_neg_eq_prob_mb += float(line[8]) * 100
            count_3_neg_eq_prob_mb +=1
        if(line[0].count("-") == 4):
            sum_4_neg_eq_prob_mb += float(line[8]) * 100
            count_4_neg_eq_prob_mb +=1

prob_0_neg_gt_mb = sum_0_neg_gt_prob_mb / count_0_neg_gt_prob_mb
prob_1_neg_gt_mb = sum_1_neg_gt_prob_mb / count_1_neg_gt_prob_mb
prob_2_neg_gt_mb = sum_2_neg_gt_prob_mb / count_2_neg_gt_prob_mb
prob_3_neg_gt_mb = sum_3_neg_gt_prob_mb / count_3_neg_gt_prob_mb
prob_4_neg_gt_mb = sum_4_neg_gt_prob_mb / count_4_neg_gt_prob_mb

prob_0_neg_lt_mb = sum_0_neg_lt_prob_mb / count_0_neg_lt_prob_mb
prob_1_neg_lt_mb = sum_1_neg_lt_prob_mb / count_1_neg_lt_prob_mb
prob_2_neg_lt_mb = sum_2_neg_lt_prob_mb / count_2_neg_lt_prob_mb
prob_3_neg_lt_mb = sum_3_neg_lt_prob_mb / count_3_neg_lt_prob_mb
prob_4_neg_lt_mb = sum_4_neg_lt_prob_mb / count_4_neg_lt_prob_mb

prob_0_neg_eq_mb = sum_0_neg_eq_prob_mb / count_0_neg_eq_prob_mb
prob_2_neg_eq_mb = sum_2_neg_eq_prob_mb / count_2_neg_eq_prob_mb
prob_4_neg_eq_mb = sum_4_neg_eq_prob_mb / count_4_neg_eq_prob_mb

'''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ","Mask >,\n 3 negativ","Mask >,\n 4 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ","Mask <,\n 3 negativ","Mask <,\n 4 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ", "Mask =,\n 4 negativ"],
        [prob_0_neg_gt_mb, prob_1_neg_gt_mb, prob_2_neg_gt_mb,prob_3_neg_gt_mb,prob_4_neg_gt_mb,
        prob_0_neg_lt_mb, prob_1_neg_lt_mb, prob_2_neg_lt_mb,prob_3_neg_lt_mb,prob_4_neg_lt_mb,
        prob_0_neg_eq_mb, prob_2_neg_eq_mb, prob_4_neg_eq_mb],
        color='#009ca4')

print("Mask >, 0 negativ : " +str(prob_0_neg_gt_mb))
print("Mask >, 1 negativ : " +str(prob_1_neg_gt_mb))
print("Mask >, 2 negativ : " +str(prob_2_neg_gt_mb))
print("Mask >, 3 negativ : " +str(prob_3_neg_gt_mb))
print("Mask >,  4 negativ : " +str(prob_4_neg_gt_mb))

print("Mask <, 0 negativ : " +str(prob_0_neg_lt_mb))
print("Mask <, 1 negativ : " +str(prob_1_neg_lt_mb))
print("Mask <, 2 negativ : " +str(prob_2_neg_lt_mb))
print("Mask <, 3 negativ : " +str(prob_3_neg_lt_mb))
print("Mask <, 4 negativ : " +str(prob_4_neg_lt_mb))

print("Mask =, 0 negativ : " +str(prob_0_neg_eq_mb))
print("Mask =, 2 negativ : " +str(prob_2_neg_eq_mb))
print("Mask =, 4 negativ : " +str(prob_4_neg_eq_mb))
'''
'''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ", "Mask <,\n 2 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 2 negativ"],
        [prob_0_neg_gt_mb, prob_1_neg_gt_mb, prob_2_neg_gt_mb,
        prob_0_neg_lt_mb, prob_1_neg_lt_mb, prob_2_neg_lt_mb,
        prob_0_neg_eq_mb, prob_2_neg_eq_mb],
        color='#')

print("Mask >, 0 negativ : " + str(prob_0_neg_gt_mb))
print("Mask >, 1 negativ : " + str(prob_1_neg_gt_mb))
print("Mask <, 2 negativ : " + str(prob_2_neg_gt_mb))

print("Mask <, 0 negativ : " + str(prob_0_neg_lt_mb))
print("Mask <, 1 negativ : " + str(prob_1_neg_lt_mb))
print("Mask <, 2 negativ : "009ca4 + str(prob_2_neg_lt_mb))

print("Mask =, 0 negativ : " + str(prob_0_neg_eq_mb))
print("Mask =, 2 negativ : " + str(prob_2_neg_eq_mb))
'''
'''
plt.ylabel('Wahrscheinlichkeit in Prozent')
plt.xlabel('[Mask]-Token, Anzahl Vorkommen negativer Zahlen')
plt.tight_layout()
'''
#nur für mod Einfluss negativer Vorzeichen

equationType_mod = "\\mod"

sum_0_neg_gt_prob = 0
sum_0_neg_lt_prob = 0
sum_0_neg_eq_prob = 0

sum_1_neg_gt_prob = 0
sum_1_neg_lt_prob = 0
sum_1_neg_eq_prob = 0

sum_2_neg_gt_prob = 0

count_0_neg_gt_prob = 0
count_0_neg_lt_prob = 0
count_0_neg_eq_prob = 0

count_1_neg_gt_prob = 0
count_1_neg_lt_prob = 0
count_1_neg_eq_prob = 0

count_2_neg_gt_prob = 0

for line in ar.values:
    if equationType_mod not in line[0]:
        continue
    if ">" in line[1]:
        if (line[0].count("-") == 0):
            sum_0_neg_gt_prob += float(line[12]) * 100
            count_0_neg_gt_prob += 1
        if (line[0].count("-") == 1):
            sum_1_neg_gt_prob += float(line[12]) * 100
            count_1_neg_gt_prob += 1
        if (line[0].count("-") == 2):
            sum_2_neg_gt_prob += float(line[12]) * 100
            count_2_neg_gt_prob += 1
    if "<" in line[1]:
        if (line[0].count("-") == 0):
            sum_0_neg_lt_prob += float(line[10]) * 100
            count_0_neg_lt_prob += 1
        if (line[0].count("-") == 1):
            sum_1_neg_lt_prob += float(line[10]) * 100
            count_1_neg_lt_prob += 1
    if "=" in line[1]:
        if (line[0].count("-") == 0):
            sum_0_neg_eq_prob += float(line[8]) * 100
            count_0_neg_eq_prob += 1
        if (line[0].count("-") == 1):
            sum_1_neg_eq_prob += float(line[8]) * 100
            count_1_neg_eq_prob += 1

prob_0_neg_gt = sum_0_neg_gt_prob / count_0_neg_gt_prob
prob_1_neg_gt = sum_1_neg_gt_prob / count_1_neg_gt_prob
prob_2_neg_gt = sum_2_neg_gt_prob / count_2_neg_gt_prob


prob_0_neg_lt = sum_0_neg_lt_prob / count_0_neg_lt_prob
prob_1_neg_lt = sum_1_neg_lt_prob / count_1_neg_lt_prob


prob_0_neg_eq = sum_0_neg_eq_prob / count_0_neg_eq_prob
prob_1_neg_eq = sum_1_neg_eq_prob / count_1_neg_eq_prob
'''
plt.bar(["Mask >,\n 0 negativ", "Mask >,\n 1 negativ", "Mask >,\n 2 negativ",
         "Mask <,\n 0 negativ ", "Mask <,\n 1 negativ",
         "Mask =,\n 0 negativ", "Mask =,\n 1 negativ"],
        [prob_0_neg_gt, prob_1_neg_gt, prob_2_neg_gt,
        prob_0_neg_lt, prob_1_neg_lt,
        prob_0_neg_eq, prob_1_neg_eq],
        color='#0b2a51')

print("Mask >, 0 negativ : " + str(prob_0_neg_gt))
print("Mask >, 1 negativ : " + str(prob_1_neg_gt))
print("Mask <, 2 negativ : " + str(prob_2_neg_gt))

print("Mask <, 0 negativ : " + str(prob_0_neg_lt))
print("Mask <, 1 negativ : " + str(prob_1_neg_lt))

print("Mask =, 0 negativ : " + str(prob_0_neg_eq))
print("Mask =, 1 negativ : " + str(prob_1_neg_eq))

plt.ylabel('Wahrscheinlichkeit in Prozent')
plt.xlabel('[Mask]-Token, Anzahl Vorkommen negativer Zahlen')
plt.tight_layout()
'''

#CM Matrix für erwartete und vorhergesagte Token
#BB allgemein
'''
conf_matrix = np.array([[0.5218, 0.7852, 0.7225],
                        [0.4471, 0.4657, 0.4781],
                        [11.0146, 15.8261, 18.8264]])

#MB
conf_matrix = np.array([[0.2294, 0.2300, 0.1846],
                        [0.5362, 0.6618, 0.6691],
                        [36.9360, 41.7963, 28.0332]])

#AR
conf_matrix = np.array([[1.9970, 1.7314, 1.1329],
                        [1.6976, 1.6461, 0.6670],
                        [69.6314, 68.6867, 54.8971]])
'''
'''
#Einfluss negativer Vorzeichen, LaTeX-Ausdruck boxed
#BB
conf_matrix = np.array([[0.9450, 0.5434, 40.1066],
                        [0.1246, 1.0460, 0],
                        [0.9048, 1.3148, 13.7904]])
#MB                   
conf_matrix = np.array([[0.0558, 0.0042, 2.8871],
                        [0.0198, 0.0192, 0],
                        [0.0168, 0.0712, 4.8851]])

#AR
conf_matrix = np.array([[5.6511, 2.6422, 18.8636],
                        [1.0616, 4.5382, 0],
                        [0.5554, 1.4402, 52.2075]])
'''
#Einfluss negativer Vorzeichen, LaTeX-Ausdruck frac
#BB
'''
conf_matrix = np.array([[0.2237, 0.1931, 6.6791],
                        [0.3263, 0.1854, 0],
                        [0.3063, 0.3018, 3.2766],
                        [0.3549, 0.1317, 0],
                        [0.1667, 0.2598, 1.2126]])

#MB
conf_matrix = np.array([[0.0855, 0.8557, 55.0390],
                        [0.2757, 0.8258, 0],
                        [0.5145, 1.7683, 42.8439],
                        [0.7656, 1.4167, 0],
                        [0.7603, 2.8157, 32.9647]])


#AR
conf_matrix = np.array([[0.8442, 0.7328, 76.2951],
                        [0.3834, 0.2646, 0],
                        [0.1755, 0.1426, 77.0918],
                        [0.0911, 0.0767, 0],
                        [0.0897, 0.0668, 80.8326]])
'''

#negative Vorzeichen mod
#BB
'''
conf_matrix = np.array([[0.5138, 0.1695, 11.4214],
                        [0.3233, 0.3541, 11.1156],
                        [0.1361, 0, 0]])

#MB
conf_matrix = np.array([[0.1243, 0.2604, 27.2670],
                        [0.0700, 0.0923, 23.7008],
                        [0.0032, 0, 0]])

#AR
conf_matrix = np.array([[0.2262, 0.1675, 56.6946],
                        [0.2213, 0.2288, 59.1710],
                        [0.1169, 0, 0]])

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center')

#plt.yticks(range(3), [">", "<", "="])
plt.yticks(range(3), ["0", "1", "2"])
#plt.yticks(range(5), ["0", "1", "2", "3", "4"])

plt.xticks(range(3), [">", "<", "="])

plt.xlabel('Predicted')
plt.ylabel('Actual')
'''
plt.show()