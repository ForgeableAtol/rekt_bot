import praw
import time

rekt_list = """
☐ Not REKT\n
☑ REKT\n
☑ REKTangle\n
☑ SHREKT\n
☑ REKT-it Ralph\n
☑ Total REKTall\n
☑ The Lord of the REKT\n
☑ The Usual SusREKTs\n
☑ North by NorthREKT\n
☑ REKT to the Future\n
☑ Once Upon a Time in the REKT\n
☑ The Good, the Bad, and the REKT\n
☑ LawREKT of Arabia\n
☑ Tyrannosaurus REKT\n
☑ eREKTile dysfunction\n
"""

been_rekt = frozenset()

rektbot = praw.Reddit('JustGotRekt 1.0')
rektbot.login(username='JustGotRekt', password='rektbot2015')

for x in range(0,10):
    comments = rektbot.get_comments('askreddit')
    for comment in comments:
        body = comment.body.lower()
        if body.find('rekt') != -1 and comment.id not in been_rekt:
            comment.reply(rekt_list)
            been_rekt.append(comment.id)
    time.sleep(120)
