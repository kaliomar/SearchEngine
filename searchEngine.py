index = []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if url not in entry[1]:
                entry[1].append(url)
            return
    index.append([keyword, [url]])


def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []


def add_page_to_index(index, url, content):
    keywords = content.split()
    for word in keywords:
        add_to_index(index, word, url)


# add_to_index(index, 'udacity', 'http://udacity.com')
# add_to_index(index, 'computing', 'http://acm.org')
# add_to_index(index, 'udacity', 'http://npr.org')
# print (index)
# print (lookup(index, 'udacity'))
# # add_page_to_index(index, 'fake.test', "this is a is test")
# # add_page_to_index(index, 'not.test', "this is not a test")
# # print (index)
