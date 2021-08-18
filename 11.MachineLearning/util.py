
# 평가지표 출력 함수
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
def print_metrics(y, pred, title=None):
    acc = accuracy_score(y, pred)
    rec = recall_score(y, pred)
    pre = precision_score(y, pred)
    f1 = f1_score(y, pred)
    if title:
        print(title)
    print(f'정확도: {acc}, recall: {rec}, precision: {pre}, f1점수: {f1}')
