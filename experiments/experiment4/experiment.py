# General experiment for 2h

config_e_1 = {
    "epochs": 25,
    "train_batch_size": 1024,
    "eval_batch_size": 2048,
    "eval_args": {
        "group_by": "user",
        "order": "RO",
        "split": {'RS': [0.8, 0.1, 0.1]},
        "mode": "full"
    },
    "metrics": ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'MAP'],
    "topk": [10, 20, 30, 40, 50],
    "valid_metric": "MRR@10",
    "metric_decimal_place": 4,
    "embedding_size": 32
}
