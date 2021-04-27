class Solution:
    def validUtf8(self, data):
        start = 0
        # set_trace()

        def isTrue(many):
            # set_trace()
            for i in range(1, many + 1):
                if (start + i) >= len(data) or data[start + i] >> 6 != 0b10:
                    return False
            return True

        while start < len(data):
            check = data[start]  # 0b11110000
            # 0b11100000
            # 0b11000000
            # 0b01111111
            if check >> 3 == 0b11110:
                if not isTrue(3):
                    return False
                start += 4
            elif check >> 4 == 0b1110:
                if not isTrue(2):
                    return False
                start += 3
            elif check >> 5 == 0b110:
                if not isTrue(1):
                    return False
                start += 2
            elif check >> 7 == 0b0:
                start += 1
                continue
            else:
                return False

        return True
