from flask import Blueprint, render_template, url_for
import random

views = Blueprint(__name__, "home")



@views.route("/", methods=['GET', 'POST'])
def home():
    chance = [1, 2]
    n = random.choices(chance)
    return render_template("home.html", sibl=n)

@views.route("/characters/")
def characters():
    chance = [1, 2]
    n = random.choices(chance)
    return render_template("char.html", sibl=n)


@views.route("/weapons/")
def weapons():
    chance = [1, 2]
    n = random.choices(chance)
    return render_template("weap.html", sibl=n)

@views.route("/artifacts/")
def artifacts():
    chance = [1, 2]
    n = random.choices(chance)
    return render_template("arti.html", sibl=n)

@views.route("/characters/<hero>/")
def indiv(hero):
    x = str(hero)
    y = x.lower()
    if y in ["albedo", "aloy", "amber", "arataki itto", "barbara", "beidou", "bennett", "chongyun", "diluc", "diona", "eula", "fischl", "ganyu", "gorou", "hu tao", "jean", "kaedehara kazuha", "kaeya", "kamisato ayaka", "kamisato ayato", "keqing", "klee", "kujou sara", "lisa", "mona", "ningguang", "noelle", "qiqi", "raiden shogun", "razor", "rosaria", "sangonomiya kokomi", "sayu", "shenhe", "sucrose", "tartaglia", "thoma", "traveler anemo", "traveler geo", "traveler electro", "venti", "xiangling", "xiao", "xinyan", "xinqiu", "yae miko", "yanfei", "yoimiya", "yunjin", "zhongli",]:

        return render_template("indiv/" + x + ".html")

    elif y in ["aratakiitto", "arataki", "itto", "itto arataki", "aratakiitto"]:
        x = "Arataki Itto"

        return render_template("indiv/" + x + ".html")

    elif y in ["hutao"]:
        x = "Hu Tao"

        return render_template("indiv/" + x + ".html")

    elif y in ["kaedeharakazuha", "kaedehara", "kazuha", "kazuha kaedehara", "kazuhakaedehara"]:
        x = "Kaedehara Kazuha"

        return render_template("indiv/" + x + ".html")

    elif y in ["kamisatoayaka", "ayaka", "ayaka kamisato", "ayakakamisato"]:
        x = "Kamisato Ayaka"

        return render_template("indiv/" + x + ".html")

    elif y in ["kamisatoayato", "ayato", "ayato kamisato", "ayatokamisato"]:
        x = "Kamisato Ayato"

        return render_template("indiv/" + x + ".html")

    elif y in ["kujousara", "kujou", "sara", "sara kujou", "sarakujou"]:
        x = "Kujou Sara"

        return render_template("indiv/" + x + ".html")

    elif y in ["raidenshogun", "raiden", "ei", "baal", "shogun", "shogun raiden", "shogunraiden"]:
        x = "Raiden Shogun"

        return render_template("indiv/" + x + ".html")

    elif y in ["sangonomiyakokomi", "sangonomiya", "kokomi", "kokomi sangonomiya", "kokomisangonomiya"]:
        x = "Sangonomiya Kokomi"

        return render_template("indiv/" + x + ".html")

    elif y in ["traveleranemo", "anemo traveler", "anemotraveler"]:
        x = "Traveler Anemo"

        return render_template("indiv/" + x + ".html")

    elif y in ["travelergeo", "geo traveler", "geotraveler"]:
        x = "Traveler Geo"

        return render_template("indiv/" + x + ".html")

    elif y in ["travelerelectro", "electro traveler", "electrotraveler"]:
        x = "Traveler Electro"

        return render_template("indiv/" + x + ".html")

    elif y in ["yaemiko", "yae", "miko", "miko yae", "mikoyae"]:
        x = "Yae Miko"

        return render_template("indiv/" + x + ".html")


    elif y in ["yelan", "kuki shinobu", "kukishinobu", "kuki", "shinobu", "shinobu kuki", "shinobukuki",]:
        if y in  ["kukishinobu", "kuki", "shinobu", "shinobu kuki", "shinobukuki",]:
            y = "kuki shinobu"
        x = y.title()
        return render_template("nope.html", name=x, aftertext="Sorry! this character has not been released yet")

    elif y in ["kamisato"]:
        return render_template("nope.html", name="Kamisato", aftertext="Please specify which sibling.", command="bruh")

    elif y in ["who"]:
        return render_template("nope.html", name="Who?", aftertext="Tao, yes")

    elif y in ["aether", "lumine", "traveler"]:
        return render_template("nope.html", name="Traveler", aftertext="Please specify which element.", command2="bruh2")

    else:
        return render_template("nope.html", name="Unknown", aftertext="Sorry! this character does not exist")