import pyshark


class CaptureParser:

    def open_capture(self):
        capture = pyshark.FileCapture("capture/stats.pcapng", only_summaries=True)
        capture.load_packets()
        self.count_packets(capture)
        pass

    def count_packets(self, capture):
        size = len(capture)
        self.average_exchange_time(capture, size)
        pass

    @staticmethod
    def average_exchange_time(capture, size):
        total_time = capture[size - 1].time
        average_time = float(total_time) / size

        print("Average packet exchange time: " + str(average_time))