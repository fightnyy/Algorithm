class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        w_log = []  # word log
        d_log = []  # digit log
        for log in logs:
            if log.split()[1].isdigit():
                d_log.append(log)
            else:
                w_log.append(log)

        w_log = sorted(
            w_log, key=lambda x: (x.split()[1:], x.split()[0])
        )  # 띄어쓰기 한것중에 두번째 꺼 부터 맞추고 다 같으면 그다음것을 사용하라는 의미
        w_log = w_log + d_log  # sorted 와 sort의 차이를 알아야 함
        return w_log
