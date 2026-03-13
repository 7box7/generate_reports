import bisect
from collections import defaultdict
from typing import List, Dict, Tuple, DefaultDict

def median_coffee_report(data: List[Dict[str, str]]) -> List[Tuple[str, float]]:
    student_spends = get_student_coffee_spends(data)

    report = []
    for student in student_spends:
        spends = student_spends[student]
        if spends:
            n = len(spends)
            if n % 2 == 1:
                median_spend = spends[n // 2]
            else:
                median_spend = (spends[n // 2 - 1] + spends[n // 2]) / 2
            report.append((student, median_spend))

    report.sort(key=lambda x: x[1], reverse=True)
    return report

def get_student_coffee_spends(data: List[Dict[str, str]]) -> DefaultDict[str, List[float]]:
    student_spends = defaultdict(list)
    for row in data:
        student = row['student']
        
        try:
            spend = float(row['coffee_spent'])
            bisect.insort(student_spends[student], spend)
        except ValueError:
            continue
    return student_spends
