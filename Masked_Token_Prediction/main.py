# https://towardsdatascience.com/how-to-train-a-bert-model-from-scratch-72cfce554fc6
from datetime import datetime
from transformers import BertTokenizer, BertForMaskedLM, pipeline, BertModel
import torch
import csv


def compute():
    startTime = datetime.now()

    #tokenizer = BertTokenizer.from_pretrained('AnReu/math_pretrained_bert', output_hidden_states=True)
    #model = "AnReu/math_pretrained_bert"

    #tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    #model = BertForMaskedLM.from_pretrained('bert-base-uncased')

    tokenizer = BertTokenizer.from_pretrained('tbs17/MathBERT', output_hidden_states=True)
    model = 'tbs17/MathBERT'

    with open('path/to/dataSet', 'r') as fp:
        data = fp.read()

    inputs = tokenizer(data, return_tensors='pt', max_length=512, truncation=True, padding='max_length')

    #input_ids klonen, um Label-Tensor zu erstellen
    inputs['labels'] = inputs.input_ids.detach().clone()

    #Gleichungszeichen maskieren für die anderen beiden Modelle

    mask_arr = (inputs.input_ids == 1026) + (inputs.input_ids == 1027) + (inputs.input_ids == 1028) * \
               (inputs.input_ids != 101) * (inputs.input_ids != 102) * (inputs.input_ids != 0)
    '''
    #token_ids für das Model 'AnReu/math_pretrained_bert' -> Vergleichszeichen maskieren
    mask_arr = (inputs.input_ids == 133) + (inputs.input_ids == 134) + (inputs.input_ids == 135) * \
               (inputs.input_ids != 101) * (inputs.input_ids != 102) * (inputs.input_ids != 0)
    '''
    selection = torch.flatten(mask_arr[0].nonzero()).tolist()

    inputs.input_ids[0, selection] = 103

    unmasker = pipeline('fill-mask', model=model, tokenizer=tokenizer, top_k=10000)

    linesUnmasked = data.split('\n')
    lines = data.replace('=', '[MASK]').replace('<', '[MASK]').replace('>', '[MASK]').split('\n')

    with open('path/to/csv',
              'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        field = ["Formula", "[MASK]-Token", "Top 1 Token", "Top 1 Probability", "Top 2 Token",
                 "Top 2 Probability", "Top 3 Token", "Top 3 Probability", "Token = Probability", "Top k =",
                 "Token < Probability", "Top k <", "Token > Probability", "Top k >", "Position Hit"]
        writer.writerow(field)

        i = 0
        for line in lines:
            if(i%50 == 0):
                print("Line " + str(i))

            unmasked = unmasker(line)

            best1 = unmasked[0]
            best2 = unmasked[1]
            best3 = unmasked[2]

            token1 = best1.get("token_str")
            token2 = best2.get("token_str")
            token3 = best3.get("token_str")

            scoreEq = ""
            scoreLe = ""
            scoreGe = ""

            hit = "NULL"
            if(token1 in "=<>"  and token1 in linesUnmasked[i]):
                hit = 1
            if(token2 in "=<>"  and token2 in linesUnmasked[i]):
                hit = 2
            if(token3 in "=<>"  and token3 in linesUnmasked[i]):
                hit = 3

            eqFound = False
            leFound = False
            geFound = False

            eqCount = 0
            geCount = 0
            leCount = 0

            count = 1
            for item in unmasked:
                token = item.get("token_str")
                if(token == "="):
                    scoreEq = item.get("score")
                    eqCount = count
                    eqFound = True
                if(token == "<"):
                    scoreLe = item.get("score")
                    leCount = count
                    leFound = True
                if(token == ">"):
                    scoreGe = item.get("score")
                    geCount = count
                    geFound = True
                if(eqFound == True and leFound == True  and geFound == True ):
                    break
                count += 1

            maskToken = ""
            if("=" in linesUnmasked[i]):
                maskToken = "="
            if("<" in linesUnmasked[i]):
                maskToken = "<"
            if(">" in linesUnmasked[i]):
                maskToken = ">"

            writer.writerow([linesUnmasked[i], maskToken, str(token1), best1.get("score"), str(token2),
                             best2.get("score"), str(token3), best3.get("score"), scoreEq, eqCount, scoreLe, leCount,
                             scoreGe, geCount, hit])
            i += 1

    endTime = datetime.now()

    print("Das Programm lief "+str(endTime-startTime)+" Sekunden")


if __name__ == "__main__":
    compute()
