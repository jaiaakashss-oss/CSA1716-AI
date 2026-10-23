
import math
from collections import Counter

# Sample dataset
data = [
    ['Sunny', 'No'],
    ['Sunny', 'No'],
    ['Overcast', 'Yes'],
    ['Rainy', 'Yes'],
    ['Rainy', 'Yes'],
    ['Overcast', 'Yes']
]

def entropy(labels):
    total = len(labels)
    counts = Counter(labels)

    return -sum(
        (count / total) * math.log2(count / total)
        for count in counts.values()
    )

def information_gain(data, feature_index):
    labels = [row[-1] for row in data]
    total_entropy = entropy(labels)

    values = set(row[feature_index] for row in data)
    weighted_entropy = 0

    for value in values:
        subset = [row for row in data
                  if row[feature_index] == value]
        subset_labels = [row[-1] for row in subset]

        weighted_entropy += (
            len(subset) / len(data)
        ) * entropy(subset_labels)

    return total_entropy - weighted_entropy

def build_tree(data, features):
    labels = [row[-1] for row in data]

    # If all labels are the same
    if len(set(labels)) == 1:
        return labels[0]

    # If no features remain
    if not features:
        return Counter(labels).most_common(1)[0][0]

    best_feature = max(
        features,
        key=lambda f: information_gain(data, f)
    )

    tree = {best_feature: {}}

    values = set(row[best_feature] for row in data)

    for value in values:
        subset = [row for row in data
                  if row[best_feature] == value]

        remaining = [f for f in features
                     if f != best_feature]

        tree[best_feature][value] = build_tree(
            subset, remaining
        )

    return tree

# Feature index 0 represents Outlook
features = [0]
tree = build_tree(data, features)

print("Decision Tree:")
print(tree)
