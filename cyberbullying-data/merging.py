import pandas as pd

train_df_duplicate = pd.read_csv("cyberbullying-data/finaltrdata.csv", index_col="Index")
test_df_duplicate = pd.read_csv("cyberbullying-data/finaltsdata.csv", index_col="Index")

train_df = train_df_duplicate.drop_duplicates()
test_df = test_df_duplicate.drop_duplicates()

train_df = train_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)
print(train_df.columns)
print(test_df.columns)

cb_labels_df = pd.read_csv("cyberbullying-data/6. CB_Labels.csv")
cb_labels_df = cb_labels_df.drop_duplicates()
cb_labels_df = cb_labels_df.reset_index(drop=True)
print(cb_labels_df.columns)
print(cb_labels_df.head())

train_merged = pd.merge(
    train_df,
    cb_labels_df[['User1_ID', 'User2_ID', 'CB_Label']],
    left_on=['source_node', 'destination_node'],
    right_on=['User1_ID', 'User2_ID'],
    how="left"
)

test_merged = pd.merge(
    test_df,
    cb_labels_df[['User1_ID', 'User2_ID', 'CB_Label']],
    left_on=['source_node', 'destination_node'],
    right_on=['User1_ID', 'User2_ID'],
    how="left"
)

train_merged["CB_Label"] = train_merged["CB_Label"].fillna("Unknown")
test_merged["CB_Label"] = test_merged["CB_Label"].fillna("Unknown")

train_merged = train_merged.sort_values(by=["source_node", "destination_node"]).reset_index(drop=True)
test_merged = test_merged.sort_values(by=["source_node", "destination_node"]).reset_index(drop=True)

train_merged.to_csv('cyberbullying-data\merged_train.csv', index=False)
test_merged.to_csv('cyberbullying-data\merged_test.csv', index=False)

print("Merge Complete")

train_df = pd.read_csv('cyberbullying-data\merged_train.csv')
test_df = pd.read_csv('cyberbullying-data\merged_test.csv')

train_df = train_df.drop(['User1_ID', 'User2_ID'], axis=1)
test_df = test_df.drop(['User1_ID', 'User2_ID'], axis=1)

train_df.to_csv('cyberbullying-data\merged_train.csv', index=False)
test_df.to_csv('cyberbullying-data\merged_test.csv', index=False)
print('done')