import pandas as pd

def post_list(df):
    
    pos_grp_list = []
    pos_list = df['Pos.'].tolist()
    
    # Create duplicate title list.
    for pos in pos_list:
         if pos == 'WR':
            pos_grp_list.append('receiver')
         if pos == 'CB':
            pos_grp_list.append('d-back')
         if pos == 'DT':
            pos_grp_list.append('d-line')
         if pos == 'DE':
            pos_grp_list.append('d-line')
         if pos == 'RB':
            pos_grp_list.append('runner')
         if pos == 'TE':
            pos_grp_list.append('receiver')
         if pos == 'G':
            pos_grp_list.append('o-line')
         if pos == 'S':
            pos_grp_list.append('d-back')
         if pos == 'QB':
            pos_grp_list.append('passer')
         if pos == 'OLB':
            pos_grp_list.append('linebacker')
         if pos == 'LB':
            pos_grp_list.append('linebacker')
         if pos == 'T':
            pos_grp_list.append('o-line')
         if pos == 'ILB':
            pos_grp_list.append('linebacker')
         if pos == 'C':
            pos_grp_list.append('o-line')
         if pos == 'K':
            pos_grp_list.append('kicking')
         if pos == 'RT':
            pos_grp_list.append('o-line')
         if pos == 'LT':
            pos_grp_list.append('o-line')
         if pos == 'P':
            pos_grp_list.append('kicking')
         if pos == 'FS':
            pos_grp_list.append('d-back')
         if pos == 'SS':
            pos_grp_list.append('d-back') 
         if pos == 'LS':
            pos_grp_list.append('kicking')
         if pos == 'FB':
            pos_grp_list.append('runner')
         if pos == 'OL':
            pos_grp_list.append('o-line')
         else:
             continue
        
    df['POS_GRP'] = pos_grp_list
    
    return df

def spend_list(df, tuples):
    # Create list to store cpending designation per position group when compared to the rest of the year.
    spending_list = []

    # Binning POS_GRP_SPENDING based on metrics above.
    # low_win% = 0.00 - 25th%
    # avg_win% = 26th% - 75th%
    # high_win% = 76th% - 100th%

    for cap, pos_grp in tuples:
        if pos_grp == 'd-back':
            if cap <= 13.26:
                spending_list.append('low_spend')
            elif cap <= 18.98:
                spending_list.append('med_spend')
            elif cap <= 100:
                spending_list.append('high_spend')
            else:
                continue
        elif pos_grp == 'd-line':
            if cap <= 11.41:
                spending_list.append('low_spend')
            elif cap <= 19.13:
                spending_list.append('med_spend')
            elif cap <= 100:
                spending_list.append('high_spend')
            else:
                continue
        elif pos_grp == 'kicking':
            if cap <= 1.95:
                spending_list.append('low_spend')
            elif cap <= 3.47:
                spending_list.append('med_spend')
            elif cap <= 100:
                spending_list.append('high_spend')
            else:
                continue
        elif pos_grp == 'linebacker':
            if cap <= 7.88:
                spending_list.append('low_spend')
            elif cap <= 15.675:
                spending_list.append('med_spend')
            elif cap <= 100:
                spending_list.append('high_spend')
            else:
                continue
        elif pos_grp == 'o-line':
            if cap <= 15.32:
                spending_list.append('low_spend')
            elif cap <= 19.85:
                spending_list.append('med_spend')
            elif cap <= 100:
                spending_list.append('high_spend')
            else:
                continue
        elif pos_grp == 'passer':
            if cap <= 6.18:
                spending_list.append('low_spend')
            elif cap <= 14.39:
                spending_list.append('med_spend')
            elif cap <= 100:
                spending_list.append('high_spend')
            else:
                continue
        elif pos_grp == 'receiver':
            if cap <= 12.47:
                spending_list.append('low_spend')
            elif cap <= 18.32:
                spending_list.append('med_spend')
            elif cap <= 100:
                spending_list.append('high_spend')
            else:
                continue
        else:
            if cap <= 3.34:
                spending_list.append('low_spend')
            elif cap <= 6.2:
                spending_list.append('med_spend')
            elif cap <= 100:
                spending_list.append('high_spend')
            else:
                continue
                
    df['pos_grp_spending'] = spending_list
    return df