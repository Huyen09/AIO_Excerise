def calc_f1_score(tp, fp, fn):
    # Kiểm tra kiểu dữ liệu (bạn đã làm phần này)
    if type(tp) != int:
        print("tp must be int")
        return
    if type(fp) != int:
        print("fp must be int")
        return
    if type(fn) != int:
        print("fn must be int")
        return

    # Kiểm tra giá trị đầu vào 
    if tp <= 0 or  fp <= 0 or  fn <= 0:
        print("tp, fp, and fn must be non-negative")
        return

    # Tính toán Precision và Recall 
    precision = tp / (tp + fp) 
    recall = tp / (tp + fn) 

    # Tính toán F1 score 
    f1_score = 2 * precision * recall / (precision + recall) 

    # In kết quả
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1_score:.4f}")

calc_f1_score(5,5,2)



