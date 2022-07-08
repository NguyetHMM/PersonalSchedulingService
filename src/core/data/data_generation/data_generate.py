import json
import random
import uuid
from datetime import datetime, timedelta
from tokenize import String


def generate_uuid():
    return str(uuid.uuid4())


def workdays(d, end, excluded=(6, 7)):
    days = []
    while d.date() <= end.date():
        if d.isoweekday() not in excluded:
            days.append(d)
        d += timedelta(days=1)
    return days


def breaking_time_generation(start_date, end_date):
    start = to_date(start_date)
    end = to_date(end_date)
    # days = date_range(start=start,
    #                   end=end)
    days = workdays(start, end)
    breaking_time = []
    if start.weekday() == 5 or start.weekday() == 6:
        temp1 = {
            'id': generate_uuid(),
            'start_time': start_date,
            'end_time': days[0].date().strftime("%Y-%m-%d") + " 08:00:00",
        }
        breaking_time.append(temp1)
    if end.weekday() == 5 or end.weekday() == 6:
        temp2 = {
            'id': generate_uuid(),
            'start_time': days[len(days)-1].date().strftime("%Y-%m-%d") + " 17:00:00",
            'end_time': end_date,
        }
        breaking_time.append(temp2)
    for i in range(len(days) - 1):
        # temp_d = d.date()
        # temp_d_after = d + timedelta(days=1)
        date_str = days[i].date().strftime("%Y-%m-%d")
        date_str_after = days[i + 1].date().strftime("%Y-%m-%d")
        temp = {
            'id': generate_uuid(),
            'start_time': date_str + " 12:00:00",
            'end_time': date_str + " 13:00:00",
        }
        temp_1 = {
            'id': generate_uuid(),
            'start_time': date_str + " 17:00:00",
            'end_time': date_str_after + " 08:00:00",
        }
        if to_date(temp['start_time']) >= start and to_date(temp['end_time']) <= end:
            breaking_time.append(temp)
        if to_date(temp_1['start_time']) >= start and to_date(temp_1['end_time']) <= end:
            breaking_time.append(temp_1)
    return breaking_time


def print_list_objects(list):
    for x in list:
        print(x)


def get_mid_date(start: datetime, end: datetime):
    mid_date = start + (end - start) / 2
    return mid_date


def get_date_between(start: datetime, end: datetime):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    random_date = (start + timedelta(seconds=random_second)).date()
    return random_date


def job_generation(num, start_date, end_date, breaking_time):
    jobs = []
    start = to_date(start_date)
    end = to_date(end_date)
    mid_date = get_mid_date(start, end)
    mini_mid_date_1 = get_mid_date(start, mid_date)
    mini_mid_date_2 = get_mid_date(mid_date, end)
    day1 = get_date_between(start, mini_mid_date_1)
    day2 = get_date_between(mini_mid_date_1, mid_date)
    day3 = get_date_between(mid_date, mini_mid_date_2)
    day4 = get_date_between(mini_mid_date_2, end)
    # durations = [60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 660, 720,
    #              780, 840, 900, 960]
    durations = [60, 90, 120, 150, 180, 210, 240]
    total_breaking_time = 0
    jobs += [
        {
            "id": generate_uuid(),
            "name": random.choice(jobs_name),
            "early_start_time": day1.strftime("%Y-%m-%d") + " 08:00:00",
            "late_finish_time": day1.strftime("%Y-%m-%d") + " 10:00:00",
            "estimated_time": 120,
            "flextime": 0
        },
        {
            "id": generate_uuid(),
            "name": random.choice(jobs_name),
            "early_start_time": day2.strftime("%Y-%m-%d") + " 08:00:00",
            "late_finish_time": day2.strftime("%Y-%m-%d") + " 10:00:00",
            "estimated_time": 120,
            "flextime": 0
        },
        {
            "id": generate_uuid(),
            "name": random.choice(jobs_name),
            "early_start_time": day3.strftime("%Y-%m-%d") + " 08:00:00",
            "late_finish_time": day3.strftime("%Y-%m-%d") + " 10:00:00",
            "estimated_time": 120,
            "flextime": 0
        },
        {
            "id": generate_uuid(),
            "name": random.choice(jobs_name),
            "early_start_time": day4.strftime("%Y-%m-%d") + " 08:00:00",
            "late_finish_time": day4.strftime("%Y-%m-%d") + " 10:00:00",
            "estimated_time": 120,
            "flextime": 0
        },
    ]
    for t in breaking_time:
        end_time = to_date(t['end_time'])
        start_time = to_date(t['start_time'])
        total_breaking_time += difference_between_to_date(later_date=end_time,
                                                          first_date=start_time)

    fix_time = 480 + 480

    available_time = difference_between_to_date(later_date=to_date(end_date),
                                                first_date=to_date(start_date)) - total_breaking_time - fix_time

    remaining_time = available_time
    ran_start_date1 = get_date_between(start, end)
    ran_end_date1 = get_date_between(datetime.combine(ran_start_date1, datetime.min.time()), end)

    ran_start_date2 = get_date_between(start, end)
    ran_end_date2 = get_date_between(datetime.combine(ran_start_date2, datetime.min.time()), end)
    jobs += [
        {
            "id": generate_uuid(),
            "name": random.choice(jobs_name),
            "early_start_time": ran_start_date1.strftime("%Y-%m-%d") + " 08:00:00",
            "late_finish_time": ran_end_date1.strftime("%Y-%m-%d") + " 17:00:00",
            "estimated_time": 240,
            "flextime": 1
        },
        {
            "id": generate_uuid(),
            "name": random.choice(jobs_name),
            "early_start_time": ran_start_date2.strftime("%Y-%m-%d") + " 08:00:00",
            "late_finish_time": ran_end_date2.strftime("%Y-%m-%d") + " 17:00:00",
            "estimated_time": 240,
            "flextime": 1
        }]
    for i in range(num - 6):
        name = random.choice(jobs_name)
        job_duration = 0
        get_index_done = False
        while not get_index_done:
            job_duration = random.choice(durations)
            print(job_duration, "job_duration")
            print(remaining_time,"remaining_time")
            if job_duration < remaining_time:
                remaining_time = remaining_time - job_duration
                print("inif")
                get_index_done = True

        temp = {
            "id": generate_uuid(),
            "name": name,
            "early_start_time": start.strftime("%Y-%m-%d %H:%M:%S"),
            "late_finish_time": end.strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_time": job_duration,
            "flextime": 1
        }
        jobs.append(temp)

    return jobs


def date_range(start, end):
    delta = end - start  # as timedelta.
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days


def to_date(datetime_str: String):
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def difference_between_to_date(later_date, first_date):
    duration = later_date - first_date
    duration_in_s = duration.total_seconds()
    minutes = divmod(duration_in_s, 60)[0]
    return minutes


hour = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

minute = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]

jobs_name = [
    "Viết nhật ký thí nghiệm",
    "Ghi nhật ký thí nghiệm",
    "Chép nhật ký thí nghiệm",
    "Chép nhật ký thí nghiệm",
    "Viết nhật ký thí nhiệm",
    "Ghi nhật ký thí nhiệm",
    "Nhật ký thí nghiệm",
    "Viết sổ tay nghiên cứu",
    "Ghi chép sổ tay thí nghiệm",
    "Viết nhật ký nghiên cứu",
    "Viết báo cáo",
    "Gửi báo cáo",
    "Hoàn thành báo cáo",
    "Hoàn thiện báo cáo",
    "Báo cáo kết quả",
    "Báo cáo thí nghiệm",
    "Báo cáo nghiên cứu",
    "Báo cáo thí nghiệm",
    "Tổng kết nghiên cứu",
    "Kết quả nghiên cứu",
    "Ghi lại kết quả",
    "Tổng hợp báo cáo",
    "Chuẩn bị báo cáo",
    "Thực hiện báo cáo",
    "Huấn luyện mô hình",
    "Train mô hình",
    "Dạy mô hình",
    "Tiến hành huấn luyện mô hình",
    "Thực hiện huấn luyện mô hình học sâu",
    "Đánh giá mô hình",
    "Thực hiện đánh giá mô hình",
    "Đánh giá mô hình học sâu",
    "Test mô hình",
    "Evaluate mô hình",
    "Chạy thử mô hình",
    "Kiểm tra mô hình",
    "Họp giao ban",
    "Họp bàn giao công việc",
    "Họp tổng kết công việc",
    "Họp báo cáo công việc",
    "Họp bàn về công việc",
    "Họp hàng tuần",
    "Họp bàn giao công việc",
    "Hoàn thành lý lịch khoa học",
    "Điền thông tin lý lịch khoa học",
    "Thu thập thông tin lý lịch khoa học",
    "Viết lý lịch khoa học",
    "Hoàn thiện lý lịch khoa học",
    "Hoàn thành hồ sơ khoa học",
    "Hoàn thành hồ sơ lý lịch khoa học",
    "Kê khai lý lịch khoa học",
    "Cung cấp thông tin lý lịch khoa học",
    "Hoàn thành LLKH",
    "Kê khai LLKH",
    "Hoàn thiện LLKH",
    "Gặp mặt đối tác",
    "Gặp đối tác",
    "Họp với đối tác",
    "Gặp gỡ bên liên kết",
    "Họp mặt với đối tác",
    "Giao lưu với đối tác",
    "Gặp người hợp tác",
    "Gặp mặt người hợp tác",
    "Gặp mặt bên đối tác",
    "Gặp bên đối tác",
    "Họp với bên đối tác",
    "Viết báo khoa học",
    "Hoàn thành bài báo khoa học",
    "Viết báo",
    "Viết bài báo",
    "Chuẩn bị bài báo",
    "Viết báo cho hội nghị khoa học",
    "Viết bài báo cho hội nghị quốc tế",
    "Làm bài báo",
    "Hoàn thành bài báo",
    "Viết bài journal",
    "Viết bài",
    "Viết báo journal",
    "Hoàn thiện bài báo",
    "Đọc báo khoa học",
    "Tham khảo bài báo khoa học",
    "Đọc báo",
    "Đọc bài báo",
    "Đọc bài journal",
    "Tham khảo bài báo",
    "Nghiên cứu bài báo",
    "Nghiên cứu bài journal",
    "Nghiên cứu báo khoa học",
    "Làm web",
    "Viết web",
    "Code web",
    "Viết script cho website",
    "Làm website",
    "Lập trình website",
    "Viết web service",
    "Viết dịch vụ web",
    "Hoàn thành website",
    "Hoàn thiện website",
    "Cài đặt website",
    "Triển khai web",
    "Triển khai web service",
    "Liên hệ đối tác",
    "Liên lạc với đối tác",
    "Gọi cho đối tác",
    "Gửi thông tin cho đối tác",
    "Gọi cho bên hợp tác",
    "Liên hệ với bên hợp tác",
    "Thông báo cho đối tác",
    "Thu thập dữ liệu",
    "Lấy dữ liệu",
    "Thực hiện thu thập dữ liệu",
    "Thu thập tập dữ liệu",
    "Thu dữ liệu",
    "Thu thập và tổng hợp dữ liệu",
    "Collect dữ liệu",
    "Collect dataset",
    "Ghi nhận dữ liệu",
    "Hoàn thiện hồ sơ đề tài",
    "Hoàn thiện hồ sơ cho đề tài",
    "Hoàn thiện hồ sơ dự án",
    "Hoàn thành hồ sơ đề tài",
    "Hoàn thành hồ sơ cho đề tài",
    "Hoàn thành đầy đủ hồ sơ đề tài",
    "Hoàn thành đầy đủ hồ sơ dự án",
    "Hoàn thành đầy đủ hồ sơ đề tài cấp bộ",
    "Tham dự hội nghị",
    "Tham gia hội nghị",
    "Đi hội nghị",
    "Nộp bài tham dự hội nghị",
    "Nộp báo tham dự hội nghị quốc tế",
]

if __name__ == "__main__":
    start_date = "2022-07-01 08:00:00"
    end_date = "2022-07-21 17:00:00"

    breaking_time = breaking_time_generation(start_date=start_date,
                                             end_date=end_date)

    get_date_between(start=to_date(start_date),
                     end=to_date(end_date))

    jobs = job_generation(36, start_date, end_date, breaking_time)

    input_data = {
        "schedule_start_time": start_date,
        "schedule_end_time": end_date,
        "jobs": jobs,
        "breaking_time_slots": breaking_time,
        "scheduled_working_time_slots": []
    }

    with open('input_36.json', 'w') as file:
        json.dump(input_data, file, indent=2, separators=(',', ':'), ensure_ascii=False)

    print_list_objects(jobs)
    print_list_objects(breaking_time)