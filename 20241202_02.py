def read_reports_from_file(file_path):
    reports = []
    
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            reports.append(report)
    
    return reports

def is_safe_report(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def is_safe_with_dampener(report):
    if is_safe_report(report):
        print("safe:", report)
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            print("safe with dampener:", report)
            return True
    
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

# Example usage:
file_path = '20241202_01.txt'
reports = read_reports_from_file(file_path)
safe_reports_count = count_safe_reports(reports)

print("Number of safe reports:", safe_reports_count)