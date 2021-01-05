from django.shortcuts import render,redirect
from project1.settings import Covid_19_file
from app1.middleware import cov19
import json

def Mainpage(request):
    dict_data = json.loads(open(Covid_19_file).read())
    states = [x for x in dict_data]
    states.pop(0)
    print(states)
    r=0
    # stat = json.loads(state)
    # states = {stat}
    total_count = [

        [[],[],[],[]],[[], [], [], []],[[], [], [], []],[[], [], [], []],[[], [], [], []],[[], [], [], []],[[], [], [], []],
        [[], [], [], []],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],
        [[], [], [], []],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],
        [[], [], [], []],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],

    ]
    # total_count = [[], [], [], []]
    # for x in dict_data[sname]['districtData']:
    #     for k,v in dict_data[sname]['districtData'][x].items():

    # for s in states:
    #
    #     for x in dict_data[s]['districtData']:
    #         for k, v in dict_data[s]['districtData'][x].items():
    #             if k != 'delta' and k != 'notes':
    #                 if k == "active":
    #                     total_count[r][0].append(v)
    #                 elif k == "confirmed":
    #                     total_count[r][1].append(v)
    #                 elif k == "deceased":
    #                     total_count[r][2].append(v)
    #                 else:
    #                     total_count[r][3].append(v)
    # r=r+1




    # total = [{"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #               "recovered": sum(total_count[3])}]


    total = [
        {"a":{"active":sum(total_count[0][0]),"confirmed":sum(total_count[0][1]),"deceased":sum(total_count[0][2]),
                 "recovered":sum(total_count[0][3])}},
        {"b": {"active": sum(total_count[1][0]), "confirmed": sum(total_count[1][1]),
               "deceased": sum(total_count[1][2]),
               "recovered": sum(total_count[1][3])}},
        {"c": {"active": sum(total_count[2][0]), "confirmed": sum(total_count[2][1]),
               "deceased": sum(total_count[2][2]),"recovered": sum(total_count[2][3])}},
        {"d": {"active": sum(total_count[3][0]), "confirmed": sum(total_count[3][1]),
               "deceased": sum(total_count[3][2]),"recovered": sum(total_count[3][3])}},
        {"e": {"active": sum(total_count[4][0]), "confirmed": sum(total_count[4][1]),
               "deceased": sum(total_count[4][2]), "recovered": sum(total_count[4][3])}},
        {"f": {"active": sum(total_count[5][0]), "confirmed": sum(total_count[5][1]),
               "deceased": sum(total_count[5][2]), "recovered": sum(total_count[5][3])}},
        {"g": {"active": sum(total_count[6][0]), "confirmed": sum(total_count[6][1]),
               "deceased": sum(total_count[6][2]), "recovered": sum(total_count[6][3])}},
        {"h": {"active": sum(total_count[7][0]), "confirmed": sum(total_count[7][1]),
               "deceased": sum(total_count[7][2]), "recovered": sum(total_count[7][3])}},
        {"i": {"active": sum(total_count[8][0]), "confirmed": sum(total_count[8][1]),
               "deceased": sum(total_count[8][2]), "recovered": sum(total_count[8][3])}},
        {"j": {"active": sum(total_count[9][0]), "confirmed": sum(total_count[9][1]),
               "deceased": sum(total_count[9][2]), "recovered": sum(total_count[9][3])}},
        {"k": {"active": sum(total_count[10][0]), "confirmed": sum(total_count[10][1]),
               "deceased": sum(total_count[10][2]), "recovered": sum(total_count[10][3])}},
        {"l": {"active": sum(total_count[11][0]), "confirmed": sum(total_count[11][1]),
               "deceased": sum(total_count[11][2]), "recovered": sum(total_count[11][3])}},
        {"m": {"active": sum(total_count[12][0]), "confirmed": sum(total_count[12][1]),
               "deceased": sum(total_count[12][2]), "recovered": sum(total_count[12][3])}},
        {"n": {"active": sum(total_count[13][0]), "confirmed": sum(total_count[13][1]),
               "deceased": sum(total_count[13][2]), "recovered": sum(total_count[13][3])}},
        {"o": {"active": sum(total_count[14][0]), "confirmed": sum(total_count[14][1]),
               "deceased": sum(total_count[14][2]), "recovered": sum(total_count[14][3])}},
        {"p": {"active": sum(total_count[15][0]), "confirmed": sum(total_count[15][1]),
               "deceased": sum(total_count[15][2]), "recovered": sum(total_count[15][3])}},
        {"q": {"active": sum(total_count[16][0]), "confirmed": sum(total_count[16][1]),
               "deceased": sum(total_count[16][2]), "recovered": sum(total_count[16][3])}},
        {"r": {"active": sum(total_count[17][0]), "confirmed": sum(total_count[17][1]),
               "deceased": sum(total_count[17][2]), "recovered": sum(total_count[17][3])}},
        {"s": {"active": sum(total_count[18][0]), "confirmed": sum(total_count[18][1]),
               "deceased": sum(total_count[18][2]), "recovered": sum(total_count[18][3])}},
        {"t": {"active": sum(total_count[19][0]), "confirmed": sum(total_count[19][1]),
               "deceased": sum(total_count[19][2]), "recovered": sum(total_count[19][3])}},
        {"u": {"active": sum(total_count[20][0]), "confirmed": sum(total_count[20][1]),
               "deceased": sum(total_count[20][2]), "recovered": sum(total_count[20][3])}},
        {"v": {"active": sum(total_count[21][0]), "confirmed": sum(total_count[21][1]),
               "deceased": sum(total_count[21][2]), "recovered": sum(total_count[21][3])}},
        {"w": {"active": sum(total_count[22][0]), "confirmed": sum(total_count[22][1]),
               "deceased": sum(total_count[22][2]), "recovered": sum(total_count[22][3])}},
        {"x": {"active": sum(total_count[23][0]), "confirmed": sum(total_count[23][1]),
               "deceased": sum(total_count[23][2]), "recovered": sum(total_count[23][3])}},
        {"y": {"active": sum(total_count[24][0]), "confirmed": sum(total_count[24][1]),
               "deceased": sum(total_count[24][2]), "recovered": sum(total_count[24][3])}},
        {"z": {"active": sum(total_count[25][0]), "confirmed": sum(total_count[25][1]),
               "deceased": sum(total_count[25][2]), "recovered": sum(total_count[25][3])}},
        {"aa": {"active": sum(total_count[26][0]), "confirmed": sum(total_count[26][1]),
               "deceased": sum(total_count[26][2]), "recovered": sum(total_count[26][3])}},
        {"ab": {"active": sum(total_count[27][0]), "confirmed": sum(total_count[27][1]),
               "deceased": sum(total_count[27][2]), "recovered": sum(total_count[27][3])}},





    ]


    # total = [
    #     ({"1":{"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #               "recovered": sum(total_count[3])}}),
    #     ({"2": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}),
    #     ({"3": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}),
    #             ({"4": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}),
    #     [{"5": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"6": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"7": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"8": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"9": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"10": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"11": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"12": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"13": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"14": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"15": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"16": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"17": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"18": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"19": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"20": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"21": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"22": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"24": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"25": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"26": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"27": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}],
    #     [{"28": {"active": sum(total_count[0]), "confirmed": sum(total_count[1]), "deceased": sum(total_count[2]),
    #             "recovered": sum(total_count[3])}}]
    #      ]


    return render(request,"index.html",{"data":states,"info":total})


def open_state(request):
    sname = request.GET.get("state_name")
    dict_data = json.loads(open(Covid_19_file).read())
    total_count = [[],[],[],[]]
    for x in dict_data[sname]['districtData']:
        for k,v in dict_data[sname]['districtData'][x].items():
            if k != 'delta' and k != 'notes':
                if k == "active":
                    total_count[0].append(v)
                elif k == "confirmed":
                    total_count[1].append(v)
                elif k == "deceased":
                    total_count[2].append(v)
                else:
                    total_count[3].append(v)
    total = [{"active":sum(total_count[0]),"confirmed":sum(total_count[1]),"deceased":sum(total_count[2]),"recovered":sum(total_count[3])}]
    return render(request,"state.html",{"sname":sname,"data":dict_data[sname],"info":total})


def refresh(request):
    cov19()
    # sname = request.GET.get("state_name")
    # dict_data = json.loads(open(Covid_19_file).read())
    # return render(request, "state.html", {"sname": sname, "data": dict_data[sname]})
    return open_state(request)
