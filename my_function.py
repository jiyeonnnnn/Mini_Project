import chardet

def detect_encoding(path):
    detector = chardet.universaldetector.UniversalDetector()
    with open(path, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break;

    print(f'encoding: {detector.result}')
    detector.close()
    
def detect_outliers(data, /, *, column, multiplier = 1.5):
    q1, q3 = data[column].quantile([0.25, 0.75])
    iqr = q3-q1
    lfence = q1 - multiplier * iqr
    ufence = q3 + multiplier * iqr
    condition = (data[column] > ufence) | (data[column] < lfence)
    outliers = data.loc[condition, :].index.tolist()
    return (outliers, q1, q3, iqr, lfence, ufence)

def get_weekday_str(d):
    result = '일'
    code = d.weekday()
    if code == 0:
        result = '월'
    elif code == 1:
        result = '화'
    elif code == 2:
        result = '수'
    elif code == 3:
        result = '목'
    elif code == 4:
        result = '금'
    elif code == 5:
        result = '토'
    return result