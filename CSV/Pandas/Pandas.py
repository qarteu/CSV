import pandas as pd
#each column in data frame is a series

"""
Aggregation statistics can be calculated on entire columns or rows.

groupby provides the power of the split-apply-combine pattern.

value_counts is a convenient shortcut to count the number of entries in each category of a variable.

To user guide
"""

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        int("Age"): [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

age = df["Age"]
print(df[["Sex", "Age"]].groupby("Sex").mean())


print("the average age is:",df["Age"].mean())

print(age)

df.agg(
    {"Age:" ["min","max","median","mean","skew"]
    }

)