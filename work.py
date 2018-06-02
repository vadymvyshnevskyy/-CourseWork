import codecs
import folium


def coordinates():
    """

    :return: list of dicts
    """
    lst = []
    with codecs.open("address20180419.csv", "r", "utf-8") as file:
        for i in file:
            i = i.strip("\n").strip("\r")
            i = i.replace("\"", "").split(";")
            lst.append(i)
        for r in lst:
            filter(None, r)
            print(r)
        print(lst)


coordinates()


def calls():
    """

    :return:
    """
    lst = []
    with codecs.open("glm2015.csv", "r") as file:
        for i in file:
            i = i.strip("\n")
            i = i.split(";")
            lst.append(i)
        for i in lst:
            i.remove(i[0])
        print(lst)
#calls()


def map():
    """

    :return:
    """
    map_lviv = folium.Map(location=[49.83826, 24.02324], zoom_start=12,
                          tiles="OpenStreetMap")
    map_lviv.save("map.html")
