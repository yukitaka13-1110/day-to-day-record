import datetime
import glob
import json
import os


class Summary:

    def __init__(self):
        self._status = {
            "basket":0,
            "work-out": 0,
            "core-training": 0,
            "jump-rope": 0,
            "strech": 0,
            "qiita": 0,
            "hatena": 0
        }

    def update(self, begin_date="2019-01-01", end_date="2060-12-31"):
        begin = int("".join(begin_date.split("-")))
        end = int("".join(end_date.split("-")))
        records = glob.glob("./*/**/*.json")
        for record in records:
            date = int(os.path.splitext("".join(record.split("/")[1:]))[0])
            if not (begin < date < end):
                continue
            f = open(record, "r")
            dct = json.load(f)
            status = dct["status"]
            for task in self._status.keys():
                if task not in status:
                    continue
                if status[task]:
                    self._status[task] += 1

    def output(self):
        f = open("README.md", "w")
        f.write("# day-to-day-record  \n")
        date = datetime.datetime.now()
        f.write("## Summary  (%s)  \n" % date)
        for task, total in sorted(self._status.items()):
            f.write("%s : %d  \n" % (task, total))
        f.close()


def main():
    summary = Summary()
    summary.update()
    summary.output()

if __name__ == "__main__":
    main()
