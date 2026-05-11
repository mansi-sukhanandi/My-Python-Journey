import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Hamara Data (Bills ya Transactions)
# 1 matlab kharida, 0 matlab nahi kharida
data = {
    'Milk': [1, 1, 0, 1, 0],
    'Bread': [1, 1, 1, 0, 0],
    'Butter': [0, 1, 0, 1, 0],
    'Beer': [0, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

# 2. Apriori Algorithm lagana (Popular items dhoondna)
# Humne bola kam se kam 40% support hona chahiye
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# 3. Rules banana (Confidence ke base par)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])