import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Data ko sahi format mein (Events as Columns)
data = {
    'Unauthorized_Login': [1, 1, 0, 1, 1], # 1 matlab hua, 0 matlab nahi
    'File_Access':        [1, 1, 1, 0, 1],
    'Data_Export':        [0, 1, 0, 1, 1]
}
df = pd.DataFrame(data)

# 1. Apriori: 60% Support (Yaani kam se kam 3 logs mein hona chahiye)
freq_items = apriori(df, min_support=0.6, use_colnames=True)

# 2. Rules: 80% Confidence
rules = association_rules(freq_items, metric='confidence', min_threshold=0.8)

# Result print karo
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])