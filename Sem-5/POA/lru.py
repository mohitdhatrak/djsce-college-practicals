def lru(pages, frames):
    s = set()
    indexes = {}
    page_f = 0

    for i in range(len(pages)):
        if len(s) < frames:
            if pages[i] not in s:
                s.add(pages[i])
                page_f = page_f + 1
                print(f"Page {pages[i]} added to frame. Page fault!")
            else:
                print(f"Page {pages[i]} exists in frame. Page hit!")
            indexes[pages[i]] = i  # we store the key value pair -> page: index

        else:
            if pages[i] not in s:
                lru = float("inf")  # positive infinity
                val = None
                for item in s:
                    # check full set, get smallest index page, i.e. least recent used page
                    if indexes[item] < lru:
                        lru = indexes[item]
                        val = item

                s.remove(val)  # remove val in queue from set
                s.add(pages[i])

                page_f = page_f + 1
                print(f"Page {val} replaced with Page {pages[i]}. Page fault!")
            else:
                print(f"Page {pages[i]} exists in frame. Page hit!")
            indexes[pages[i]] = i
    return page_f


pages = [7, 0, 1, 2, 0, 4, 2, 0, 3]
frames = 4
x = lru(pages, frames)

print("No of miss = ", x)
print("No of hits = ", len(pages) - x)
