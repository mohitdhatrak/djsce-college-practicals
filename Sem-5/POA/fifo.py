from collections import deque


def fifo(pages, frames):
    s = set()
    indexes = deque()
    page_f = 0

    for page in pages:
        if len(s) < frames:
            if page not in s:
                s.add(page)
                page_f = page_f + 1
                indexes.append(page)
                print(f"Page {page} added to frame. Page fault!")
            else:
                print(f"Page {page} exists in frame. Page hit!")

        else:
            if page not in s:
                val = indexes.popleft()  # get first in queue, as FIFO
                s.remove(val)  # remove val in queue from set

                s.add(page)
                indexes.append(page)

                page_f = page_f + 1
                print(f"Page {val} replaced with Page {page}. Page fault!")
            else:
                print(f"Page {page} exists in frame. Page hit!")

    return page_f


pages = [7, 0, 1, 2, 0, 4, 2, 0, 3]
frames = 4
x = fifo(pages, frames)

print("No of miss = ", x)
print("No of hits = ", len(pages) - x)
