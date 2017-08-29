from dcard import Dcard


def key_word(metas):
    return [meta for meta in metas if '貓' in meta['title']]


if __name__ == '__main__':

    dcard = Dcard()
    metas = dcard.forums('pet').get_metas(num=150, callback=key_word)
    posts = dcard.posts(metas).get(comments=False, links=False)

    resources = posts.parse_resources()

    status, fails = posts.download(resources)
    print('download success! ')
