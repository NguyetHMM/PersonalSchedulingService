from enum import Enum


class TabuMessageException(str, Enum):
    RANG_BUOC_4 = 'Thời điểm bắt đầu lập lịch cần sớm hơn thời điểm kết thúc gợi ý lập lịch'
    RANG_BUOC_8 = 'Các công việc cố định và thời gian nghỉ không được giao nhau'
    RANG_BUOC_6 = 'Mọi công việc cần lập lịch đều có thời gian bắt đầu sớm nhất muộn hơn hoặc bằng thời điểm bắt đầu gợi ý lịch trình và thời hạn của công việc sớm hơn hoặc bằng thời điểm kết thúc gợi ý lập lịch'
    RANG_BUOC_5 = 'Mọi công việc trong lịch trình đều có 〖jt〗_i nhỏ hơn hoặc bằng khoảng thời gian từ thời gian bắt đầu sớm nhất đến thời hạn của công việc, hay nói cách khác công việc t_i sẽ không cần dành ra 100% từ thời điểm được giao đến thời điểm thời hạn để hoàn thành.'
    RANG_BUOC_7 = 'Tổng thời gian từ thời điểm bắt đầu lập lịch đến thời điểm kết thúc lập lịch cần lớn hơn hoặc bằng tổng thời gian ước lượng hoàn thành công việc'

class TabuException(Exception):
    message: str

    def __init__(self, message: TabuMessageException):
        self.message = message.value

    def __repr__(self):
        return f"{self.__class__}: {self.message}"
