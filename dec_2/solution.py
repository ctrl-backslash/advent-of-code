def is_safe(report_values: list[int]):
    if report_values[0] == report_values[1]:
        return False
    increasing = report_values[0] < report_values[1]
    for idx in range(1, len(report_values)):
        if (report_values[idx - 1] < report_values[idx]) != increasing or not (
            1 <= abs(report_values[idx - 1] - report_values[idx]) <= 3
        ):
            return False
    return True


def part1(input: list[str]):
    safe_reports = 0
    for report in input:
        if is_safe([int(num) for num in report.split()]):
            safe_reports += 1
    return safe_reports


def part2(input: list[str]):
    safe_reports = 0
    for report in input:
        report_values = [int(num) for num in report.split()]
        if is_safe(report_values):
            safe_reports += 1
            continue
        for idx in range(len(report_values)):
            if is_safe(report_values[:idx] + report_values[idx + 1 :]):
                safe_reports += 1
                break

    return safe_reports
