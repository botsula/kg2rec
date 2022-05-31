# Sparsity test for [30, 60, 90] % of train set
# ndcg 20

train_test_split = {
    '90': [90, 5, 5],
    '60': [6, 2, 2],
    '30': [3, 4, 3]
}

config_e_sparsity_90 = {
    "epochs": 10,
    "train_batch_size": 1024,
    "eval_batch_size": 2048,
    "eval_args": {
        "group_by": "user",
        "order": "RO",
        "split": {'RS': train_test_split['90']},
        "mode": "full"
    },
    "metrics": ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'MAP'],
    "topk": [10, 20, 30, 40, 50],
    "valid_metric": "MRR@10",
    "metric_decimal_place": 4
}

config_e_sparsity_60 = {
    "epochs": 10,
    "train_batch_size": 1024,
    "eval_batch_size": 2048,
    "eval_args": {
        "group_by": "user",
        "order": "RO",
        "split": {'RS': train_test_split['60']},
        "mode": "full"
    },
    "metrics": ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'MAP'],
    "topk": [10, 20, 30, 40, 50],
    "valid_metric": "MRR@10",
    "metric_decimal_place": 4
}

config_e_sparsity_30 = {
    "epochs": 10,
    "train_batch_size": 1024,
    "eval_batch_size": 2048,
    "eval_args": {
        "group_by": "user",
        "order": "RO",
        "split": {'RS': train_test_split['30']},
        "mode": "full"
    },
    "metrics": ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'MAP'],
    "topk": [10, 20, 30, 40, 50],
    "valid_metric": "MRR@10",
    "metric_decimal_place": 4
}
